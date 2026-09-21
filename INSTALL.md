# Install

`show-me-dont-tell-me` is a single skill. Three ways to get it.

---

## 1. Claude (web / desktop app)

Ask Claude to add it, pasting the contents of [`skills/show-me-dont-tell-me/SKILL.md`](skills/show-me-dont-tell-me/SKILL.md):

> Add this as a skill named `show-me-dont-tell-me`: <paste the file>

Claude shows a review card. Save it. Invoke with `/show-me-dont-tell-me`.

## 2. Claude Code — plugin marketplace

```bash
claude plugin marketplace add MyKhalijAi/show-me-dont-tell-me
claude plugin install show-me-dont-tell-me
```

Verify:

```bash
claude plugin list
```

## 3. Claude Code — manual

```bash
git clone https://github.com/MyKhalijAi/show-me-dont-tell-me.git
mkdir -p ~/.claude/skills
cp -r show-me-dont-tell-me/skills/show-me-dont-tell-me ~/.claude/skills/
```

Restart Claude Code. The skill appears as `show-me-dont-tell-me`.

---

## Annotation helper (optional)

Only needed if you run the Pillow helper yourself. Claude installs what it needs on its own.

```bash
pip install pillow
```

```python
import sys; sys.path.insert(0, "scripts")
from annotate import Annot
```

Fonts: the helper looks for DejaVu Sans (Linux), then Segoe UI (Windows), then falls back to Pillow's default. Install `fonts-dejavu-core` on Linux for best results.

---

## Prerequisites for screenshots

The skill needs a way to see a screen. At least one of:

| Source | Requires |
|---|---|
| You paste a screenshot | nothing |
| Browser page | Claude in Chrome extension, with the site allowed — including `localhost` and `127.0.0.1`, which are **not** allowed by default |
| Your machine's files | a connected folder |
| Your screen | Computer use enabled in the Claude desktop app |

If none is available the skill says so and asks for a screenshot. It does not guess where a button is.

### Known limitations

- **Browsers under computer use are read-only.** Visible in screenshots, not clickable. Clicking requires the browser extension.
- **Terminals are masked** out of computer-use screenshots. Paste console text instead.
- **Multi-monitor setups** capture one monitor at a time.
- A screenshot that arrives only in the conversation cannot be annotated — the skill needs a file on disk.

---

## Uninstall

```bash
claude plugin uninstall show-me-dont-tell-me
```

Or delete `~/.claude/skills/show-me-dont-tell-me/`. For the Claude app, remove the skill from your skills settings.
