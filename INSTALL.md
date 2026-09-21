# Install

`show-me-dont-tell-me` is a single skill. Pick the route that matches where you use Claude.

| You use | Go to |
|---|---|
| Claude Desktop (Mac / Windows) | [§1](#1-claude-desktop) |
| claude.ai in a browser | [§2](#2-claudeai-in-a-browser) |
| Claude Code (CLI, IDE, or inside the desktop app) | [§3](#3-claude-code--plugin-marketplace) |

---

## 1. Claude Desktop

### a. Upload the skill — recommended

Package the skill folder as a `.zip` first.

macOS / Linux:

```bash
git clone https://github.com/MyKhalijAi/show-me-dont-tell-me.git
cd show-me-dont-tell-me/skills
zip -r show-me-dont-tell-me.zip show-me-dont-tell-me
```

Windows (PowerShell):

```powershell
git clone https://github.com/MyKhalijAi/show-me-dont-tell-me.git
Set-Location show-me-dont-tell-me\skills
Compress-Archive -Path show-me-dont-tell-me -DestinationPath show-me-dont-tell-me.zip
```

Then, in Claude Desktop:

1. Open **Settings → Capabilities → Skills**
2. **Upload skill**, and pick `show-me-dont-tell-me.zip`
3. Turn the skill **on** once it appears in the list

The zip must contain the **folder**, with `SKILL.md` at its root — not the `.md` file on its own. That is the most common reason an upload is rejected.

Skills require a paid plan. On Team and Enterprise, an administrator has to enable Skills for the workspace before the section appears.

### b. Paste it instead — no zip

Open the raw [`SKILL.md`](skills/show-me-dont-tell-me/SKILL.md), copy everything, and tell Claude:

> Add this as a skill named `show-me-dont-tell-me`: &lt;paste the file&gt;

Claude shows a review card. Save it.

### c. Through Claude Code inside the desktop app

Claude Code also runs inside Claude Desktop. If that is how you work, use the marketplace commands in [§3](#3-claude-code--plugin-marketplace) — they apply unchanged.

### Then

Invoke it with `/show-me-dont-tell-me`, or just describe what you need — the skill triggers on its own when a request involves documenting, guiding through, or troubleshooting an interface.

For the skill to see a live screen rather than a pasted image, enable **computer use** in the desktop app, or install the Claude in Chrome extension for browser pages. See [Prerequisites for screenshots](#prerequisites-for-screenshots) below.

## 2. claude.ai in a browser

Same two routes as the desktop app: **Settings → Capabilities → Skills → Upload skill** with the zip built above, or paste the contents of [`SKILL.md`](skills/show-me-dont-tell-me/SKILL.md) into a conversation and ask Claude to save it as a skill.

## 3. Claude Code — plugin marketplace

```bash
claude plugin marketplace add MyKhalijAi/show-me-dont-tell-me
claude plugin install show-me-dont-tell-me
```

Verify:

```bash
claude plugin list
```

## 4. Claude Code — manual

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

**Claude Desktop and claude.ai** — **Settings → Capabilities → Skills**, then switch `show-me-dont-tell-me` off to keep it for later, or delete it to remove it outright.

**Claude Code, installed as a plugin:**

```bash
claude plugin uninstall show-me-dont-tell-me
```

**Claude Code, installed manually** — delete `~/.claude/skills/show-me-dont-tell-me/`.
