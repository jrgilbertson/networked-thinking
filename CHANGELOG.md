# Changelog

All notable changes to this vault are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [1.2.1] - 2026-08-12

### Fixed

- Atomic note filenames that made every released ZIP unopenable on Windows.
  Windows File Explorer rejects an entire archive when any entry reaches 260
  bytes, and GitHub prepends `networked-thinking-<version>/` to every path, so
  one 238-byte note pushed the archive to 263 bytes. Both the Releases ZIP and
  the repository's "Download ZIP" button failed, in v1.0.0, v1.1.0, and v1.2.0.
  Eight Definitions were split into two sentences, keeping the meaning and the
  filename-matches-Definition convention, which brought the longest vault path
  from 238 bytes to 169.
- Extraction and `git clone` on Windows, which previously skipped notes whose
  extracted path exceeded the 260-character limit and left the vault with broken
  wikilinks.
- A stale example wikilink in `GETTING-STARTED.md` that pointed at a truncated
  DAE framework filename which no longer existed.

### Added

- `.github/workflows/path-length.yml`, failing any change that pushes a vault
  path past 171 UTF-8 bytes.
- A path-budget rule in `AGENTS.md` and `Templates/Atomic Note Template.md`,
  with guidance to split an over-long Definition rather than cut words.
- Windows extraction guidance in the README quickstart.

### Changed

- Updated the README banner to the shared Networked Thinking visual system and
  current tagline, removing proof marks and the border so the title and
  knowledge graph remain prominent.

### Removed

- The `docs/` tree, holding a banner ratio study and a design-pattern writeup.
  Someone who downloads this vault opens it in Obsidian, where agent working
  folders are just clutter. `AGENTS.md` now rules them out and `.gitignore`
  keeps them from returning; the same folders stay in the skills and site
  repositories, which are not vaults.
- `Attachments/jason-knowledge-graph.png` and `Attachments/fonts/`, which only
  the removed `docs/` files referenced. The graph image is the source for the
  superseded 3:1 banner and is still tracked by the companion site repository;
  the fonts existed to make the ratio study self-contained. Together they cut
  about 340 KB from every download.

## [1.2.0] - 2026-07-09

### Added

- `CHANGELOG.md`, documenting the vault's release history.
- `AGENTS.md` as the canonical agent instruction file, with `CLAUDE.md` reduced to an import shim.
- Dependabot configuration to keep GitHub Actions current.
- `Bases/DailyNote.base`, a genericized Base for embedding daily-note views.
- Company, Content, and Writing Draft templates.
- Optional `Reference:` sections in the atomic-note templates and example notes, for linking related atomic notes.
- `.compound-engineering/config.local.example.yaml` as an example project configuration.

### Changed

- Rebuilt the README around the book launch, and reconciled it and `GETTING-STARTED.md` to the current fourteen-template set and Bases.
- Ported the genericized template set: Daily Note, Decision, Meeting, Person, Quarterly Review, Reference Note, Structure Note, Vocabulary, Weekly Review, and General Note.
- Daily-note Base views now key off the `date_created` property rather than `file.ctime`, so views survive file moves and re-syncs.
- Migrated the Claude GitHub workflows from `@beta` to `@v1`, limited automated review to pull-request open, and simplified its comment mode.
- Reconciled the example notes to the new templates and updated their AI provenance to the current model.
- Made Anki explicitly optional in the Vocabulary and atomic-note templates.

### Removed

- The `Prompts/` folder and its atomic-note generator, superseded by the dual-track AI tooling described in the README.
- The separate `Atomic Note Template (Anki)` and `Atomic Note Template (Default)` files, consolidated into a single `Atomic Note Template` with an optional Anki block.
- `.obsidian/workspace.json` from version control. It holds per-machine UI state that churned on every open, and is now ignored.

### Fixed

- Title placeholder in the Structure Note template.
- Ebbinghaus forgetting-curve figures in the spaced-repetition notes.
- An orphaned note on atomicity, now linked from its structure hub.
- Stale references to the removed `Prompts/` folder in `AGENTS.md` and `GETTING-STARTED.md`.

## [1.1.0] - 2025-11-18

### Changed

- Updated documentation for accuracy and expanded vault content.
- Documented the GitHub template and Releases paths for obtaining the vault.
- Adjusted graph view scaling and refreshed Obsidian workspace layouts, navigation state, and file references.
- Configured the Obsidian editor to indent with spaces.

## [1.0.0] - 2025-11-14

### Added

- Folder structure for the knowledge system: Atomic Notes, Structure Notes, Reference Notes, Templates, Inbox, Projects, Meetings, People, Reviews, Places and Things, and Attachments.
- Example atomic notes, structure notes, and templates for the companion vault.
- An interactive `GETTING-STARTED.md` guide.
- Claude Code GitHub Actions workflows for pull-request assistance and code review.
- An atomic-note generator prompt under `Prompts/`.
- A mailing-list signup link in the README.

### Changed

- Rebranded the project from "Curate, Connect, Cultivate" to "Networked Thinking".
- Replaced the MIT License with Creative Commons Attribution 4.0.
- Replaced wiki-style links with plain text so notes render correctly on GitHub.
- Removed unnecessary YAML metadata from the README.
- Updated vault documentation, templates, and structure for the book launch.

[Unreleased]: https://github.com/jrgilbertson/networked-thinking/compare/v1.2.1...HEAD
[1.2.1]: https://github.com/jrgilbertson/networked-thinking/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/jrgilbertson/networked-thinking/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/jrgilbertson/networked-thinking/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/jrgilbertson/networked-thinking/releases/tag/v1.0.0
