#!/usr/bin/env python3

import subprocess
import sys

def kill_process_on_port(port):
    try:
        # Find process using lsof
        result = subprocess.run(
            ['lsof', '-ti', f':{port}'],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0 or not result.stdout.strip():
            print(f"No process found on port {port}")
            return
        
        # Get PIDs
        pids = result.stdout.strip().split('\n')
        
        for pid in pids:
            # Get process name
            name_result = subprocess.run(
                ['ps', '-p', pid, '-o', 'comm='],
                capture_output=True,
                text=True
            )
            process_name = name_result.stdout.strip()
            
            print(f"Found process: {process_name} (PID: {pid}) on port {port}")
            
            # Kill the process
            subprocess.run(['kill', '-9', pid])
            print(f"Killed process {pid}")
        
        print(f"\nKilled {len(pids)} process(es)")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    kill_process_on_port(3000)

