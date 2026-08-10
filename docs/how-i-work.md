# How I Work

<!--
  Drop this file in as docs/how-i-work.md and add a nav entry in mkdocs.yml.
  No custom colors or fonts are set here — everything below reads from
  MkDocs Material's own CSS variables (--md-primary-fg-color, etc.), so it
  automatically matches whatever palette and font you've configured, in
  both light and dark mode.
-->

A structural method for turning uncertainty into evidence-backed outcomes — nothing skipped, nothing handed back half-built.

<div style="overflow-x:auto; margin: 2rem 0;">
<svg viewBox="0 0 1400 460" style="width:100%; min-width:640px;" role="img" aria-labelledby="bridgeTitle bridgeDesc">
  <title id="bridgeTitle">A bridge spanning from your problem to your outcome</title>
  <desc id="bridgeDesc">Five towers labeled Understand, Architect, Define, Deliver, and Handover carry the deck across the gap between the client's problem and the delivered outcome.</desc>

  <defs>
    <pattern id="hatch-p" width="9" height="9" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="9" stroke="var(--md-default-fg-color--lightest)" stroke-width="1"/>
    </pattern>
  </defs>

  <!-- banks -->
  <rect x="0" y="330" width="150" height="90" fill="url(#hatch-p)"/>
  <rect x="1250" y="330" width="150" height="90" fill="url(#hatch-p)"/>
  <line x1="0" y1="330" x2="150" y2="330" stroke="var(--md-default-fg-color)" stroke-width="1.5"/>
  <line x1="1250" y1="330" x2="1400" y2="330" stroke="var(--md-default-fg-color)" stroke-width="1.5"/>

  <!-- bank labels -->
  <text x="75" y="300" text-anchor="middle" fill="var(--md-default-fg-color--light)" font-size="11" letter-spacing="1.5">YOUR PROBLEM</text>
  <text x="1325" y="300" text-anchor="middle" fill="var(--md-default-fg-color--light)" font-size="11" letter-spacing="1.5">YOUR OUTCOME</text>

  <!-- back-stay cables -->
  <line x1="40" y1="390" x2="260" y2="170" stroke="var(--md-default-fg-color--light)" stroke-width="1.25"/>
  <line x1="1140" y1="170" x2="1360" y2="390" stroke="var(--md-default-fg-color--light)" stroke-width="1.25"/>

  <!-- main span cable -->
  <path d="M260,170 Q370,208 480,170 Q590,208 700,170 Q810,208 920,170 Q1030,208 1140,170"
        fill="none" stroke="var(--md-default-fg-color--light)" stroke-width="1.25"/>

  <circle cx="40" cy="390" r="3.5" fill="var(--md-default-fg-color--light)"/>
  <circle cx="1360" cy="390" r="3.5" fill="var(--md-default-fg-color--light)"/>

  <!-- deck -->
  <rect x="150" y="324" width="1100" height="6" fill="var(--md-primary-fg-color)"/>

  <!-- towers -->
  <g stroke="var(--md-default-fg-color)" stroke-width="2" fill="none">
    <line x1="248" y1="170" x2="248" y2="324"/><line x1="272" y1="170" x2="272" y2="324"/>
    <line x1="248" y1="220" x2="272" y2="220"/><line x1="248" y1="270" x2="272" y2="270"/>
    <line x1="468" y1="170" x2="468" y2="324"/><line x1="492" y1="170" x2="492" y2="324"/>
    <line x1="468" y1="220" x2="492" y2="220"/><line x1="468" y1="270" x2="492" y2="270"/>
    <line x1="688" y1="170" x2="688" y2="324"/><line x1="712" y1="170" x2="712" y2="324"/>
    <line x1="688" y1="220" x2="712" y2="220"/><line x1="688" y1="270" x2="712" y2="270"/>
    <line x1="908" y1="170" x2="908" y2="324"/><line x1="932" y1="170" x2="932" y2="324"/>
    <line x1="908" y1="220" x2="932" y2="220"/><line x1="908" y1="270" x2="932" y2="270"/>
    <line x1="1128" y1="170" x2="1128" y2="324"/><line x1="1152" y1="170" x2="1152" y2="324"/>
    <line x1="1128" y1="220" x2="1152" y2="220"/><line x1="1128" y1="270" x2="1152" y2="270"/>
  </g>

  <!-- tower labels -->
  <g text-anchor="middle">
    <text x="260" y="354" fill="var(--md-accent-fg-color)" font-size="12" letter-spacing="0.5">01</text>
    <text x="260" y="374" fill="var(--md-default-fg-color)" font-size="14">Understand</text>
    <text x="480" y="354" fill="var(--md-accent-fg-color)" font-size="12" letter-spacing="0.5">02</text>
    <text x="480" y="374" fill="var(--md-default-fg-color)" font-size="14">Architect</text>
    <text x="700" y="354" fill="var(--md-accent-fg-color)" font-size="12" letter-spacing="0.5">03</text>
    <text x="700" y="374" fill="var(--md-default-fg-color)" font-size="14">Define</text>
    <text x="920" y="354" fill="var(--md-accent-fg-color)" font-size="12" letter-spacing="0.5">04</text>
    <text x="920" y="374" fill="var(--md-default-fg-color)" font-size="14">Deliver</text>
    <text x="1140" y="354" fill="var(--md-accent-fg-color)" font-size="12" letter-spacing="0.5">05</text>
    <text x="1140" y="374" fill="var(--md-default-fg-color)" font-size="14">Handover</text>
  </g>

  <!-- dimension line -->
  <line x1="150" y1="402" x2="150" y2="418" stroke="var(--md-accent-fg-color)" stroke-width="1"/>
  <line x1="1250" y1="402" x2="1250" y2="418" stroke="var(--md-accent-fg-color)" stroke-width="1"/>
  <line x1="150" y1="410" x2="1250" y2="410" stroke="var(--md-accent-fg-color)" stroke-width="1"/>
  <path d="M150,410 L162,406 L162,414 Z" fill="var(--md-accent-fg-color)"/>
  <path d="M1250,410 L1238,406 L1238,414 Z" fill="var(--md-accent-fg-color)"/>
  <text x="700" y="438" text-anchor="middle" fill="var(--md-accent-fg-color)" font-size="11" letter-spacing="1">
    THE DISTANCE FROM UNCERTAINTY TO EVIDENCE
  </text>
</svg>
</div>

## The five stages

**Understand.** What problem are we really solving, and what does success look like?

**Architect.** Design the solution and its boundaries before anything is built.

**Define.** Agree scope, what's in, what's out, and how we'll know it worked.

**Deliver.** Build the smallest useful version and prove that it works.

**Handover.** You and your team own it, fully documented, end to end.
