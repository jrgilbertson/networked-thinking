# Getting Started with the Companion Vault

This vault provides pre-configured infrastructure for networked thinking. Essential plugins, templates, and example notes are already set up—you can start creating notes immediately.

## Four Design Principles

Your workspace rests on four principles that make knowledge work frictionless:

**Separate raw from processed.** Capture ideas to Inbox instantly without organizing. Process them during weekly review when you have mental space for evaluation. This separation maintains flow during interruption and deliberation during cultivation.

**Favor flat over deep.** Links beat folder hierarchies for knowledge organization. Structure notes beat subfolders for navigation. Deep hierarchies hide connections; flat structures reveal them. A note about "decision fatigue" appears in Psychology, Productivity, and Leadership contexts through links—not by choosing a single folder.

**Blend time and topic.** Daily notes capture temporal reflection (what happened today). Structure notes create conceptual maps (productivity concepts organized by relationship). Time preserves context; topics reveal patterns. Both matter.

**Build semantic connections through links and aliases.** Every link creates a meaningful relationship in your knowledge graph. Aliases extend discoverability—"ROI," "return on investment," and "investment returns" all point to the same concept. Discovery emerges through meaning, not memory.

## Folder System

Your workspace contains thirteen folders organized by workflow state, not knowledge category.

### Essential Folders (6)

**Inbox** - Quick capture without formatting or organization. Review during daily or weekly rhythms, converting worthy items to atomic notes and deleting the rest.

**Atomic Notes** - Self-contained concepts, one per note. Uses flat structure with no subfolders. Notes organize through links and structure notes, not folder hierarchies. Every atomic note must appear on at least one structure note (no orphans).

**Structure Notes** - Topic maps linking related atomic notes. Think curated reading lists organized around themes. Navigate your knowledge by opening structure notes and following links.

**Reference Notes** - Processed insights from books, articles, podcasts, research papers. Summarizes source ideas in original context. Contains Books/ and Articles/ subfolders for organization (optional).

**Reviews** - Temporal anchors for reflection and planning. Nested structure:
	- Daily Notes/ - Day-to-day reflections
	- Weekly Review/ - Weekly patterns and planning
	- Decisions/ - Significant choices requiring documentation
	- Quarterly Reviews/ - Long-term reflection

**Templates** - All note templates in one location. Reduces cognitive load during capture by providing consistent structure.

### Optional Folders (7)

Add these only when specific needs arise:

**Projects** - Multi-session work documentation linking atomic notes, reference notes, and meetings.

**People** - Recurring collaborators, capturing expertise and relationship context.

**Meetings** - Regular meetings requiring searchable records.

**Vocabulary Notes** - Technical terms within specific contexts (legal, medical, technical). Differs from atomic notes which connect across domains.

**Places and Things** - Physical locations, tools, equipment, resources referenced repeatedly.

**Attachments** - Images, PDFs, audio files, media. Keeps them separate from knowledge content.

**Prompts** - AI prompts for processing notes, writing atomic notes, analyzing connections. Save for reuse and refinement.

**Key principle:** Folders organize workflow (Inbox → processing → reflection), not categories (Marketing/, Philosophy/). Knowledge transcends arbitrary categories.

## Note Types

**Atomic Notes** - One concept per note following DAE framework: Definition (concise explanation), Analogy (memorable comparison), Example (concrete application). Timestamp filename format: `YYYYMMDDHHMM Full sentence describing core insight.md`. Self-contained and reusable across contexts.

**Structure Notes** - Navigation hubs organizing atomic notes by topic. Create themed collections showing how concepts relate. Ensures no atomic note becomes orphaned. Update as you add relevant atomic notes.

**Reference Notes** - Summaries of external sources in original context. Captures author's ideas before integrating into your thinking through atomic notes. Includes source metadata and key concepts.

**Daily Notes** - Temporal reflection anchoring knowledge to specific dates. Includes Dataview queries showing notes created/modified today. Links events to people to concepts.

**People Notes** - Relationship context for recurring collaborators. Documents expertise, interaction history, insights from conversations. Timestamp each interaction for chronological tracking.

**Meeting Notes** - Event documentation with attendees, agenda, decisions, action items. Links to people who participated and concepts discussed.

**No orphans rule:** Every atomic note must appear on at least one structure note for discoverability.

## Template Inventory

The vault includes twelve templates accessible via Cmd+T:

1. **Atomic Note Template (Default)** - DAE framework structure
2. **Atomic Note Template (Anki)** - DAE plus spaced repetition syntax
3. **Daily Note Template** - Temporal reflection with Dataview queries
4. **Decision Template** - Structured frameworks for significant choices
5. **General Note Template** - Minimal fallback for uncategorized notes
6. **Meeting Template** - Attendees, agenda, decisions, action items
7. **Person Template** - Relationship context and expertise tracking
8. **Quarterly Review Template** - Long-term goal and habit reflection
9. **Reference Note Template** - External source insights and metadata
10. **Structure Note Template** - Topic maps for atomic note navigation
11. **Vocabulary Template** - Technical term definitions in context
12. **Weekly Review Template** - Weekly planning and pattern recognition

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

All aliases link to the same note, respecting how different domains use varied terminology.

### Bidirectional Linking

Links automatically create backlinks—no need to edit both notes. Check **Outgoing Links** (left sidebar) to see what you could link to. Check **Backlinks** to see who's linking to the current note. **Unlinked mentions** show text matches that could become links.

## Essential Hotkeys

- **Cmd+N** (Ctrl+N) - Create new timestamped note
- **Cmd+T** (Ctrl+T) - Insert template
- **Cmd+.** (Ctrl+.) - Open today's daily note
- **Cmd+Shift+M** (Ctrl+Shift+M) - Move file to folder
- **Cmd+G** (Ctrl+G) - Open graph view

## Quick Start Actions

**1. Explore existing notes**
- Open Structure Notes/Networked Thinking System
- Click through linked atomic notes
- Notice DAE structure pattern (Definition, Analogy, Example)

**2. Create a note**
- Press Cmd+N for timestamped filename
- Press Cmd+T to insert template
- Try Meeting Template or Atomic Note Template
- Fill in sections and save

**3. Create today's daily note**
- Press Cmd+. to create/open daily note
- Notice Dataview queries automatically show notes created and modified today
- Add a reflection entry linking to existing atomic notes

**4. Practice linking**
- Use `[[` to start creating wikilinks
- Use `[[Note|Display]]` for custom display text
- Check Outgoing Links panel for unlinked mentions
- Click Link button to convert text to wikilinks
