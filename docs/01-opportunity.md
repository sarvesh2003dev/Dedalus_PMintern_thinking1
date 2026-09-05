# Opportunity: Make Long-Running Agent Work Recoverable

## Context

Persistent machines are an important primitive for agentic software: an agent can retain a filesystem and a running environment instead of rebuilding every dependency and artifact in a fresh ephemeral sandbox. Dedalus publicly positions Machines around that persistent-compute model.

A persistent machine alone does not make a long-running *task* recoverable. Developers still need to answer:

- Which task was this machine working on?
- What was the last safe boundary?
- Is it safe to resume, retry, or hand off?
- What changed since the prior checkpoint?
- Where should I look when a task stalls?

This proposal explores a product layer for those questions.

**Evidence boundary:** The workflow observations above are product hypotheses derived from public documentation and common developer-infrastructure patterns—not claims about Dedalus customers. The research plan tests them before any build is treated as validated.

## Who has the problem?

### 1. Agent application developer

They build a coding, research, data, or operations agent that may run for minutes or hours. They need confidence that a restart will not lose useful work or create duplicate side effects.

**Job to be done:** “When my agent is interrupted, help me resume the right task from a known-safe point without manually reconstructing its state.”

### 2. Platform engineer

They operate many agent runs and need an understandable way to inspect failures, determine what can be retried, and support teammates.

**Job to be done:** “When an agent run looks unhealthy, show me enough structured context to diagnose it and choose a safe recovery action.”

### 3. Technical product team

They want to adopt persistent compute but need a low-friction first success before committing production workloads.

**Job to be done:** “Help me prove a persistent workflow works for my use case in one short session.”

## Problem statement

For developers running multi-step agent tasks, machine persistence does not automatically provide **task continuity**. Without an explicit checkpoint contract, recovery can be manual, opaque, and inconsistent across teams.

The result is a trust gap: a developer may know the computer still exists, but not know whether the agent’s work is resumable, what state is safe, or what to do next.

## Product insight

The first valuable product is not a large agent framework. It is a narrow contract that makes a durable task legible:

```
task → checkpoint → observable status → resume / recover decision
```

The user should be able to create a named checkpoint at a meaningful boundary, attach non-sensitive diagnostic metadata, and later retrieve an actionable status and recovery option.

## Alternatives and trade-offs

| Alternative | Strength | Limitation |
| --- | --- | --- |
| Let developers save files manually | Flexible, no platform work | Inconsistent; no task identity or recovery guidance |
| Build a full orchestration framework | Broad control plane | Large surface area; risks competing with customer stacks |
| Add generic logs only | Fast to ship | Logs answer “what happened?” poorly when state must be recovered |
| **Proposed checkpoint contract** | Small, composable, observable | Requires precise safety and lifecycle design |

The checkpoint contract is the smallest bet that can improve trust without assuming how customers author their agents.

## Risks to test early

1. **State ambiguity:** A filesystem snapshot may not capture external side effects or in-memory context.
2. **Safety:** Metadata and artifacts may include secrets or regulated information.
3. **False confidence:** “Resume” must not imply idempotence when a task can duplicate writes.
4. **API complexity:** A design that requires a new framework will hurt adoption.
5. **Value threshold:** Developers may prefer their own orchestration layer; research must identify where a platform primitive is genuinely useful.

## Decision criteria

I would proceed only if early users can:

- reach a first durable run quickly,
- explain the difference between a machine and a task checkpoint,
- recover a representative interrupted workflow without manual forensics, and
- name a use case where the platform-level primitive saves meaningful work or time.

Otherwise, I would narrow the scope to better status visibility or document a recommended integration pattern rather than build a new API.

## Sources

- [Dedalus Machines public documentation](https://www.dedaluslabs.ai/beta/dedalus-machines)
- [Dedalus Product Manager Intern role](https://jobs.ashbyhq.com/dedalus-labs/ca4245ff-0dee-4f16-80ca-24912d72079c)

Last reviewed: 2026-09-05.