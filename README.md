<div align="center">

# show-me-dont-tell-me

### Every assistant *describes* your screen. This one **points at it**.

A Claude skill that answers with annotated screenshots — numbered markers, arrows, zoom — instead of three paragraphs guessing where a button might be.

[![License MIT](https://img.shields.io/badge/license-MIT-000000)](LICENSE)
[![Claude skill](https://img.shields.io/badge/Claude-skill-d97757)](INSTALL.md)
[![Version 2.0.0](https://img.shields.io/badge/version-2.0.0-2563eb)](CHANGELOG.md)

**English** · [Français](README.fr.md) · [العربية](README.ar.md) · [Español](README.es.md) · [简体中文](README.zh.md)

</div>

![Before and after: a wall of prose describing a button, versus an annotated screenshot with a red numbered marker pointing straight at it](assets/hero.png)

---

## The minute you lose, every single time

You ask where a setting is. You get this:

> *"Navigate to the settings panel, locate the Advanced section, and look for the download option near the bottom."*

Three sentences. Zero pixels. You still have to go hunting — and if that answer came from a memory of an older release, the option may not even carry that name any more.

**show-me-dont-tell-me** answers the same question with a picture of **your** screen and a red ① sitting on the exact button.

One step = one annotated image + one line of action. The text never repeats what the image already shows.

---

## Install in 30 seconds

```bash
claude plugin marketplace add MyKhalijAi/show-me-dont-tell-me
claude plugin install show-me-dont-tell-me
```

Then just ask:

```
/show-me-dont-tell-me document the signup flow of my app
/show-me-dont-tell-me I'm stuck on this screen
/show-me-dont-tell-me why does this throw a 403
```

Other platforms, manual install, setup without the CLI → **[INSTALL.md](INSTALL.md)**

---

## What changes

| Without | With |
|---|---|
| "Navigate to the settings panel and locate the download option" | An image with a red ① on the exact button |
| Invented labels from an older version | Labels read from your screen or your i18n files |
| Only the happy path | Empty states, validation errors, permission denied |
| Screenshots shipped with live customer data | Redaction is a mandatory step, not an afterthought |
| "This will take a while" | "About 25 min at 100 Mbps" |
| A wall of prose you have to decode | One image, one gesture, one thing to check |

---

## What people actually do with it

**📘 Ship the user guide you keep postponing.** Point it at your repository. It reads your routes, templates and i18n files, then produces a tutorial covering the screens you would have forgotten — error states included.

**🧑‍💻 Onboard someone without booking a call.** "Document how we deploy" becomes a numbered, illustrated document, with a verification signal after every step.

**🎫 Turn one support ticket into a permanent answer.** Troubleshoot mode gives cause → fix → verification, with the error captured and the fix captured. Paste it into your help centre and never answer it twice.

**🧭 Get unstuck in an interface you have never seen.** Live mode recaptures your screen before every instruction, so it never walks you through a panel you already left.

**🎬 Storyboard a screencast before you hit record.** Numbered shots, a duration for each, spoken text kept separate from on-screen text.

---

## Four modes, triaged for you

It works out what you need before doing anything. The mode decides screenshot density, structure and output format.

| Mode | Triggered by | Output |
|---|---|---|
| **LIVE** | "help me with", "I'm stuck" | short message + one image per step |
| **DOC** | "document this", "tutorial for my app" | structured document, images inline |
| **TROUBLESHOOT** | a specific error, "it's not working" | cause → fix → verification |
| **SCRIPT** | "video", "screencast", "training" | numbered shots, timing per shot |

It also adapts the vocabulary to the audience — end customer, internal team, or your own future self.

---

## Five rules it never breaks

This is why you can paste the output straight into your documentation:

1. **Never describe a UI from memory.** Real capture or source code first. If nothing is obtainable, it says so and asks — it never guesses where a button is.
2. **Redact before annotating.** Emails, API keys, client names, the browser tab bar. Blurred rather than covered, so the reader still sees a field is there.
3. **One marker number = one step number.** Never out of sync.
4. **Every step ends with a verification signal** — what you should see to know it worked.
5. **Five markers maximum per image.** Beyond that, it splits.

Then it re-reads the image it just produced and checks all five, because a misplaced marker is worse than no marker.

---

## Point it at your own codebase — this is where it wins

Given access to your source, it reads before it captures:

- **i18n files, templates, constants** → exact labels, verbatim, in the right language
- **Routes, controllers, validators** → the screens you would never have thought to show
- **Error paths** → empty list, invalid field, loading, permission denied, quota reached, network failure
- **Prerequisites** → the role, data or setting needed before step 1, stated up front

> A tutorial that skips the validation error is the one that generates the support ticket.

---

## Built for real products, not demo screenshots

- **Right-to-left done properly.** In Arabic and Hebrew the markers move to the left of the target, arrows point right, reading order runs right to left — and it verifies that on the produced image, not from memory.
- **Accessible by construction.** Meaning is never carried by colour alone: the number carries it. Alt text is required on every image. Text must stay legible at half size.
- **Answers in your language.** Write in Spanish, get Spanish — while UI labels stay quoted exactly as they appear on screen.
- **Stays true over time.** Each tutorial is dated against an app version, and text is never edited without recapturing the screen concerned.

---

## The annotation helper

`scripts/annotate.py` — a small Pillow wrapper implementing the conventions. No framework, no build step:

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

---

## The fifth tutorial costs a fraction of the first

One folder per product, so the work compounds instead of restarting:

```
<product>/
  captures/      raw images
  annotated/     final images
  glossary.md    exact labels, per language
  style.md       colours, fonts, window width, demo dataset
  flows/         one file per tutorial
```

Before starting from scratch, it checks whether the flow already exists and only needs updating.

---

## Who it's for

Anyone who has to make an interface understandable to someone else:

- **Developers** documenting their own app without losing a day to it
- **Support and success teams** answering the same screen question every week
- **Technical writers** who need screenshots that stay accurate release after release
- **Trainers and educators** building illustrated courses, in any language
- **Anyone stuck** in a piece of software right now

---

## Contribute

The skill is a single readable Markdown file — [`SKILL.md`](skills/show-me-dont-tell-me/SKILL.md). No build, no dependencies, no magic. Improve a convention there and it shows up in everybody's tutorials.

⭐ **Star the repo** if it saves you a screenshot — it is how other people find it.

🐛 **Issues and pull requests are welcome**, in any of the five languages of this README. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## About

Built and maintained by **Dr Maher** at **MyKhalijAi** — Claude tooling and training, in Arabic, French, English and Spanish.

Contact: [mykhalijai@gmail.com](mailto:mykhalijai@gmail.com) · [github.com/MyKhalijAi](https://github.com/MyKhalijAi)

First of a series of skills that work from real interfaces rather than from memory.

## License

MIT — see [LICENSE](LICENSE). Use it commercially, fork it, ship it.
