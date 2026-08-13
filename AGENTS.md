# AGENTS.md

This is the canonical project instruction file. Codex reads `AGENTS.md` natively; Claude Code reads these same instructions through the `CLAUDE.md` import shim.

## Project Context

This repository is an Obsidian vault template for the Networked Thinking methodology. Markdown notes, templates, Obsidian configuration, and documentation are the product. Treat content quality, link integrity, and vault portability as the main correctness concerns.

Start with `README.md` and `GETTING-STARTED.md` when you need product context. Use the existing notes and files under `Templates/` as the source of truth for local note structure.

This repository ships as a clean Obsidian vault, so it keeps no `docs/` tree. Everything tracked here is content a downloader opens in Obsidian. `.gitignore` already keeps a stray `docs/` tree out of commits, so leave one a tool writes rather than deleting untracked work. The same goes for working documents at the root: durable learnings, ideation studies, plans, and product or design briefs live in `networked-thinking-skills` or `networked-thinking-site`, which are not vaults.

## Editing Rules

- Preserve Obsidian-compatible Markdown, wikilinks (`[[Note]]`, `[[Note|Display]]`), aliases, frontmatter, and folder names with spaces.
- Before any `obsidian` command that writes, run `obsidian vault info=path` and compare it with `git rev-parse --show-toplevel`. The CLI acts on a registered vault, which can be a different checkout of this repository on a different branch, so matching the vault's name is not enough. Identical paths: use the CLI. Anything else, including a git worktree Obsidian has not opened or a machine with no `obsidian` binary: use git for this checkout.
- With the paths matching, create, rename, move, and delete vault files with `obsidian create`, `obsidian rename`, `obsidian move`, and `obsidian delete`, which rewrite the wikilinks pointing at a renamed or moved note when the vault has Files and links -> Automatically update internal links enabled. Using git instead leaves every inbound link dangling behind a diff that looks clean, so `rg` the old filename, confirm zero hits, and update each one. To target a vault explicitly, put `vault=<name>` before the command; placed after it, it is ignored rather than refused.
- Prefer small, targeted edits. Do not reformat whole notes, rewrite unrelated prose, or normalize whitespace across files unless asked.
- Keep the `README.md` badges as links, not bare images. The license badge links to `LICENSE.md` and the release badge links to the Releases page; both are wrapped as `[![Alt](image-url)](target-url)`. It is easy to drop the outer `[...](target)` when hand-editing the intro. If a README edit changes any line other than the one you were asked to change, restore it before committing.
- Do not edit vendored Obsidian plugin bundles under `.obsidian/plugins/` unless the task is explicitly about plugin files.
- When adding media or non-markdown assets, place them under `Attachments/` unless the user gives a more specific location.
- Write in ASCII. Non-ASCII belongs only where the content requires it, such as IPA in vocabulary notes or a name spelled with diacritics. Use a comma, a colon, a period, or a reworked sentence rather than an em dash.
- Keep `AGENTS.md` as the single canonical source of project instructions. Do not duplicate these instructions in `CLAUDE.md`; it should remain only the import shim.

## Vault Conventions

- Atomic notes live in `Atomic Notes/` and capture one self-contained idea. The filename is the timestamp plus the Definition's first sentence without its final period: `YYYYMMDDHHMM The Definition's first sentence.md`. The `title:` property and the H1 carry the short concept name of two to five words instead, and `date_created` and `date_modified` use `YYYY-MM-DD HH:MM`.
- Atomic notes should follow the DAE pattern used by the templates and examples: Definition, Analogy, and Example.
- Keep every vault path at or under 171 UTF-8 bytes so the release ZIP opens on Windows. `.github/scripts/check_path_length.py` enforces the budget and documents how it is derived; change the note, not the budget. When a Definition's first sentence would breach it, split the Definition into two sentences so the filename still matches that first sentence.
- Renaming an atomic note breaks every wikilink that targets it, including piped `[[Long file name|Short label]]` links in structure notes. After a rename, `rg` the old filename and update every hit before committing.
- Every atomic note should be discoverable from at least one structure note. When adding or materially changing an atomic note, update the relevant file under `Structure Notes/` or create a structure-note link if needed.
- Structure notes are navigation hubs and curated topic maps. Keep them link-rich and organized around relationships, not folder hierarchy.
- Reference notes preserve source context before ideas are synthesized into atomic notes.
- Inbox content is raw capture. Move or transform it only when the task explicitly asks for curation.
- People, Meetings, Projects, Reviews, Places and Things, and Vocabulary Notes are workflow folders. Follow the closest matching template when creating new files there.
- `Bases/` holds the `.base` view definitions that templates and notes embed, such as `DailyNote.base` in the Daily Note Template. Change one only when the task is about Bases views; deleting it breaks every note that embeds it.

## Verification

There is no application build or test suite for normal content edits. Leave `lefthook install` to whoever owns the checkout; CI re-runs the path-length check on every pull request. Run all five of these directly before committing:

- Running `python3 .github/scripts/check_path_length.py` when adding or renaming notes. It covers new files before they are staged.
- Running targeted `rg` searches for changed terminology, links, or old conventions, including the old filename after any rename.
- Checking `git diff --check HEAD` for whitespace errors, which covers staged changes as well as unstaged.
- Running `rg -n '[^\x00-\x7F]'` over changed files, expecting hits only where the content requires them.
- Reviewing changed Markdown for broken wikilinks, malformed frontmatter, and accidental duplication.

For GitHub workflow changes, inspect the affected YAML carefully and run a YAML linter if one is available locally.
