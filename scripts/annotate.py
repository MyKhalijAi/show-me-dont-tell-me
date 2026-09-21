"""
annotate.py — helpers for show-me-dont-tell-me annotated screenshots.

Usage:
    from annotate import Annot
    a = Annot("capture.png")
    a.blur(120, 300, 420, 28)          # redact BEFORE annotating
    a.frame(980, 550, 460, 50)
    a.arrow(1500, 575, 1450, 575)
    a.marker(1540, 575, 1)
    a.crop_around(980, 400, 900, 500)
    a.save("etape-01-telecharger.png")

Requires: pillow
"""
from __future__ import annotations
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

NOW = "#ff3b30"      # do this now
NEXT = "#2ea043"     # afterwards
WARN = "#f0b429"     # warning
WHITE = "#ffffff"

_FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans{bold}.ttf",
    "/System/Library/Fonts/Supplemental/DejaVuSans{bold}.ttf",
    "C:/Windows/Fonts/segoeui{boldwin}.ttf",
]


def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    for pat in _FONT_CANDIDATES:
        p = pat.format(bold="-Bold" if bold else "", boldwin="b" if bold else "")
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


class Annot:
    """Annotate a screenshot. Redact first, annotate second, verify third."""

    def __init__(self, src: str | Path | Image.Image):
        self.img = src.copy() if isinstance(src, Image.Image) else Image.open(src)
        self.img = self.img.convert("RGB")
        self.d = ImageDraw.Draw(self.img)
        self.rtl = False

    # ---------- step 2: redaction ----------
    def blur(self, x: int, y: int, w: int, h: int, radius: int = 12) -> "Annot":
        """Blur a region. Keeps the shape so the reader still sees a field is there."""
        box = (x, y, x + w, y + h)
        self.img.paste(self.img.crop(box).filter(ImageFilter.GaussianBlur(radius)), box)
        return self

    def blur_all(self, regions, radius: int = 12) -> "Annot":
        for r in regions:
            self.blur(*r, radius=radius)
        return self

    # ---------- step 3: annotation ----------
    def frame(self, x: int, y: int, w: int, h: int, color: str = NOW, width: int = 5) -> "Annot":
        self.d.rounded_rectangle([x, y, x + w, y + h], radius=8, outline=color, width=width)
        return self

    def arrow(self, x1: int, y1: int, x2: int, y2: int, color: str = NOW, width: int = 5) -> "Annot":
        self.d.line([x1, y1, x2, y2], fill=color, width=width)
        a = math.atan2(y2 - y1, x2 - x1)
        L, s = 20, 0.5
        self.d.polygon(
            [(x2, y2),
             (x2 - L * math.cos(a - s), y2 - L * math.sin(a - s)),
             (x2 - L * math.cos(a + s), y2 - L * math.sin(a + s))],
            fill=color,
        )
        return self

    def marker(self, cx: int, cy: int, n: int, color: str = NOW, r: int = 26) -> "Annot":
        self.d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color, outline=WHITE, width=4)
        t = str(n)
        f = _font(int(r * 1.15), True)
        bb = self.d.textbbox((0, 0), t, font=f)
        self.d.text((cx - (bb[2] - bb[0]) / 2, cy - (bb[3] - bb[1]) / 2 - r * 0.19),
                    t, font=f, fill=WHITE)
        return self

    def point_at(self, tx: int, ty: int, n: int, color: str = NOW,
                 gap: int = 12, reach: int = 76) -> "Annot":
        """Marker + arrow aimed at (tx, ty). Mirrors automatically in RTL mode."""
        side = -1 if self.rtl else 1
        mx = tx + side * reach
        self.arrow(tx + side * (reach - 32), ty, tx + side * gap, ty, color)
        self.marker(mx, ty, n, color)
        return self

    def set_rtl(self, rtl: bool = True) -> "Annot":
        """Arabic/Hebrew UIs: markers go left of the target, arrows point right."""
        self.rtl = rtl
        return self

    def zoom_inset(self, x: int, y: int, w: int, h: int,
                   at: tuple[int, int], factor: int = 3, color: str = NOW) -> "Annot":
        """Magnified inset for targets under ~40 px."""
        crop = self.img.crop((x, y, x + w, y + h)).resize((w * factor, h * factor), Image.LANCZOS)
        self.img.paste(crop, at)
        self.d = ImageDraw.Draw(self.img)
        self.d.rectangle([at[0], at[1], at[0] + w * factor, at[1] + h * factor],
                         outline=color, width=4)
        return self

    def label(self, x: int, y: int, text: str, size: int = 20,
              color: str = WHITE, bg: str | None = "#00000099") -> "Annot":
        f = _font(size, True)
        if bg:
            bb = self.d.textbbox((x, y), text, font=f)
            self.d.rectangle([bb[0] - 8, bb[1] - 6, bb[2] + 8, bb[3] + 6], fill=bg)
        self.d.text((x, y), text, font=f, fill=color)
        return self

    def watermark_reconstructed(self) -> "Annot":
        """Mandatory when the image is a redrawn schematic, not a real capture."""
        return self.label(16, 16, "schema reconstruit / reconstructed schematic", 18, WARN, "#000000cc")

    # ---------- framing ----------
    def crop_around(self, cx: int, cy: int, w: int, h: int) -> "Annot":
        W, H = self.img.size
        x = max(0, min(cx - w // 2, W - w))
        y = max(0, min(cy - h // 2, H - h))
        self.img = self.img.crop((x, y, x + w, y + h))
        self.d = ImageDraw.Draw(self.img)
        return self

    def save(self, path: str | Path, max_width: int | None = 1440) -> Path:
        if max_width and self.img.width > max_width:
            r = max_width / self.img.width
            self.img = self.img.resize((max_width, int(self.img.height * r)), Image.LANCZOS)
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        self.img.save(p)
        return p
