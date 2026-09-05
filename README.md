# Durable-Agent Checkpoints

> An independent product case study for persistent agent infrastructure. This is **not** an official Dedalus Labs product or roadmap.

[Read the original brief (PDF)](Dedalus_PM_Brief_v2.pdf) · [Opportunity](docs/01-opportunity.md) · [PRD](docs/02-prd.md) · [Metrics & experiments](docs/03-metrics-and-experiments.md) · [Learning log](docs/04-learning-log.md) · [90-day plan](docs/05-90-day-plan.md) · [Runnable persistence exercise](prototype/README.md)

## The one-minute version

Dedalus Machines makes it possible to give an AI agent a persistent Linux computer rather than a disposable sandbox. That unlocks a useful question: when a multi-step agent pauses, fails, or hands work to another process, how should its **task state** survive—not just its machine?

This case study proposes a thin **durable-agent checkpoint contract**: a developer can name a checkpoint, attach safe metadata, observe its progress, and resume or recover a task without rebuilding the agent's working context from scratch.

The proposal focuses on developer activation and reliable recovery. It deliberately avoids inventing customer interviews, usage numbers, benchmarks, or shipping commitments.

## Why this is relevant

Dedalus describes Machines as persistent compute for agents, with an API for running work in isolated Linux microVMs. The company’s Product Manager Intern role asks for people who can understand users, make trade-offs, ship with engineering, and improve developer experience. This repository is my attempt to show that work in public.

- Product context: [Dedalus Machines](https://www.dedaluslabs.ai/beta/dedalus-machines)
- Role context: [Product Manager Intern](https://jobs.ashbyhq.com/dedalus-labs/ca4245ff-0dee-4f16-80ca-24912d72079c)
- Company context: [Dedalus careers](https://www.dedaluslabs.ai/careers)

## What is in this repository

| Artifact | What it demonstrates |
| --- | --- |
| [Opportunity](docs/01-opportunity.md) | User problem, assumptions, alternatives, and the product boundary |
| [PRD](docs/02-prd.md) | A scoped v0 proposal, flows, proposed API shape, and non-goals |
| [Metrics & experiments](docs/03-metrics-and-experiments.md) | Clear activation and reliability metrics, plus falsifiable tests |
| [Learning log](docs/04-learning-log.md) | A reproducible plan to learn the product hands-on and record real observations |
| [90-day plan](docs/05-90-day-plan.md) | How I would sequence discovery, build, and launch work in an internship |
| [Persistence exercise](prototype/README.md) | A runnable public-SDK exercise that verifies an artifact persists across separate executions |

## Product thesis

**If developers can safely checkpoint and inspect agent task state at meaningful boundaries, they will recover from interrupted long-running work faster and trust persistent compute for higher-value workflows.**

A checkpoint should be a product primitive, not a loose collection of files. It needs a stable identity, an explicit lifecycle, guardrails around sensitive data, observable events, and a recovery path that is understandable at 2 a.m.

## Run one real learning exercise

The [persistence exercise](prototype/README.md) uses Dedalus’s public Python SDK to write and retrieve a small task artifact across separate executions on one Machine.

It requires your own API key. Running with `--create-machine` provisions infrastructure and may incur cost, so read the instructions and clean up the Machine when finished. Do not publish your key or any customer data.

## Scope discipline

This is a **proposal**, not a claim that I have access to Dedalus’s internal systems or data.

- Facts about Dedalus are linked to public sources.
- Product interfaces below are illustrative and clearly marked as proposed.
- The experiment plan contains no fabricated results. Results will be added only after I run and document them.
- I do not assume a particular internal architecture or customer segment without validation.

## Next evidence I will add

1. Complete the public Machines quickstart and publish observations in the learning log.
2. Run the persistence/recovery exercise and record the setup, command, result, and limitations.
3. Conduct a handful of consented developer conversations; publish only anonymized themes and the exact research questions.
4. Revise the proposal when the evidence disagrees with the thesis.

## Author

Sarvesh Tamse · [GitHub profile](https://github.com/sarvesh2003dev)

Feedback is welcome through [issues](../../issues).