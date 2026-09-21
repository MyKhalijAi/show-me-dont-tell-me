<div align="center">

# show-me-dont-tell-me

**Claude describes the button. This makes it point at the button.**

A Claude skill that answers with annotated screenshots — numbered markers, arrows, zoom — instead of paragraphs describing an interface.

[Install](INSTALL.md) · [Français](README.fr.md) · [Changelog](CHANGELOG.md) · MIT

</div>

![Before and after: a wall of prose describing a button, versus an annotated screenshot with a red marker pointing at it](assets/hero.png)

---

## Install

```bash
claude plugin marketplace add MyKhalijAi/show-me-dont-tell-me
claude plugin install show-me-dont-tell-me
```

Then:

```
/show-me-dont-tell-me document the signup flow of my app
/show-me-dont-tell-me I'm stuck on this screen
/show-me-dont-tell-me why does this throw a 403
```

Other platforms and manual install: [INSTALL.md](INSTALL.md).

---

## What changes

| Without | With |
|---|---|
| "Navigate to the settings panel and locate the download option" | An image with a red ① on the exact button |
| Invented labels from an older version | Labels read from your screen or your i18n files |
| Only the happy path | Empty states, validation errors, permission denied |
| Screenshots shipped with live customer data | Redaction is a mandatory step |
| "This will take a while" | "About 25 min at 100 Mbps" |

## Four modes

The skill triages before doing anything. The mode decides screenshot density, structure and output.

| Mode | Triggered by | Output |
|---|---|---|
| **LIVE** | "help me with", "I'm stuck" | short message + one image per step |
| **DOC** | "document this", "tutorial for my app" | structured document, images inline |
| **TROUBLESHOOT** | a specific error, "it's not working" | cause → fix → verification |
| **SCRIPT** | "video", "screencast", "training" | numbered shots, timing per shot |

## Five rules it never breaks

1. **Never describe a UI from memory.** Real capture or source code first.
2. **Redact before annotating.** Emails, API keys, client names, the browser tab bar.
3. **One marker number = one step number.** Never out of sync.
4. **Every step ends with a verification signal** — what you should see to know it worked.
5. **Max 5 markers per image.** Beyond that, split.

## When it's your own app

Pointed at a codebase, it reads the source before capturing:

- **i18n files, templates, constants** → exact labels, right language
- **Routes, controllers, validators** → screens you would not have thought to show
- **Error paths** → empty list, invalid field, loading, permission denied, quota reached

A tutorial that skips the validation error is the one that generates the support ticket.

## Annotation helper

`scripts/annotate.py` — a small Pillow wrapper implementing the conventions:

```python
from annotate import Annot

(Annot("capture.png")
    .blur(120, 300, 420, 28)        # redact first
    .frame(980, 550, 460, 50)
    .point_at(980, 575, 1)          # marker + arrow, RTL-aware
    .crop_around(1100, 500, 1000, 600)
    .save("step-01-download.png"))
```

`set_rtl(True)` mirrors marker placement and arrow direction for Arabic and Hebrew.

## Accessibility

Meaning is never carried by color alone — the number carries it. Alt text is required per image. Text must stay legible at half size. RTL layouts are handled explicitly.

## Languages

`SKILL.md` is English. A French translation lives at [`SKILL.fr.md`](skills/show-me-dont-tell-me/SKILL.fr.md). The skill answers in whatever language you write in.

## About

Built and maintained by **Dr Maher** at **MyKhalijAi** — Claude tooling and training, in Arabic, French, English and Spanish.

Contact: [mykhalijai@gmail.com](mailto:mykhalijai@gmail.com) · [github.com/MyKhalijAi](https://github.com/MyKhalijAi)

## License

MIT — see [LICENSE](LICENSE).
