# Contributing

## Source of truth

`skills/show-me-dont-tell-me/SKILL.md` is canonical. Change behaviour there first, then update the README tables and `CHANGELOG.md` if the change is user-visible. Bump `version` in `.claude-plugin/plugin.json`.

## What belongs in this skill

Anything that makes the output **more accurate or safer**:

- A capture path that works where the existing ones fail
- A redaction case that is easy to miss
- An annotation convention that survives being resized
- A platform gotcha that cost you an hour

## What does not

Features that add surface without adding accuracy: animated GIFs, automatic light/dark variants, multi-format export pipelines. A skill that tries to do everything stops being applied.

If you are unsure, open an issue describing the tutorial that came out wrong, and what the skill should have done instead.

## Testing a change

There is no unit test for prose. Test by using it:

1. Pick a real interface you did not write
2. Run `/show-me-dont-tell-me document <a flow>` before and after your change
3. Give both to someone who has never seen that interface
4. Count where they hesitate

A change that does not reduce hesitation is not an improvement.

## Style

- Write in the imperative. "Redact before annotating", not "it is advised to redact".
- Keep tables over prose when the content is a lookup.
- No emoji in the skill body.
- Cite exact tool names and exact error strings — they are what makes the skill actionable.

## Translations

The skill body is French. Translations are welcome as `skills/show-me-dont-tell-me/SKILL.<lang>.md`. Keep section order identical so diffs stay readable across languages.

## Contact

Maintainer: Dr Maher — mykhalijai@gmail.com

## License

Contributions are accepted under the MIT License.
