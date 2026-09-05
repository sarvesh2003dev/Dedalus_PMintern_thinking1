# Persistence Exercise

A minimal, real exercise for the public Dedalus Machines Python SDK.

It writes a small task note in one headless execution and retrieves that same note in a later execution on the same Machine. It is intended to produce a dated learning-log entry—not to simulate a production benchmark.

## Prerequisites

- A Dedalus API key with permission to use Machines
- Python 3.10+
- A deliberate choice about whether to create a new Machine (which may incur cost)

## Run

```bash
pip install -r prototype/requirements.txt
export DEDALUS_API_KEY=<your-key>
python prototype/run_persistence_exercise.py --create-machine
```

Or use a Machine you already created:

```bash
python prototype/run_persistence_exercise.py --machine-id dm-<id>
```

The script prints the Machine ID and does **not** delete it automatically. After recording your result, use the official lifecycle instructions to retrieve its revision and delete the Machine deliberately.

## What to record

Add the following to the [learning log](../docs/04-learning-log.md):

- Date and public documentation consulted
- Whether the first and second execution outputs matched
- What persisted and what remained ambiguous
- Sanitized command/output evidence
- The Machine ID only if you are comfortable exposing it; never publish an API key
- Any change this exercise causes in the PRD

## Limitation

This confirms persistence across separate command executions on one Machine. It does not prove an official agent-checkpoint feature, transaction safety, automatic recovery, or persistence of arbitrary in-memory/external state.