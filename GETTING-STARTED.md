# Getting Started with the Companion Vault

The plugins, templates, and example notes are already set up, so you can write your first note without configuring anything.

## Four Design Principles

**Separate raw from processed.** Capture ideas to Inbox instantly without organizing. Process them during weekly review when you have mental space for evaluation.

**Favor flat over deep.** Links beat folder hierarchies for knowledge organization. Structure notes beat subfolders for navigation. A note about "decision fatigue" appears in Psychology, Productivity, and Leadership contexts through links, not by choosing a single folder.

**Blend time and topic.** Daily notes capture temporal reflection (what happened today). Structure notes create conceptual maps (productivity concepts organized by relationship).

**Build semantic connections through links and aliases.** Every link creates a meaningful relationship in your knowledge graph. Aliases extend discoverability, so "ROI," "return on investment," and "investment returns" all point to the same concept.

## Folder System

Your workspace is grouped by where a note sits in your workflow. Several ship empty for you to fill: Inbox, Projects, Places and Things, Vocabulary Notes, and the weekly, quarterly, and decision review folders.

### Essential Folders

**Inbox** holds quick captures with no formatting or organization. Review it during your daily or weekly rhythm, turning what earns a place into atomic notes and deleting the rest.

**Atomic Notes** holds one self-contained concept per note. The folder is flat, with no subfolders, because the notes organize themselves through links and structure notes.

**Structure Notes** holds topic maps that link related atomic notes, closer to a curated reading list than to a folder. You navigate the vault by opening one and following its links.

**Reference Notes** holds processed insights from books, articles, podcasts, and research papers. Each one keeps the author's ideas in their original context, before you pull them into atomic notes. A `Books/` subfolder is set up; add others as your sources need them.

**Reviews** anchors reflection and planning to dates:
	- Daily Notes/ - Day-to-day reflections
	- Weekly Review/ - Weekly patterns and planning
	- Decisions/ - Significant choices requiring documentation
	- Quarterly Reviews/ - Long-term reflection

**Templates** keeps every note template in one place, so you are not choosing a format while trying to capture something.

### Supporting Folders

Add the workflow folders below as the need arises. Attachments and Bases are different: they ship with the vault and are already wired in.

**Projects** documents multi-session work, linking the atomic notes, reference notes, and meetings behind it.

**People** captures expertise and relationship context for the people you work with repeatedly.

**Meetings** keeps searchable records of the meetings worth returning to.

**Vocabulary Notes** defines technical terms inside a single field, such as legal or medical usage. Atomic notes, by contrast, connect across domains.

**Places and Things** covers the locations, tools, and equipment you reference repeatedly.

**Attachments** holds images, PDFs, and audio, kept out of the note folders. Obsidian is configured to save new attachments here.

**Bases** holds the saved `.base` view definitions that templates embed, such as the daily note's created-today and modified-today lists. The Daily Note Template depends on it.

Folders organize workflow (Inbox > processing > reflection), not categories (Marketing/, Philosophy/).

## Note Types

**Atomic Notes** carry one concept each in DAE form: a Definition, an Analogy, and an Example. Name the file with the timestamp followed by the Definition's first sentence, without its final period, as in `YYYYMMDDHHMM The Definition's first sentence.md`. Keep the whole path at or under 171 bytes so the vault survives a Windows download; if the sentence runs long, split the Definition into two sentences rather than cutting words.

**Structure Notes** are navigation hubs that group atomic notes by topic and show how the concepts relate. Update one whenever you add a note that belongs on it.

**Reference Notes** summarize an external source in its own context, with the source metadata alongside. They hold the author's ideas until you have turned them into atomic notes of your own.

**Daily Notes** anchor reflection to a date and link events to the people and concepts involved. They embed Bases views listing the notes created and modified that day.

**People Notes** record expertise, interaction history, and what came out of conversations. Timestamp each interaction so the log stays chronological.

**Meeting Notes** capture attendees, agenda, decisions, and action items, and link to the people and concepts involved.

**No orphans rule:** Every atomic note must appear on at least one structure note for discoverability.

## Template Inventory

Templates are available via Cmd+T:

1. **Atomic Note Template** - DAE framework (optional Anki block)
2. **Company Template** - Organization profile and relationship context
3. **Content Template** - Books, films, and media you consume, with ratings
4. **Daily Note Template** - Temporal reflection with Bases views
5. **Decision Template** - Structured frame for significant choices
6. **General Note Template** - Minimal fallback for uncategorized notes
7. **Meeting Template** - Attendees, context, notes, decisions, next steps
8. **Person Template** - Relationship context and expertise tracking
9. **Quarterly Review Template** - Long-term goal and habit reflection
10. **Reference Note Template** - External source insights and metadata
11. **Structure Note Template** - Topic maps for atomic note navigation
12. **Vocabulary Template** - Technical term definitions in context
13. **Weekly Review Template** - Weekly planning and pattern recognition
14. **Writing Draft Template** - Draft a piece from raw material to final

## Linking Mechanics

### Basic Wikilink Syntax

Create links using double brackets:

```markdown
[[Note Title]]
```

### Pipe Syntax for Custom Display

Show different text than the note title:

```markdown
[[Full Note Title|Display Text]]
```

**Example:**

```markdown
[[202509030636 The DAE framework is a structured method for writing atomic notes|DAE framework]]
```

Displays as "DAE framework" but links to the full atomic note title.

### Aliases

Define multiple terms for the same concept in note frontmatter:

```yaml
aliases:
  - ROI
  - return on investment
  - investment returns
```

All three open the same note, so you can type whichever term your field uses.

### Bidirectional Linking

Links automatically create backlinks, so there is no need to edit both notes. Check **Outgoing Links** in the sidebar to see what you could link to. Check **Backlinks** to see who's linking to the current note. **Unlinked mentions** show text matches that could become links.

## Essential Hotkeys

- **Cmd+N** (Ctrl+N) - Create new timestamped note
- **Cmd+T** (Ctrl+T) - Insert template
- **Cmd+.** (Ctrl+.) - Open today's daily note
- **Cmd+Shift+M** (Ctrl+Shift+M) - Move file to folder
- **Cmd+G** (Ctrl+G) - Open graph view

## Command Line Access

Obsidian ships a command line interface that reads and edits this vault from a terminal, which is how an AI assistant should make changes: it rewrites the wikilinks pointing at a note you rename or move, where a plain file rename leaves them dangling.

To turn it on, open Settings, go to General, enable **Command line interface**, and follow the prompt to register it. You need the Obsidian 1.12.7 desktop installer or later, and the app has to be running for any command to work.

Registration sets up the `obsidian` command for your platform:

- macOS creates a symlink at `/usr/local/bin/obsidian` and asks for admin approval.
- Windows adds the `Obsidian.com` terminal redirector. Restart your terminal afterwards.
- Linux copies the binary to `~/.local/bin/obsidian`. Make sure that directory is on your PATH.

Run `obsidian help` for the full command list. `obsidian create`, `obsidian rename`, `obsidian move`, and `obsidian delete` cover the file operations, and `obsidian backlinks` shows what points at a note before you change it.

If your terminal is sitting inside a vault folder, the CLI uses that vault. Otherwise it uses whichever vault is currently active, so check with `obsidian vault info=path` before running anything that writes. To choose a vault yourself, put `vault=<name>` before the command, as in `obsidian vault=my-vault rename file="Old note name" name="New note name"`. Placed after the command it is ignored rather than refused. Note that `file=` matches a filename, not an alias.

## Quick Start Actions

**1. Explore existing notes**
- Open Structure Notes/Networked Thinking System
- Click through linked atomic notes
- Notice DAE structure pattern (Definition, Analogy, Example)

**2. Create a note**
- Press Cmd+N for a timestamped filename. The new note lands in Inbox/
- Press Cmd+T to insert a template, such as Atomic Note or Meeting
- Fill in the sections and save
- For an atomic note, rename the file to the timestamp plus your Definition's first sentence, press Cmd+Shift+M to move it into Atomic Notes/, and link it from a structure note

**3. Create today's daily note**
- Press Cmd+. to create/open daily note
- The Bases views list the notes created and modified that day, once the Linter writes the date on save
- Add a reflection entry linking to existing atomic notes

**4. Practice linking**
- Use `[[` to start creating wikilinks
- Use `[[Note|Display]]` for custom display text
- Check Outgoing Links panel for unlinked mentions
- Click Link button to convert text to wikilinks
