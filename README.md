# Networked Thinking

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE.md)
[![Latest release](https://img.shields.io/github/v/release/jrgilbertson/networked-thinking)](https://github.com/jrgilbertson/networked-thinking/releases)

![Networked Thinking Companion Vault banner showing a connected knowledge graph with the tagline The missing manual for knowledge work in the AI age](Attachments/networked-thinking-readme-banner.webp)

Networked Thinking is a book and practical system for turning saved articles, highlights, and notes into a living knowledge system for writing, decisions, and work.

## Purpose

I built the original setup in 2022 after realizing I confused saving information with learning from it. AI has made that mistake easier to make. The system protects the useful friction of writing down what I know, what connects, and what I still need to figure out. Then when I bring in AI, I'm asking it to work with my thinking instead of replacing it.

This vault is the companion to [Networked Thinking](https://networkedthinking.ai/), the forthcoming book by Jason Gilbertson and Terri Yeh. Every note type, template, and folder the book describes is built out and linked here, so you can see the system running instead of reading about it in the abstract.

## Quickstart

Install [Obsidian](https://obsidian.md/), the free local-first app this vault is built for. Then either click "Use this template" on this repository to create your own version-controlled copy, or download the latest release ZIP from the [Releases page](https://github.com/jrgilbertson/networked-thinking/releases) for a plain folder. Open that folder as a vault in Obsidian (File > Open Vault), then read [GETTING-STARTED.md](GETTING-STARTED.md) for the full folder map, template inventory, and linking mechanics.

On Windows, extract the ZIP somewhere short such as `C:\vault` rather than the Desktop. Windows cannot create a file whose full path exceeds 260 characters, and Explorer skips the ones that do.

## Structure

Content is organized by workflow state, with links and structure notes carrying the topic organization instead of folders. The essential folders:

```text
Atomic Notes/     Single-concept notes, one idea each (YYYYMMDDHHMM filenames)
Structure Notes/  Topic maps that link related atomic notes together
Reference Notes/  Notes on external sources, kept before they're synthesized
Templates/        Starting points for every note type
Inbox/            Raw capture, sorted during weekly review
Reviews/          Daily, weekly, and quarterly reflection notes
```

People, Meetings, Projects, Vocabulary Notes, and Places and Things are optional workflow folders, added only when a real need shows up. `Attachments/` holds media and `Bases/` holds the saved view definitions that templates embed. [GETTING-STARTED.md](GETTING-STARTED.md) has the complete folder map, the full template inventory, and the wikilink and alias mechanics.

For agentic assistants working directly in the vault, the companion [Networked Thinking Skills](https://github.com/jrgilbertson/networked-thinking-skills) project adds `atomic-note` and `atomic-note-audit` skills (`npx skills add`). The book's paste-into-any-chat-AI prompt lives in Appendix D.

## Status

This is active, pre-launch material for the book, due in 2026. It already holds fourteen atomic notes, three structure notes, fourteen templates, and one fully processed reference note, all real content to open and read rather than stub files. Five daily notes show the shape of the routine, one worked through and four left blank to write into. See [CHANGELOG.md](CHANGELOG.md) for what has changed between tagged releases. Additional vocabulary entries and cross-domain linking examples are still being added.

Learn more and join the waitlist at [networkedthinking.ai](https://networkedthinking.ai/). For beta reading or early-access questions, email [jason.gilbertson@gmail.com](mailto:jason.gilbertson@gmail.com) or [yeh.terri@gmail.com](mailto:yeh.terri@gmail.com).

## License

CC BY 4.0. See [LICENSE](LICENSE.md).
