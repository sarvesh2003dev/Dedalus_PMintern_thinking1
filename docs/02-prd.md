# PRD: Durable-Agent Checkpoints (Proposed v0)

> This is an illustrative product specification for discussion. Endpoint names and behaviors are proposed; they are not an existing Dedalus API.

## 1. Goal

Help a developer create a safe, inspectable recovery point for a long-running agent task, then understand whether and how to resume it after an interruption.

## 2. Target user and primary use case

**Target user:** A developer who runs an agent on persistent compute and wants a reliable boundary between “work completed safely” and “work in progress.”

**Primary use case:** A code-maintenance agent completes a discrete stage—such as cloning a repository, writing a patch, or preparing a test artifact. Before it begins the next side-effecting stage, the developer records a checkpoint. If the run is interrupted, the developer can inspect the checkpoint and choose a recovery action.

## 3. v0 user story

> As an agent developer, I can create a named checkpoint with a small set of safe metadata so that, after interruption, I can identify the last known-safe task boundary and resume using documented instructions.

### Acceptance criteria

- A developer can create a checkpoint from an existing machine using one SDK call or one API request.
- Every checkpoint has an immutable ID, timestamp, task label, status, and link to the machine context.
- The developer can retrieve a list of checkpoints ordered by recency.
- A checkpoint exposes whether it is ready, incomplete, failed, or expired.
- The interface makes it explicit that external side effects may not be reversible or idempotent.
- The developer can discover the recommended next action: inspect, resume, retry from a safe boundary, or discard.
- Events are emitted so a developer can connect the lifecycle to their own observability stack.

## 4. Proposed interface

```ts
// Proposed TypeScript shape — not an existing Dedalus SDK API.
type Checkpoint = {
  id: string;
  machineId: string;
  taskLabel: string;
  status: "creating" | "ready" | "failed" | "expired";
  createdAt: string;
  metadata: Record<string, string>; // small, non-sensitive diagnostic fields
  recoveryNotes?: string;
  warnings: string[];
};

const checkpoint = await machine.checkpoints.create({
  taskLabel: "apply-auth-middleware",
  metadata: {
    workflow: "repo-maintenance",
    stage: "tests-passed"
  },
  recoveryNotes:
    "Review the test report, then continue from the deployment gate."
});

const latest = await machine.checkpoints.latest();
```

### Example status response

```json
{
  "id": "cp_01...",
  "status": "ready",
  "taskLabel": "apply-auth-middleware",
  "warnings": [
    "External side effects are not verified by this checkpoint."
  ],
  "recommendedAction": "inspect_then_resume"
}
```

## 5. Key flows

### A. First checkpoint

1. Developer creates or selects a persistent machine.
2. Developer runs a small multi-step task.
3. SDK prompts for a task label and validates metadata size and keys.
4. The system creates the checkpoint and shows status.
5. The developer receives a stable ID and a next-step link.

**Success:** The developer understands what was saved, what was not saved, and how to retrieve it.

### B. Recovery after interruption

1. Developer opens the task or machine view.
2. The product shows the latest checkpoint, its status, warnings, and recovery notes.
3. Developer inspects artifacts/logs and selects a recovery path.
4. The product emits an event and preserves the decision history.

**Success:** The developer reaches a deliberate recovery decision without searching scattered logs or guessing the state.

### C. Handoff

1. A teammate or service receives a checkpoint ID.
2. They see the minimum safe context: task label, machine link, current status, warnings, and recovery notes.
3. They continue only after reviewing the warnings.

**Success:** Task continuity does not depend on one person’s memory.

## 6. Non-goals for v0

- Designing or replacing the customer’s agent framework
- Promising transactional rollback for arbitrary external systems
- Capturing unbounded or secret-bearing metadata
- Automatically resuming every task without a developer decision
- Building a full visual workflow editor

These exclusions keep v0 composable and honest about the boundary between compute persistence and workflow semantics.

## 7. Guardrails

| Risk | v0 guardrail |
| --- | --- |
| Secrets in metadata | Allow-list short keys; document redaction; reject oversized payloads |
| Duplicate writes after resume | Persistent warning and explicit recovery modes |
| Stale checkpoints | Status/expiry fields and a clear retention policy |
| Misleading “success” | Separate checkpoint creation from task-completion state |
| API lock-in | Simple, portable identifiers and event hooks |

## 8. Open questions

1. Which state belongs in a platform checkpoint versus an agent’s own store?
2. Should a checkpoint point to an immutable machine snapshot, a filesystem state, or a higher-level task record?
3. What is the smallest metadata schema that is useful across coding, research, and operational agents?
4. Which recovery actions can safely be automated?
5. How should retention, pricing, and compliance shape the experience?

## 9. Launch gate

Do not launch because the API exists. Launch only when a small set of target developers can complete a real interrupted-workflow recovery exercise, understand the caveats, and report that the workflow is preferable to their current manual process.