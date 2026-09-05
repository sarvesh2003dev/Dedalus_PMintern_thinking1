# 90-Day PM Internship Plan

## Operating principle

Start close to users, keep the first scope small, and ship only after the value and safety boundary are understood. This plan is a personal working model—not a statement about Dedalus’s internal roadmap.

## Days 1–30: Learn the system and locate the sharpest problem

### Objectives

- Become technically fluent in the public product surface and the developer workflow around persistent machines.
- Map the agent lifecycle from provisioning through completion, interruption, and recovery.
- Speak with developers and internal partners to identify the highest-friction recovery moments.
- Choose one narrow problem with a clear success metric.

### Deliverables

- A workflow map annotated with known evidence, assumptions, and open questions.
- 8–12 developer conversations or support-signal reviews, subject to access and consent.
- A concise problem brief with target user, job to be done, alternatives, and non-goals.
- Baseline instrumentation proposal for activation and recovery reliability.

### Decisions to make

- Is the core gap task visibility, checkpointing, handoff, or something else?
- Is the right first user a solo agent developer, a platform team, or an internal workflow?
- What must be explicitly out of scope to preserve a two-week build?

## Days 31–60: Prototype and validate

### Objectives

- Turn the chosen problem into an explicit user flow and a small functional slice.
- Validate language and behavior with real developer tasks, not opinion-only reviews.
- Work daily with engineering and design on technical constraints, safety, and instrumentation.

### Deliverables

- PRD with success criteria, API/UX contract, edge cases, and launch guardrails.
- Clickable or functional prototype for one end-to-end workflow.
- At least two usability or technical validation cycles.
- Metrics dashboard specification and an experiment readout template.

### Decisions to make

- Which recovery action is safe to make easy?
- What must require an explicit developer confirmation?
- Which telemetry is genuinely necessary—and how can it minimize sensitive content?

## Days 61–90: Ship a constrained beta and learn

### Objectives

- Release a limited, observable version to the smallest appropriate cohort.
- Help early users succeed directly; treat confusing onboarding as product feedback.
- Make a documented go/no-go recommendation for the next iteration.

### Deliverables

- Launch checklist, documentation, and support path.
- Cohort definition and consent-aware feedback plan.
- Readout: activation, recovery decisions, qualitative themes, limitations, and next actions.
- A recommendation to expand, narrow, iterate, or stop.

### Decisions to make

- Did the product reduce recovery friction for a real workflow?
- Are warning and safety boundaries understood?
- Is the problem large enough to justify a durable platform primitive?

## How I would work

| Behavior | What it looks like |
| --- | --- |
| High agency | Bring a clear artifact, recommendation, and next experiment—not just a question |
| Technical fluency | Read docs, run workflows, understand constraints, and make trade-offs legible |
| User closeness | Talk to developers early and compare opinions with observed behavior |
| Good judgment | Mark uncertainty, protect sensitive data, and kill scope that does not earn its complexity |
| Execution | Keep a visible decision log, short feedback loops, and an honest launch bar |

## What success would mean

By the end of the internship, I would want to leave behind more than a feature: a deeply understood developer problem, a validated scope, clean instrumentation, a reusable decision record, and a product surface that makes persistent agent work easier to trust.