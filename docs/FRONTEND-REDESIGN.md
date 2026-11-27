# Frontend redesign playbook

Use this when redesigning a product across multiple journeys. Start by watching people complete their work, then choose a design direction and prove it on the hardest screen. Use the [frontend skill inventory](FRONTEND-SKILLS.md) when picking a review or implementation skill.

## What the sources teach

| Decision | What to look for | How to use the guidance |
| --- | --- | --- |
| Diagnose the experience | Find the moment a user loses their place, has to search for an action, or would make a decision without enough information. | Use one interface review first. Record the viewport, task, action, visible result, and consequence. Use a specialist for the underlying problem. Jakub’s layout and writing lenses distinguish page hierarchy from unclear labels. His accessibility lens checks how the same controls work without a pointer. [Jakub Krehel’s collection](https://github.com/jakubkrehel/skills) |
| Define the visual direction | Establish a recognizable hierarchy, typography, surfaces, and color roles that fit the product and hold up in dense views. | Draw two or three distinct directions using the same real tasks and content states. Use Anthropic’s frontend design guidance for a coherent point of view and Taste Skill for specific layout and visual decisions. Use the Awwwards material where the brief calls for editorial presentation or deliberate storytelling. [Anthropic](https://github.com/anthropics/skills) · [Taste Skill](https://github.com/Leonxlnx/taste-skill) · [Meng To](https://github.com/MengTo/Skills) |
| Make motion earn its place | An animation can preserve orientation or acknowledge a state change. Delayed responses and repeated entrances make frequent work feel slower. | Test each transition at the frequency users will encounter it. Give keyboard and repeated actions immediate feedback. Use motion on a drawer or an occasional reveal when it explains where content came from. Check rapid reversal, interrupted transitions, touch gestures, and reduced motion. [Emil Kowalski’s collection](https://github.com/emilkowalski/skills) |
| Make the interface work across sizes | Focus, labels, reading order, and decision-critical data must survive narrow widths and zoom. | Test keyboard traversal and focus return, label field errors, inspect sticky elements around focus, and check reflow at 320 CSS pixels. A graph or dense table can have its own scrolling surface. Keep the surrounding reading and action flow usable. [W3C reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) · [W3C focus not obscured](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html) |
| Choose component and state boundaries | Repeated toggles and option flags can leave controls inconsistent across pages. Redundant client fetches can stall the first useful screen. | Define the component’s states and required slots. Use existing native controls or accessible primitives where they already provide the behavior. Check for independent requests that can run together and load optional calculator, chart, or animation code when needed. Measure readiness and interaction on the working page. [shadcn/ui](https://ui.shadcn.com/) · [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills) |

## Before choosing a direction

1. Inventory the main surfaces, routes, role boundaries, and tasks. For each task, identify the actual start and the success state. Include empty, loading, error, denied, and interrupted states that users can reach.
2. Run the current product on desktop and narrow mobile with realistic content. Keep a keyboard pass separate from pointer exploration. Record the same tasks, viewports, and fixture states so a later comparison is reproducible.
3. Rank findings by consequence. Lost progress, answer corruption, hidden controls, and misleading feedback take priority over cosmetic inconsistencies. Count extra actions or note exact viewport failures where that makes a finding clear.
4. Compare visual directions on the same hard screens. Agree on typography roles, spacing, semantic color, component states, and navigation before expanding the work. Specify anything that must retain its URL, persisted state, or access rule.
5. Build one complete vertical slice. Verify it through the normal entry point with real server responses or explicitly labeled fixtures. Capture changes against the baseline before migrating adjacent screens.

## Record decisions before implementation

- **Visual system.** Give background, raised surfaces, primary action, text, focus, success, error, and caution separate semantic roles. Include the actual typography roles for paragraphs, dense labels, math, and timers. Test the real rendered foreground/background combinations.
- **Component contracts.** Document which parts of a question are shared, which each experience owns, and how keyboard focus and style change with state. A study session can share the answer button and feedback primitives with a timed exam while keeping separate grading, timing, and navigation rules.
- **Navigation state.** Put shareable filters and destinations in the URL where appropriate. Distinguish a reusable route from private input and in-progress state. Preserve return paths when a person opens a detail or signs in.
- **Motion.** Write down what moves, why, and which repeated actions should respond immediately. Verify that reduced motion leaves the same controls and feedback. Measure a slow route before attributing it to animation.

For an existing journey, start with `better-interface` and use one owning lens to investigate a specific problem. Use `frontend-design` for a visual concept and `variant` or the existing prototype skill when choosing between concrete alternatives. Use `web-design-guidelines` for implementation review, and use Vercel React Best Practices when a real browser trace or request path needs investigation.

## Apply it to SAThack

The redesign can share a visual system across the site while giving each type of work an appropriate layout.

| Part of the site | Task to exercise | What the design needs to prove |
| --- | --- | --- |
| Public pages and sign-in | Understand the study options, open a route, sign in, and return to that route. | The main action and access rules are clear. Authentication keeps the intended destination and offers actionable recovery. |
| Study dashboard and question banks | Find an appropriate topic, choose difficulty or progress filters, open an item, and return to the same results. | Labels follow student intent. Search, filtering, and browsing preserve context. Empty results explain how to continue. Admin-only archives retain their access boundary. |
| Single-question solving and practice sessions | Solve Reading & Writing and Math examples with long passages, diagrams, multiple choice, and numeric input. | Both stem and answers are legible. The primary action stays reachable. Marking, notes, answer elimination, and Desmos have separate roles and clear states. A user can tell what will survive moving away or refreshing. |
| Timed tests | Answer, mark for review, jump between questions, and submit a module. | Timer and progress are always understandable. Review restores the right question. Calculator use does not obscure the exam or cause focus loss. |
| Results, review, and saved work | Find a missed question, understand why, retry it, and return to the relevant result. | The result guides the next study action. Answer, explanation, and retry history have a clear order and remain readable on mobile. |
| Admin and moderation | Find a question, edit its metadata, review a report, and confirm a decision. | Essential context and decisions remain visible on narrow screens. Error recovery retains entered values. Access status and audit history are explicit. |

### Prove the solving workspace first

Use the longest representative passage, a wide Math figure, a numeric input, a multi-choice question with wrapped options, and a question with a long explanation. Use synthetic or approved material when saving screenshots.

- On desktop, compare passage-and-question and calculator-and-question layouts on a short as well as a wide screen. Ensure each pane shows which content scrolls. Give focus and touch users an alternative to dragging a splitter or sheet.
- On mobile, order passage, stem, answers, and feedback so the next action is obvious. Try the software keyboard, zoom, and a long explanation with a sticky footer. Check whether any footer covers the focused field or response.
- Use distinct visual and accessible states for selected, eliminated, saved, submitted, correct, incorrect, and unavailable. Check whether a repeated shortcut competes with ordinary typing in notes or calculator inputs.
- Test initial load, fetching the next question, a failed submission, a successful retry, Back, refresh, and session restoration. Explicitly track which state belongs to the question, practice session, or user.
- Keep frequent interactions prompt. Animate only an occasional transition that helps users see what opened or changed. Verify that users who prefer reduced motion retain the same information and control.

## Evidence to bring to the design review

- Desktop and narrow captures of the key steps, with the corresponding issue IDs and a short description of what the user could or could not do.
- A keyboard run covering skips, answer selection, menu and dialog escape, focus return, and visible focus. Add a screen-reader check for answer options, feedback, and progress.
- The smallest set of representative fixtures for long text, missing media, numbers and fractions, no results, invalid inputs, and failed network requests.
- A browser trace for the transition that feels slow, used alongside the visible result. Compare time to a usable question and data motion between steps under the same conditions.
- A short release checklist mapping each agreed journey to current evidence. Separate the checks that ran locally from production verification.

The referenced [frontend article](https://agenticskills.io/learn/best-frontend-skills) is a discovery list. The [inventory](FRONTEND-SKILLS.md) maps names to their actual maintainers, revisions, installation status, and prerequisites.
