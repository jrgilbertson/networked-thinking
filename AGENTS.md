# AGENTS.md

This is the canonical project instruction file. Codex reads `AGENTS.md` natively; Claude Code reads these same instructions through the `CLAUDE.md` import shim.

## Project Context

This repository is an Obsidian vault template for the Networked Thinking methodology. Markdown notes, templates, Obsidian configuration, and documentation are the product. Treat content quality, link integrity, and vault portability as the main correctness concerns.

Start with `README.md` and `GETTING-STARTED.md` when you need product context. Use the existing notes and files under `Templates/` as the source of truth for local note structure.

`docs/solutions/` contains durable project learnings, organized by category with searchable YAML frontmatter.

## Editing Rules

- Keep `AGENTS.md` as the single canonical source of project instructions. Do not duplicate these instructions in `CLAUDE.md`; it should remain only the import shim.
- Preserve Obsidian-compatible Markdown, wikilinks (`[[Note]]`, `[[Note|Display]]`), aliases, frontmatter, and folder names with spaces.
- Prefer small, targeted edits. Do not reformat whole notes, rewrite unrelated prose, or normalize whitespace across files unless asked.
- Keep the `README.md` badges as links, not bare images. The license badge links to `LICENSE.md` and the release badge links to the Releases page; both are wrapped as `[![Alt](image-url)](target-url)`. It is easy to drop the outer `[...](target)` when hand-editing the intro. If a README edit changes any line other than the one you were asked to change, restore it before committing.
- Do not edit vendored Obsidian plugin bundles under `.obsidian/plugins/` unless the task is explicitly about plugin files.
- When adding media or non-markdown assets, place them under `Attachments/` unless the user gives a more specific location.
- Write new files in ASCII. Non-ASCII belongs only where the content requires it, such as IPA in vocabulary notes or a name spelled with diacritics. Use a comma, a colon, a period, or a reworked sentence rather than an em dash.

## Vault Conventions

- Atomic notes live in `Atomic Notes/` and capture one self-contained idea. The filename is the timestamp plus the Definition's first sentence without its final period: `YYYYMMDDHHMM The Definition's first sentence.md`.
- Atomic notes should follow the DAE pattern used by the templates and examples: Definition, Analogy, and Example.
- Keep every vault path at or under 171 UTF-8 bytes so the release ZIP opens on Windows. `.github/scripts/check_path_length.py` enforces the budget and documents how it is derived; change the note, not the budget. When a Definition's first sentence would breach it, split the Definition into two sentences so the filename still matches that first sentence.
- Renaming an atomic note breaks every wikilink that targets it, including piped `[[Long file name|Short label]]` links in structure notes. After a rename, `rg` the old filename and update every hit before committing.
- Every atomic note should be discoverable from at least one structure note. When adding or materially changing an atomic note, update the relevant file under `Structure Notes/` or create a structure-note link if needed.
- Structure notes are navigation hubs and curated topic maps. Keep them link-rich and organized around relationships, not folder hierarchy.
- Reference notes preserve source context before ideas are synthesized into atomic notes.
- Inbox content is raw capture. Move or transform it only when the task explicitly asks for curation.
- People, Meetings, Projects, Reviews, Places and Things, and Vocabulary Notes are workflow folders. Follow the closest matching template when creating new files there.

## Verification

There is no application build or test suite for normal content edits. If lefthook is already installed, `lefthook install` once makes `lefthook.yml` run the path-length and whitespace checks on every commit; CI repeats the path-length check only. Do not install lefthook to satisfy this file. Run the checks below directly instead. Verify by:

- Running `python3 .github/scripts/check_path_length.py` when adding or renaming notes. It covers new files before they are staged.
- Running targeted `rg` searches for changed terminology, links, or old conventions, including the old filename after any rename.
- Checking `git diff --check` for whitespace errors.
- Reviewing changed Markdown for broken wikilinks, malformed frontmatter, and accidental duplication.

For GitHub workflow changes, inspect the affected YAML carefully and run a YAML linter if one is available locally.
