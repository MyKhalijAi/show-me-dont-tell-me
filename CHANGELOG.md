# Changelog

All notable changes to this project are documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/).

Maintained by Dr Maher — MyKhalijAi.

## [2.0.0] — 2026-09-22

### Added
- **Request triage** — four modes (DIRECT, DOC, TROUBLESHOOT, SCRIPT) selected before any work. The mode decides screenshot density, structure and output format.
- **Audience model** — end customer, internal team, or your future self. Changes vocabulary and how much "why" is included.
- **Source-of-truth pass for your own apps** — read i18n files, templates, routes and validators before capturing, to get exact labels and cover states the happy path never reaches.
- **Mandatory redaction step** — blur list covering emails, API keys, client names, browser tab bar and notifications, with a Pillow snippet. Runs before annotation, never after.
- **RTL handling** — marker placement and arrow direction mirrored for Arabic and Hebrew interfaces.
- **Final check** — five-point review of the produced image before sending.
- **Reusable library layout** — per-product folder with captures, glossary, style and flows.
- **Maintenance rules** — date each tutorial, record the documented app version, recapture on i18n change.
- **Alt text requirement** per image.
- **Destructive-action confirmation** in live assistance mode.
- `scripts/annotate.py` — Pillow helper implementing the conventions, with `point_at`, `zoom_inset`, `blur`, `set_rtl` and `crop_around`.

### Changed
- Capture sources reordered by reliability, with the file-versus-context distinction made explicit.
- Delivery format now depends on mode rather than being a single default.

## [1.0.0] — 2026-09-22

### Added
- Initial release: capture, annotate, write, deliver.
- Numbered markers matching step numbers, arrows, frames, zoom for small targets.
- Verification signal after each step.
- Failure-mode template: exact error, cause, fix.
- Live-assistance rules: recapture before each instruction, restate progress, one instruction at a time.
