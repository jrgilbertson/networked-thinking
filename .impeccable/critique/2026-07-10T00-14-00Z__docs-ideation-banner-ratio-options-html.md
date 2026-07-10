---
target: "3:1 README banner ratio study"
total_score: 32
p0_count: 0
p1_count: 2
timestamp: 2026-07-10T00-14-00Z
slug: docs-ideation-banner-ratio-options-html
---
# Banner Ratio Study Critique

## Design Health Score

| # | Heuristic | Score | Key Issue |
|---|---|---:|---|
| 1 | Visibility of System Status | 3 | Identity is immediate; the artifact's meaning is less explicit. |
| 2 | Match System / Real World | 4 | Uses a real working graph and plain language. |
| 3 | User Control and Freedom | 4 | No interaction or trap; role-limited for a static asset. |
| 4 | Consistency and Standards | 4 | Strong companion-site continuity. |
| 5 | Error Prevention | 2 | Baked descriptor text is vulnerable at narrow widths. |
| 6 | Recognition Rather Than Recall | 3 | Neither Obsidian nor working vault is named. |
| 7 | Flexibility and Efficiency | 2 | One crop and text scale must serve every README width. |
| 8 | Aesthetic and Minimalist Design | 3 | Clean, but the plate competes with the evidence. |
| 9 | Error Recovery | 4 | No recoverable interaction; role-limited for a static asset. |
| 10 | Help and Documentation | 3 | Descriptor orients, but essential context must remain live. |
| **Total** | | **32/40** | **Good** |

## Anti-Patterns Verdict

**LLM assessment:** Pass, with one familiar-template caveat. The authentic graph, Alegreya, and restrained cobalt identity prevent the banner from reading as generic AI/SaaS imagery. The conventional white title plate with a colored top rule is the only templated move, and its current footprint makes the graph feel more like a backdrop than the subject.

**Deterministic scan:** One warning at `docs/ideation/banner-ratio-options.html:16-21`: `overused-font` for Inter. This is a low-priority false positive for the banner because Inter is established companion-site body typography and the graph plus Alegreya carry the identity.

**Visual overlays:** No reliable overlay is available. The browser runtime reported no available browser, so inspection fell back to source HTML/CSS and the graph asset.

## Overall Impression

The banner is credible, editorial, and grounded in a real system. Its biggest opportunity is to make the 3:1 crop feel deliberately art-directed rather than like a graph placed behind a title card.

## What's Working

1. **Authentic evidence:** Irregular clusters, hubs, outliers, and mixed node colors communicate a mature working vault.
2. **Brand continuity:** Alegreya, Inter, cobalt, ink, and white connect the repository to the companion site without excess chrome.
3. **Disciplined composition:** The opaque plate protects legibility over a complex source, and the restrained palette avoids productivity-app cliches.

## Priority Issues

### [P1] The descriptor will not survive narrow README rendering

Embedded raster text scales with the image, so the descriptor becomes microtype on phone-width GitHub layouts. Test at 320-360 CSS pixels; either shorten and enlarge it or move the explanation into live README text below the image. **Suggested command:** `$impeccable adapt`.

### [P1] The 3:1 crop makes the real graph read partly as decorative texture

The shallow center crop discards much of the source topology, weakening the promise to show the system working. Art-direct a dedicated band that preserves several hubs and the blue/green relationship instead of relying on generic `object-fit: cover`. **Suggested command:** `$impeccable layout`.

### [P2] The title plate competes with the stated subject

The plate spans about 42% of the canvas and obscures a meaningful part of the graph. Reduce its width or vertical footprint and move it toward lower-value whitespace while preserving an opaque contrast field. **Suggested command:** `$impeccable distill`.

### [P2] The descriptor is not repository-specific

"Connected notes, clearer thinking, and better work" could describe many PKM tools. Test a concrete line such as "A working Obsidian vault for connected notes and clearer thinking." **Suggested command:** `$impeccable clarify`.

## Persona Red Flags

**First-time GitHub visitor:** The graph establishes credibility, but the visitor may read it as generic network imagery because neither Obsidian nor vault appears in the banner.

**Distracted mobile reader:** The title survives, but the descriptor and fine edges disappear when the banner scales down, making the first impression less informative.

**Design-conscious PKM practitioner:** The authentic source earns trust, but a shallow generic crop may feel less honest than a deliberately selected hub-to-hub view.

## Minor Observations

- The cobalt rule is an efficient brand cue.
- The 94% white plate creates strong text contrast.
- The fine keyline may disappear at reduced sizes and is not essential.
- Node colors should not be presented as semantic categories unless the README explains them.

## Questions to Consider

- Must the descriptor survive inside the image at 320 pixels wide, or can live README copy do that job?
- Should the final crop maximize density, or tell one clearer hub-to-hub story?
- Is naming the working Obsidian vault more valuable than the broader benefit statement?
