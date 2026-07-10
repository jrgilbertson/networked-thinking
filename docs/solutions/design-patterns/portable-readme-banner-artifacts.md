---
module: README and design workflow
date: 2026-07-09
problem_type: design_pattern
component: documentation
severity: low
applies_when:
  - A README banner is derived from a larger source image
  - A retained comparison artifact should work outside the author's machine
  - Typography and export fidelity need to survive future edits
tags:
  - readme
  - banner
  - image-assets
  - portability
  - design-workflow
  - webp
---

# Portable README banner artifacts preserve design intent

## Context

A README banner derived from a larger visual source has two different jobs. The production image must load quickly and read clearly at repository widths, while the retained design artifact must make later revisions reproducible. Keeping only the exported raster loses the crop, typography, and comparison rationale. Keeping an HTML study that depends on machine-local paths or network fonts makes the artifact non-portable.

This repository separates those concerns:

- [`Attachments/jason-knowledge-graph.png`](../../../Attachments/jason-knowledge-graph.png) is the retained 2322 x 2022 source graph.
- [`docs/ideation/banner-ratio-options.html`](../../ideation/banner-ratio-options.html) is the portable 3:1 treatment study, with compact-label and caption-rail variants.
- [`Attachments/networked-thinking-readme-banner.webp`](../../../Attachments/networked-thinking-readme-banner.webp) is the 1800 x 600 RGB production derivative embedded by [`README.md`](../../../README.md).
- [`PRODUCT.md`](../../../PRODUCT.md) records the audience, brand register, anti-references, and accessibility constraints that inform future iterations.

## Guidance

1. **Retain the source separately from the production derivative.** Preserve the uncropped image for future art direction, but give the README a purpose-built export. Do not make later editors reverse-engineer a crop from the final WebP.
2. **Keep comparison artifacts repository-portable.** Use paths relative to the HTML file for the graph and fonts. The study resolves its graph and local WOFF2 files from `Attachments/` instead of using an author-specific filesystem path or remote font service.
3. **Vendor typography with its licenses.** The study uses [`Alegreya-Variable.woff2`](../../../Attachments/fonts/Alegreya-Variable.woff2) and [`Inter-Variable.woff2`](../../../Attachments/fonts/Inter-Variable.woff2), with adjacent SIL OFL license texts. This keeps the design reproducible offline and makes redistribution terms discoverable.
4. **Optimize the production artifact independently.** The lossless WebP is 473,734 bytes, compared with 1,889,935 bytes for the retained PNG source. The smaller derivative does not replace the source; each file serves a different purpose.
5. **Keep essential meaning outside the raster.** The README supplies descriptive alt text and follows the banner with live explanatory copy. Embedded text establishes identity, but the image is not the only carrier of repository purpose.
6. **Inspect the actual delivery sizes.** Review the full 1800 x 600 export for crop and typography, then inspect it near GitHub's typical rendered width. A design that works only at source resolution is not ready for the README.

## Why This Matters

The real knowledge graph is evidence that the vault is a working system, not generic network decoration. A dedicated crop preserves that evidence while the compact label keeps branding subordinate. The retained study makes the visual decision inspectable, and local assets prevent the design from changing or breaking when a network resource disappears.

Separating source, study, and derivative also allows future refinements without inflating the README payload or discarding source information.

## When To Apply

Use this pattern when:

- a README image is derived from a larger screenshot, graph, diagram, or photograph;
- multiple treatments or crop decisions need to remain reviewable;
- exact typography matters to the identity of the asset;
- the design should remain reproducible offline or on another contributor's machine; or
- the production image needs a different format, size, or compression policy than its source.

For a disposable image with no expected revisions, retaining a full interactive study may be unnecessary. Still keep the source and licensing information when future redistribution or editing is plausible.

## Example

The README embeds only the delivery asset with descriptive alt text. The design study resolves visual dependencies from the repository:

```css
@font-face {
  font-family: "Alegreya";
  src: url("../../Attachments/fonts/Alegreya-Variable.woff2") format("woff2");
}
```

```html
<img class="graph" src="../../Attachments/jason-knowledge-graph.png" alt="" />
```

The study's graph image is decorative because the surrounding comparison UI names the treatments. The production README image has descriptive alt text because it is part of the document's opening content.

## Verification

Before shipping this pattern:

- confirm the README target and every HTML image and font path resolve from their containing files;
- scan the retained HTML for unintended `http://` or `https://` asset dependencies;
- validate inline JavaScript syntax and exercise treatment controls in a browser when a browser runtime is available;
- confirm the derivative's intended dimensions, color mode, and format;
- inspect the banner at full size and at a representative README width;
- run `git diff --check`; and
- verify font binaries have adjacent license files.

## Related

- [`PRODUCT.md`](../../../PRODUCT.md) defines the product and accessibility constraints.
- [`docs/ideation/banner-ratio-options.html`](../../ideation/banner-ratio-options.html) is the retained implementation artifact.
- [The Impeccable critique](../../../.impeccable/critique/2026-07-10T00-14-00Z__docs-ideation-banner-ratio-options-html.md) records the design-review evidence behind the final treatment.
