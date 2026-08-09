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

This repository separates those concerns. The current delivery state, updated on 2026-08-09, is:

- [`Attachments/networked-thinking-readme-banner.webp`](../../../Attachments/networked-thinking-readme-banner.webp) is the 1600 x 640 RGB production asset embedded by [`README.md`](../../../README.md).
- [`Attachments/jason-knowledge-graph.png`](../../../Attachments/jason-knowledge-graph.png) and [`docs/ideation/banner-ratio-options.html`](../../ideation/banner-ratio-options.html) are retained as the source and portable treatment study for the previous 3:1 banner. They are historical design evidence, not the source of the current artwork.
- [`PRODUCT.md`](../../../PRODUCT.md) records the audience, brand register, anti-references, and accessibility constraints that inform future iterations.

## Guidance

1. **Retain the source separately from the production derivative when one exists.** Preserve editable or uncropped source material for future art direction, but give the README a purpose-built export. The current banner arrived as a final production asset without an editable master in this repository, so future revisions should replace it from the shared Networked Thinking visual system rather than reverse-engineer the WebP.
2. **Keep comparison artifacts repository-portable and label historical studies accurately.** Use paths relative to the HTML file for local assets and fonts. A retained study that no longer represents the shipped artwork is useful design history, but it must not be described as the current banner's reproducible source.
3. **Vendor typography with its licenses.** The historical study uses [`Alegreya-Variable.woff2`](../../../Attachments/fonts/Alegreya-Variable.woff2) and [`Inter-Variable.woff2`](../../../Attachments/fonts/Inter-Variable.woff2), with adjacent SIL OFL license texts. This keeps that artifact reproducible offline and makes redistribution terms discoverable.
4. **Optimize and record the production artifact independently.** The current lossless WebP is 1600 x 640 and 666,364 bytes. These values are delivery facts for validation, not properties inherited from the older graph source or 3:1 study.
5. **Keep essential meaning outside the raster.** The README alt text names the title, Companion Vault descriptor, connected-graph subject, and exact tagline, "The missing manual for knowledge work in the AI age." Live explanatory copy follows the banner, so the image is not the only carrier of repository purpose.
6. **Inspect the actual delivery sizes.** Review the full 1600 x 640 export for crop and typography, then inspect it near GitHub's typical rendered width. A design that works only at source resolution is not ready for the README.

## Why This Matters

The connected knowledge graph makes the system's relationships legible at a glance rather than using generic network decoration. The current banner carries the shared Networked Thinking identity, while descriptive alt text preserves its essential message for people who do not see the raster. The older portable study remains inspectable as design history without being mistaken for the current source.

When those artifacts are available, separating source, study, and derivative allows future refinements without inflating the README payload or discarding source information. When only a final export is retained, document that limitation and preserve the exact delivery facts.

## When To Apply

Use this pattern when:

- a README image is derived from a larger screenshot, graph, diagram, or photograph;
- multiple treatments or crop decisions need to remain reviewable;
- exact typography matters to the identity of the asset;
- the design should remain reproducible offline or on another contributor's machine; or
- the production image needs a different format, size, or compression policy than its source.

For a disposable image with no expected revisions, retaining a full interactive study may be unnecessary. Still keep the source and licensing information when future redistribution or editing is plausible.

## Example

The README embeds only the delivery asset with descriptive alt text. The retained historical study still resolves its visual dependencies from the repository:

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
- [`docs/ideation/banner-ratio-options.html`](../../ideation/banner-ratio-options.html) is the retained historical implementation artifact for the previous banner.
- [The Impeccable critique](../../../.impeccable/critique/2026-07-10T00-14-00Z__docs-ideation-banner-ratio-options-html.md) records the design-review evidence behind the final treatment.
