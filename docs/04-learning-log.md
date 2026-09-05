# Learning Log: From Public Docs to Evidence

## Purpose

This log turns learning into visible, reproducible evidence. I will record what I actually ran, observed, and could not verify. I will not backfill polished results or present documentation reading as production experience.

## Learning sequence

### Step 1 — Learn the public surface

- Read the [Dedalus Machines quickstart](https://www.dedaluslabs.ai/beta/dedalus-machines).
- Identify the lifecycle concepts: machine creation, command execution, persistence, retrieval, and cleanup.
- Write down the terms I can explain and the terms that still need validation.

**Evidence to add:** date, SDK/language used, commands run, actual output summary, and a link to the commit.

### Step 2 — Run a minimal persistent workflow

Build a tiny task with two stages:

1. Create an artifact such as a file, test report, or task note.
2. Reconnect to the same machine and verify the artifact remains available.

**What to document:** setup steps, command transcript with secrets removed, elapsed time, expected vs. actual behavior, and failure modes.

### Step 3 — Simulate interruption and recovery

Use a safe, non-production task that can be paused between stages.

1. Define the last known-safe boundary.
2. Record a small checkpoint note outside any secret-bearing context.
3. Interrupt or abandon the next stage.
4. Reconnect and decide whether to continue, retry, or discard.
5. Compare the recovery process against a logs-only baseline.

**What to document:** exact recovery decision, ambiguity encountered, and whether the proposed checkpoint contract would have changed the outcome.

### Step 4 — Learn from developers, with consent

Run short conversations with agent builders or platform engineers. Do not call someone a “customer” unless they are one.

**Research questions:**

- What long-running agent work do you restart most often?
- What information do you reconstruct by hand?
- Which data would you never want a platform checkpoint to hold?
- When would a persistent machine be more useful than an ephemeral sandbox?
- What would make a recovery tool trustworthy?

**Publication standard:** share only anonymized, consented themes. Include sample size and limitations.

### Step 5 — Revise publicly

When observations challenge the thesis, change the proposal and explain why. A small, well-documented reversal is stronger evidence of product judgment than defending the first idea.

## Experiment log template

Copy this section for every hands-on run.

```md
### Run YYYY-MM-DD — <short title>

- Goal:
- Public docs / version consulted:
- Environment and SDK:
- Steps taken:
- Expected behavior:
- Observed behavior:
- Result: success / partial / failed
- What persisted:
- What did not persist:
- Risks or ambiguity:
- Evidence: commit, sanitized log, or screenshot
- Next change to the proposal:
```

## Current status

| Item | Status | Evidence |
| --- | --- | --- |
| Read public product documentation | Planned | Add a dated note after completing |
| Complete minimal persistent workflow | Planned | Add commit and sanitized observations |
| Run interruption/recovery exercise | Planned | Add reproducible scenario |
| Conduct developer conversations | Planned | Add consented, aggregated themes |
| Revise PRD from evidence | Planned | Link decision log |

## Integrity note

“Planned” means planned. This document will only use “completed” after I can point to reproducible evidence.