# Windows Endpoint Monitoring — Sysmon Investigation

## Scenario
Performed host-based threat hunting using Windows Security Logs and Sysmon telemetry to identify suspicious process execution, persistence, and command-and-control behavior on a Windows endpoint.

---

## Data Sources
- Windows Security Logs
- Sysmon Telemetry

---

## Key Telemetry Reviewed
- Event ID 1 – Process Creation
- Event ID 3 – Network Connections
- Event ID 11 – File Creation
- Event ID 13 – Registry Changes
- Event ID 22 – DNS Queries
- Security Events 4624/4625 – Authentication

---

## Investigation Actions
- Reviewed failed and successful login activity
- Traced parent-child process chains
- Analyzed PowerShell execution history
- Inspected outbound network connections
- Checked registry and startup locations for persistence
- Correlated suspicious events across logs

---

## Findings
- winword.exe spawning powershell.exe (macro-based execution behavior)
- Repeated outbound connections to external hosts at regular intervals
- Suspicious processes executing from user temp directories
- Registry modifications consistent with persistence attempts

Behavior consistent with potential malware staging and command-and-control activity.

---

## Detection Opportunities
- Alert on Office → PowerShell child processes
- Alert on repeated beaconing network traffic
- Monitor execution from temp/user directories
- Flag abnormal registry persistence changes

---

## Outcome
Successfully identified malicious-like behavior using log analysis and Sysmon telemetry without relying on antivirus alerts.
