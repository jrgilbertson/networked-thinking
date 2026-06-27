# AGENTS.md

This is the canonical project instruction file. Codex reads `AGENTS.md` natively; Claude Code reads these same instructions through the `CLAUDE.md` import shim.

## Project Context

This repository is an Obsidian vault template for the Networked Thinking methodology. Markdown notes, templates, Obsidian configuration, and documentation are the product. Treat content quality, link integrity, and vault portability as the main correctness concerns.

Start with `README.md` and `GETTING-STARTED.md` when you need product context. Use the existing notes and files under `Templates/` as the source of truth for local note structure.

## Editing Rules

- Keep `AGENTS.md` as the single canonical source of project instructions. Do not duplicate these instructions in `CLAUDE.md`; it should remain only the import shim.
- Preserve Obsidian-compatible Markdown, wikilinks (`[[Note]]`, `[[Note|Display]]`), aliases, frontmatter, and folder names with spaces.
- Prefer small, targeted edits. Do not reformat whole notes, rewrite unrelated prose, or normalize whitespace across files unless asked.
- Do not edit vendored Obsidian plugin bundles under `.obsidian/plugins/` unless the task is explicitly about plugin files.
- When adding media or non-markdown assets, place them under `Attachments/` unless the user gives a more specific location.
- Use ASCII for new project files unless a note already uses non-ASCII characters for its content.

## Vault Conventions

- Atomic notes live in `Atomic Notes/`, use `YYYYMMDDHHMM Full sentence describing core insight.md`, and should capture one self-contained idea.
- Atomic notes should follow the DAE pattern used by the templates and examples: Definition, Analogy, and Example.
- Every atomic note should be discoverable from at least one structure note. When adding or materially changing an atomic note, update the relevant file under `Structure Notes/` or create a structure-note link if needed.
- Structure notes are navigation hubs and curated topic maps. Keep them link-rich and organized around relationships, not folder hierarchy.
- Reference notes preserve source context before ideas are synthesized into atomic notes.
- Inbox content is raw capture. Move or transform it only when the task explicitly asks for curation.
- People, Meetings, Projects, Reviews, Places and Things, Vocabulary Notes, and Prompts are workflow folders. Follow the closest matching template when creating new files there.

## Verification

There is no application build or test suite for normal content edits. Verify by:

- Running targeted `rg` searches for changed terminology, links, or old conventions.
- Checking `git diff --check` for whitespace errors.
- Reviewing changed Markdown for broken wikilinks, malformed frontmatter, and accidental duplication.

For GitHub workflow changes, inspect the affected YAML carefully and run a YAML linter if one is available locally.
