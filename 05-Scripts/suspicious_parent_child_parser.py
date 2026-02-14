#!/usr/bin/env python3

"""
Purpose:
Detect suspicious parent-child process relationships in log files
where Microsoft Office spawns PowerShell.
"""

import sys

if len(sys.argv) != 2:
    print("Usage: python suspicious_parent_child_parser.py <logfile>")
    sys.exit(1)

logfile = sys.argv[1]

try:
    with open(logfile, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line_lower = line.lower()
            if "winword.exe" in line_lower and "powershell.exe" in line_lower:
                print("[ALERT] Suspicious Office -> PowerShell execution detected:")
                print(line.strip())
except FileNotFoundError:
    print(f"Error: File '{logfile}' not found.")
    sys.exit(1)
