# Design System — "Nexus Ready"

Source: Stitch project **Internship Readiness Platform**, extracted from the
"Top Career Matches" screen family (mobile: *Top Career Matches*, *Top Career
Matches (Animated)*, *Top Career Matches (Animated Scores)*, *Top Career
Matches (Skeleton Loading)*; desktop: *Career Matches (Desktop)*) — the
top-5 career path results screens.

## Brand & Style

Personality: "Trusted Mentor" — knowledgeable, steady, encouraging. Targets
CS/IT students who need a clear, structured path toward professional
readiness.

Style: Corporate / Modern leaning Minimalist. Heavy whitespace to reduce
cognitive load. Avoids decoration; relies on typography and a precise grid.
Target emotional response: "calm confidence."

## Colors

| Token | Hex | Usage |
|---|---|---|
| `primary` | `#3525CD` | Text/icon on-primary contexts, strong emphasis |
| `primary-container` | `#4F46E5` | Main CTA buttons, active nav, progress fills ("Confident Indigo") |
| `on-primary` | `#FFFFFF` | Text on primary surfaces |
| `secondary` | `#006C49` | Deep secondary text |
| `secondary-container` | `#6CF8BB` | Success / "Readiness" states in ML-driven scores |
| `tertiary` | `#684000` | Deep tertiary text |
| `tertiary-container` | `#885500` | Warning / pending-task states |
| `error` | `#BA1A1A` | Errors |
| `error-container` | `#FFDAD6` | Error surfaces |
| `background` | `#F9F9FF` | App background (soft off-white) |
| `surface-container-lowest` | `#FFFFFF` | Cards (lift off the page) |
| `surface-container` | `#E7EEFF` | Nested containers |
| `surface-container-high` / `-highest` | `#DEE8FF` / `#D8E3FB` | Elevated surfaces |
| `on-surface` | `#111C2D` | Primary text ("Deep Slate") |
| `on-surface-variant` | `#464555` | Secondary text |
| `outline` | `#777587` | Borders, dividers |
| `outline-variant` | `#C7C4D8` | Subtle borders (e.g. Slate-200 equivalents) |

Full Material-style role set (fixed/dim/inverse variants) is in the raw
`designMd` pulled from Stitch if finer tokens are needed later.

Flat override shorthands used in the brand brief: Primary `#4F46E5`,
Success/Secondary `#10B981`, Warning/Tertiary `#F59E0B`, Neutral text
`#1E293B` (Slate).

## Typography

Body/UI font: **Inter**. Technical/code contexts (algorithm tips, code
feedback): **JetBrains Mono**.

| Style | Font | Size | Weight | Line height | Letter spacing |
|---|---|---|---|---|---|
| headline-lg | Inter | 32px | 700 | 40px | -0.02em |
| headline-lg-mobile | Inter | 24px | 700 | 32px | -0.01em |
| headline-md | Inter | 20px | 600 | 28px | — |
| body-lg | Inter | 18px | 400 | 28px | — |
| body-md | Inter | 16px | 400 | 24px | — |
| body-sm | Inter | 14px | 400 | 20px | — |
| label-caps | Inter | 12px | 600 | 16px | 0.05em (uppercase metadata, e.g. "ESTIMATED TIME") |
| code-snippet | JetBrains Mono | 14px | 400 | 20px | — |

Headlines: tight letter-spacing, heavy weight, strong visual anchor. Body
text: generous 1.5x line height for long-form reading.

## Spacing

Base unit: **4px**, strict linear scale.

| Token | Value | Typical use |
|---|---|---|
| `base` | 4px | Fine adjustments |
| `xs` | 8px | Tight gaps |
| `sm` | 12px | Compact padding |
| `md` | 16px | Standard internal padding |
| `lg` | 24px | Internal card padding |
| `xl` | 32px | Section spacing |
| `2xl` | 48px | Vertical section separation |
| `3xl` | 64px | Large section separation |

Grid:
- Mobile (≤599px): 4-column, 16px side margins, vertical stacking.
- Tablet (600–1023px): 8-column, 32px margins, sidebars may appear.
- Desktop (≥1024px): 12-column, max-width 1200px.

## Shape

- Buttons / inputs: `0.5rem` (8px) radius.
- Cards / large containers: `1rem` (16px) radius.
- Chips / selection pills: full radius (`9999px`).

## Elevation

Tonal layers + ambient shadows over heavy drop shadows:
- Background `#F9F9FF`; cards lift with pure white (`#FFFFFF`) surface.
- Standard shadow: `0 4px 6px -1px rgba(30, 41, 59, 0.05)`.
- "Next Step"/ML-recommendation cards: prefer a 1px `outline-variant` stroke
  over a shadow (flatter, more professional).
- Modals/dropdowns: stronger shadow with a slight indigo tint.

## Key Components (relevant to results screens)

- **Readiness Cards**: 16px radius, header for skill/role name, footer for a
  progress bar — this is the card pattern used for each of the 5 ranked
  career matches.
- **Progress bars**: track `surface-container` (Slate-100 equivalent), fill
  gradient `primary` → `primary-container` (Indigo-500 → 600), animated on
  load — matches the "Animated Scores" variant of the results screen.
- **Chips**: skill/tag pills (e.g. "Java", "SQL", "Remote") — light
  Indigo-50-equivalent background, Indigo-700-equivalent text.
- **Skeleton loaders**: light `surface-container` pulse animation, same
  8px/16px corner radii as the loaded content — used in the "Skeleton
  Loading" variant while ML scoring is fetched.
- **Buttons**: primary = solid indigo fill, white text, hover slightly
  darker; secondary = 1px indigo stroke, transparent fill.
- **Bottom nav (mobile, 390px frame)**: 24px icons, 12px labels.
