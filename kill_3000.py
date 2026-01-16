#!/usr/bin/env python3
"""Script to kill processes running on port 3000."""

import subprocess
import sys

# --------------------------------------------------------------
def get_pids_on_port(port):
    """Find process IDs using a specific port."""
    result = subprocess.run(
        ['lsof', '-ti', f':{port}'],
        capture_output=True,
        text=True
    )
    if result.returncode != 0 or not result.stdout.strip():
        return []
    return result.stdout.strip().split('\n')

# --------------------------------------------------------------
def get_process_name(pid):
    """Get the name of a process by its PID."""
    result = subprocess.run(
        ['ps', '-p', pid, '-o', 'comm='],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

# --------------------------------------------------------------
def kill_pid(pid):
    """Kill a process by its PID."""
    subprocess.run(['kill', '-9', pid])

# --------------------------------------------------------------
def kill_process_on_port(port):
    """Kill all processes running on the specified port."""
    try:
        pids = get_pids_on_port(port)
        if not pids:
            print(f"No process found on port {port}")
            return

        for pid in pids:
            process_name = get_process_name(pid)
            print(f"Found: {process_name} (PID: {pid}) on port {port}")
            kill_pid(pid)
            print(f"Killed process {pid}")

        print(f"\nKilled {len(pids)} process(es)")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

# --------------------------------------------------------------
if __name__ == "__main__":
    kill_process_on_port(3000)