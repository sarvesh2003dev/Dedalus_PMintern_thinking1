# Metrics and Experiment Plan

## Measurement principle

A durable-agent feature should be judged by changed developer behavior and recovery reliability—not by API calls alone. Every metric below is a **proposal** until it is instrumented and evaluated with real users.

No results are reported in this repository yet.

## North-star outcome

**Successful durable recovery:** the share of eligible interrupted tasks that a developer restores to a deliberate next state (resume, retry from a known-safe boundary, or discard with documented context) without manual state reconstruction.

This is more meaningful than “checkpoint created,” because a checkpoint is useful only if it improves a recovery decision.

## Funnel

```
Machine created
  → first task started
  → first checkpoint created
  → checkpoint becomes ready
  → recovery exercise attempted
  → deliberate recovery outcome reached
```

## Candidate metrics

| Metric | Definition | Why it matters | Guardrail |
| --- | --- | --- | --- |
| Time to first durable run | Time from machine creation to a task that creates and retrieves a ready checkpoint | Activation and onboarding clarity | Segment by new vs. returning developer |
| Checkpoint readiness rate | Ready checkpoints / creation attempts | Core reliability | Track failure reason; do not hide retries |
| Recovery decision completion | Eligible interrupted tasks with a recorded resume/retry/discard decision | Whether the feature supports the real job | Never equate a decision with task success |
| Median recovery time | Time from interruption detected to a deliberate recovery decision | Friction reduction | Inspect long-tail failures separately |
| Unsafe-resume warnings acknowledged | Warning acknowledgements / eligible recovery attempts | Safety comprehension | Validate understanding, not just clicks |
| Week-one return for checkpoint users | Users who return to inspect/create a checkpoint within seven days | Early retained value | Compare cohorts only after sufficient sample size |

## Proposed event schema

```json
{
  "event": "checkpoint.ready",
  "checkpoint_id": "cp_...",
  "machine_id": "machine_...",
  "task_label": "apply-auth-middleware",
  "created_at": "2026-09-05T00:00:00Z",
  "metadata_key_count": 2
}
```

A companion recovery event should capture the **decision** and reason without collecting secret payloads:

```json
{
  "event": "checkpoint.recovery_decided",
  "checkpoint_id": "cp_...",
  "decision": "retry_from_boundary",
  "reason_category": "task_process_ended",
  "warning_acknowledged": true
}
```

## First experiments

### Experiment 1 — Can a developer explain the model?

**Hypothesis:** After a short guided run, at least a strong majority of target developers can correctly explain what a checkpoint preserves and what it does not.

**Method:**

1. Give 5–8 developers a scripted multi-step task on persistent compute.
2. Ask them to create a checkpoint, interrupt the run, and choose a recovery action.
3. Ask four comprehension questions before showing any help text.
4. Record confusion points and revise the language, not just the UI.

**Pass signal:** Clear explanation of the distinction between machine persistence, task status, and external side effects.

### Experiment 2 — Does the recovery path beat manual forensics?

**Hypothesis:** For a representative interrupted workflow, checkpoint guidance reduces time to a deliberate recovery decision compared with a logs-and-files-only baseline.

**Method:**

1. Use the same small task in two sessions.
2. In the baseline, provide files and logs only.
3. In the treatment, provide a checkpoint ID, status, warnings, and recovery notes.
4. Measure time, confidence, error types, and recovery outcome.

**Do not claim a win** until the task, participants, and results are published or reproducibly documented.

### Experiment 3 — Is the proposed API small enough?

**Hypothesis:** Developers can integrate one checkpoint call at a meaningful task boundary without adopting a new orchestration framework.

**Method:**

1. Show a minimal SDK sketch.
2. Ask users where they would insert it in their actual workflow.
3. Count integration blockers and missing context.
4. Remove fields or abstractions that do not change a recovery decision.

## Qualitative questions

- “Tell me about the last agent run you had to restart.”
- “Where do you currently record the last known-safe point?”
- “Which state would you trust a platform to retain?”
- “What would make you refuse to press Resume?”
- “What would a teammate need to safely take over this task?”

These questions are prompts for future research, not evidence that research has already happened.

## Analysis standards

- Predefine the success metric before reviewing results.
- Keep raw notes private unless participants explicitly consent to publication.
- Publish aggregated themes, methods, limitations, and disconfirming evidence.
- Avoid percentage claims with small sample sizes.
- Separate product telemetry from customer content; minimize and redact data by default.

## Decision after the first cycle

| Finding | Decision |
| --- | --- |
| Users understand the model and recover faster | Build a constrained alpha with SDK + status surface |
| Users want visibility but distrust automatic resumption | Prioritize inspectability and explicit recovery modes |
| Users already solve this well in their framework | Document an integration pattern rather than create a platform primitive |
| Metadata/safety concerns dominate | Narrow scope; solve governance and redaction before growth |