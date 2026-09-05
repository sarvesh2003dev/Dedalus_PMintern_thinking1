#!/usr/bin/env python3
"""Run a transparent persistence exercise on a Dedalus Machine.

This script uses the public Dedalus Machines Python SDK flow. It demonstrates
that a file written in one execution remains available to a later execution on
the same machine. It does not implement, claim, or depend on an official
"checkpoint" feature.

Running with --create-machine provisions a machine in the configured account.
Use --machine-id to run the exercise on an existing machine instead. The script
never sends an API key to output, but it does print the machine ID so the owner
can clean up the resource deliberately after the exercise.
"""

from __future__ import annotations

import argparse
import os
import time
from typing import Any


DEFAULT_BASE_URL = "https://staging.dcs.dedaluslabs.ai"
TERMINAL_EXECUTION_STATES = {"succeeded", "failed"}


def wait_for_machine(client: Any, machine_id: str) -> Any:
    """Wait until a newly provisioned machine reports running."""
    while True:
        machine = client.machines.retrieve(machine_id=machine_id)
        if machine.status.phase == "running":
            return machine
        print(f"Machine phase: {machine.status.phase}; waiting...")
        time.sleep(1)


def run_command(client: Any, machine_id: str, command: list[str]) -> str:
    """Run one command and return stdout, raising on a failed execution."""
    execution = client.machines.executions.create(
        machine_id=machine_id,
        command=command,
    )
    while execution.status not in TERMINAL_EXECUTION_STATES:
        time.sleep(0.5)
        execution = client.machines.executions.retrieve(
            machine_id=machine_id,
            execution_id=execution.execution_id,
        )

    output = client.machines.executions.output(
        machine_id=machine_id,
        execution_id=execution.execution_id,
    )
    if execution.status != "succeeded":
        stderr = getattr(output, "stderr", "")
        raise RuntimeError(f"Command failed: {stderr}")
    return getattr(output, "stdout", "")


def run_exercise(client: Any, machine_id: str) -> None:
    """Write an agent-task note, then retrieve it in a separate execution."""
    create_note = [
        "/bin/bash",
        "-lc",
        "set -eu\n"
        "mkdir -p ~/.durable-agent-demo\n"
        "printf '%s\\n' '{\"task\": \"persistence-exercise\", "
        "\"boundary\": \"artifact-written\", "
        "\"note\": \"created-by-first-execution\"}' "
        "> ~/.durable-agent-demo/checkpoint.json\n"
        "cat ~/.durable-agent-demo/checkpoint.json",
    ]
    first_output = run_command(client, machine_id, create_note)
    print("First execution wrote:\n" + first_output)

    verify_note = [
        "/bin/bash",
        "-lc",
        "set -eu\n"
        "test -f ~/.durable-agent-demo/checkpoint.json\n"
        "cat ~/.durable-agent-demo/checkpoint.json",
    ]
    second_output = run_command(client, machine_id, verify_note)
    print("Second execution recovered:\n" + second_output)

    if first_output != second_output:
        raise RuntimeError(
            "The two outputs differ; inspect the machine and do not claim "
            "the persistence exercise succeeded."
        )
    print("Result: the recorded artifact was available in a later execution.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument(
        "--machine-id",
        help="Run against an existing Dedalus Machine ID.",
    )
    selection.add_argument(
        "--create-machine",
        action="store_true",
        help="Provision a small machine before running the exercise.",
    )
    parser.add_argument(
        "--base-url",
        default=os.environ.get("DEDALUS_BASE_URL", DEFAULT_BASE_URL),
        help="Dedalus API base URL (defaults to the public quickstart URL).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    api_key = os.environ.get("DEDALUS_API_KEY")
    if not api_key:
        raise SystemExit("Set DEDALUS_API_KEY before running this exercise.")

    try:
        from dedalus_sdk import Dedalus
    except ImportError as error:
        raise SystemExit(
            "Install the public SDK first: pip install dedalus-sdk"
        ) from error

    client = Dedalus(api_key=api_key, base_url=args.base_url)
    if args.create_machine:
        machine = client.machines.create(vcpu=1, memory_mib=1024, storage_gib=10)
        machine_id = machine.machine_id
        print(f"Created machine: {machine_id}")
        wait_for_machine(client, machine_id)
    else:
        machine_id = args.machine_id

    run_exercise(client, machine_id)
    print("\nCleanup reminder: machines can incur storage or compute cost.")
    print(
        "Use the public CLI/docs to retrieve the machine revision and delete "
        f"machine {machine_id} when you are finished."
    )


if __name__ == "__main__":
    main()
