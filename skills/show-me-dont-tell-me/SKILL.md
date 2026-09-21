---
name: show-me-dont-tell-me
description: Build step-by-step tutorials and live assistance from annotated screenshots — numbered markers, arrows, zoom — instead of paragraphs describing a button. Use to document an app, guide a setting, troubleshoot an interface, or assist live on the user's screen.
---

# show-me-dont-tell-me

Every step = **one annotated image + one line of action**. The text never describes what the image already shows.

Answer in the user's language.

## Absolute rule

Never describe an interface from memory. Real capture or source code first, writing second. Interfaces change between versions; an invented instruction costs more time than it saves.

If nothing is obtainable: say so and ask for a screenshot. Never guess where a button is.

---

## Step 0 — Triage the request

Four modes. The mode decides everything downstream. If the request is ambiguous, ask **one** question to settle it.

| Mode | Triggered by | Captures | Output |
|---|---|---|---|
| **LIVE** | "help me with", "I'm stuck", a session in progress | 1 per message, recapture before each instruction | short message + image |
| **DOC** | "document this", "tutorial for my app" | 1 per step + edge states | structured document, images inline |
| **TROUBLESHOOT** | a specific error, "it's not working" | capture of the error + of the fix | cause → fix → verification |
| **SCRIPT** | "video", "screencast", "training" | 1 per shot | timed script, numbered shots |

### Audience

Identify who it is for — it changes vocabulary and how much "why" to include:

- **End customer** — zero technical jargon, never a server file path, reassuring tone on errors.
- **Internal team** — house jargon allowed, keyboard shortcuts, edge cases.
- **Your future self** — record decisions and reasons, not only gestures.

---

## Step 1 — Source of truth

### When it is the user's own application

Read the code **before** capturing. This is the skill's biggest accuracy gain.

1. **Exact labels** — i18n files, templates, constants. Copy strings verbatim, never paraphrase or translate.
2. **Full journey** — routes, controllers, validators: they reveal the screens the user would not think to show.
3. **States to document**, not just the happy path: empty list, invalid field, loading, permission denied, quota reached, network failure. A tutorial that skips the validation error is the one that generates the support ticket.
4. **Prerequisites** — role, data or setting needed before step 1. State them first.

### Getting an image file

Annotation needs a **file on disk**. An image that only arrives in the conversation cannot be modified.

In order of preference:

1. **Screenshot supplied by the user** — already a file.
2. **Browser** — `mcp__claude-in-chrome__computer` action `screenshot`, `save_to_disk: true`. The result gives the path. Requires the extension to have permission on the site; `localhost` and `127.0.0.1` must be allowed explicitly.
3. **User's machine** — `device_bash` to capture, `device_stage_files` to bring it back. Requires a connected folder.
4. **Computer use** — `computer_screenshot` is for **seeing and orienting**, but returns an image in context, not a file: not annotatable. Use it to read the real state, then reconstruct (point 5).
5. **Faithful reconstruction** — redraw the observed panel in PIL/SVG. Always write "reconstructed schematic" on the image. Never pass a reconstruction off as a capture.

### Capture pitfalls

- **Multiple monitors**: capture targets one monitor. Identify the right one from the monitor list, then switch to it.
- **Masked windows**: terminals, command prompts and system windows are often masked out of captures. If a console is needed, ask the user to paste the text.
- **Read-only browsers**: under computer use, a browser is granted at tier "read" — visible, not clickable. To click, go through the browser extension.
- **Variable width**: ask for a stable window width (1440 px recommended) so every capture in one tutorial lines up.

---

## Step 2 — Redact first

**Mandatory, before annotation.** A real interface capture almost always contains data that must be hidden.

Always blur:

1. Email addresses, phone numbers, names of real people
2. API keys, tokens, session identifiers, signed URLs
3. Client names, company names, amounts, invoice numbers
4. Browser tab bar and bookmarks — they expose the rest of the user's activity
5. Notifications, message previews, content of other windows

Blur rather than cover with a solid rectangle: keep the shape so the reader still understands a field is there.

```python
from PIL import ImageFilter
zone = img.crop((x, y, x+w, y+h)).filter(ImageFilter.GaussianBlur(12))
img.paste(zone, (x, y))
```

Prefer a **demo dataset** over redaction when possible: cleaner, and reusable across tutorials.

If in doubt about a region: ask before publishing.

---

## Step 3 — Annotate

Crop to the useful area. A full 4K capture makes markers unreadable.

Conventions:

- **Numbered marker** = filled circle, white digit, white outline. The number matches the written step number. Never out of sync.
- **Arrow** toward the target, never on top of it: the target stays readable.
- **Frame** around the target area, 4 to 5 px.
- **Zoom** on any target under 40 px: magnified inset beside it.
- **Color code**: red = do now, green = afterwards, orange = warning. Never let color alone carry meaning — the number carries it.
- **Five markers maximum per image.** Beyond that, split.
- **Before / after** side by side when the result is visual.

### RTL languages (Arabic, Hebrew)

The interface is mirrored: markers go to the **left** of the target, arrows point right, marker reading order runs right to left. Verify on the produced image, not from memory.

### Reusable skeleton

```python
from PIL import Image, ImageDraw, ImageFont
import math
FD = "/usr/share/fonts/truetype/dejavu/"
def F(n, b=False):
    return ImageFont.truetype(FD + ("DejaVuSans-Bold.ttf" if b else "DejaVuSans.ttf"), n)

img = Image.open("capture.png").convert("RGB")
d = ImageDraw.Draw(img)

def frame(x, y, w, h, c="#ff3b30"):
    d.rounded_rectangle([x, y, x+w, y+h], radius=8, outline=c, width=5)

def arrow(x1, y1, x2, y2, c="#ff3b30", w=5):
    d.line([x1, y1, x2, y2], fill=c, width=w)
    a = math.atan2(y2-y1, x2-x1); L, s = 20, 0.5
    d.polygon([(x2, y2),
               (x2-L*math.cos(a-s), y2-L*math.sin(a-s)),
               (x2-L*math.cos(a+s), y2-L*math.sin(a+s))], fill=c)

def marker(cx, cy, n, c="#ff3b30", r=26):
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=c, outline="#ffffff", width=4)
    t = str(n); bb = d.textbbox((0, 0), t, font=F(30, True))
    d.text((cx-(bb[2]-bb[0])/2, cy-(bb[3]-bb[1])/2-5), t, font=F(30, True), fill="#ffffff")

img.save("step-01.png")
```

Naming: `<product>-<flow>-<NN>-<slug>.png`, two-digit number so alphabetical sort follows step order.

---

## Step 4 — Write

One step = one gesture. Format:

```
1. [Gesture] on [exact label as written on screen]
   → [what should appear next]
```

Rules:

- The first line of the response is the gesture to perform now, not context.
- Quote labels **exactly** as displayed, in the interface's language, even when the tutorial is written in another language.
- Give a **verification signal** after each step: what the user should see to know it worked.
- Time estimates in concrete units ("25 min at 100 Mbps"), never "a while".
- File paths and commands in code blocks, copyable as-is.
- No preamble, no recap, no closing pleasantry.
- Delete any sentence that adds no information to the image.
- **Alt text** per image: what the image shows, not "screenshot".

### When it breaks

For each risky step, anticipate the likely failure:

```
If [exact error message]: [cause in one sentence]. Fix: [gesture].
```

Cause and fix, neutral tone. No "oops", no drama.

---

## Step 5 — Final check

Before sending, **re-read the produced image** and verify:

1. Every marker lands on its target, not beside it
2. The image numbers match the text numbers
3. No sensitive data visible (re-read the step 2 list)
4. Text stays legible at half size
5. Nothing in the text describes what the image already shows

A misplaced marker is worse than no marker.

---

## Step 6 — Deliver

| Mode | Format |
|---|---|
| LIVE | image via `SendUserFile` `display: "render"`, one-line caption + short steps in the message |
| DOC | structured document, images inline in order, table of contents beyond 6 steps |
| TROUBLESHOOT | short message: cause, fix, verification |
| SCRIPT | numbered shots, duration per shot, spoken text separate from on-screen text |

End with **one** concrete action doable in under two minutes.

---

## Reusable library

One folder per product. The fifth tutorial should cost a fraction of the first.

```
<product>/
  captures/      raw images
  annotated/     final images
  glossary.md    exact labels, per language
  style.md       colors, fonts, window width, demo dataset
  flows/         one file per tutorial
```

Before starting from scratch: check whether the flow already exists and only needs updating.

## Maintenance

Date each tutorial and record the documented app version.

Recapture when: the version changes, a label moves in i18n, a user reports the screen no longer matches.

Never edit a tutorial's text without recapturing the screen concerned — that is how a tutorial becomes wrong while looking current.

---

## Live assistance (LIVE mode)

1. **Recapture before each instruction** — the user may have moved on or switched tabs.
2. **Restate where they are** ("step 2 of 4"): they do not hold state between messages.
3. **One instruction at a time.**
4. **Confirm what already works** before moving on.
5. **Stuck three exchanges in a row on the same point**: stop offering variants. Name the assumption that might be wrong, ask for a capture of the real state.

If an action is destructive (deletion, overwrite, migration, payment): confirm first, even at the cost of a round trip.
