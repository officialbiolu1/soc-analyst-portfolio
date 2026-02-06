# Case 25 — Zero-Day Suspicion & Behavioral Threat Hunt

## Incident Type
Suspicious Endpoint Behavior / Potential Zero-Day or Fileless Malware

---

## Summary
Users reported system slowdowns with no antivirus or signature-based detections. Threat hunting identified hidden PowerShell activity and periodic encrypted outbound connections to unknown external infrastructure. Behavioral indicators suggested possible fileless or custom malware operating without disk artifacts.

---

## Detection Source
- Network Traffic Logs
- Endpoint/EDR Telemetry
- Process Monitoring
- Memory Analysis

---

## Key Indicators
- Encrypted outbound HTTPS connections to unknown IP addresses
- Consistent 15-minute beaconing pattern
- Hidden long-running PowerShell process
- No associated file on disk
- Gradual memory growth over time
- No AV detections or known malware hashes

---

## Investigation Actions
- Correlated outbound connections across hosts
- Identified shared external C2 infrastructure
- Reviewed PowerShell parent-child process chains
- Inspected execution history and command artifacts
- Captured volatile memory from affected endpoints
- Performed memory forensics to locate injected code
- Queried threat intelligence for IP/domain reputation
- Conducted lateral hunt for similar behavior across environment

---

## Findings
- Suspicious PowerShell-based execution observed
- Memory-resident activity without disk artifacts
- Repeated external beaconing behavior
- Multiple systems affected
- No signature match to known malware

Activity consistent with potential fileless or custom malware (zero-day behavior).

---

## MITRE ATT&CK Mapping

| Tactic | Technique |
|--------|------------|
| Execution | T1059.001 – PowerShell |
| Command & Control | T1071.001 – Web Protocols (HTTPS) |
| Defense Evasion | T1564 – Hide Artifacts |
| Defense Evasion | T1620 – Reflective Code Loading |
| Persistence (Suspected) | T1053 – Scheduled Task/Job |

---

## Containment
- Isolated affected endpoints
- Blocked suspicious IP addresses
- Terminated suspicious PowerShell processes
- Captured memory for forensic preservation
- Reset credentials as precaution
- Increased monitoring and logging

---

## Root Cause
Undetermined. Behavioral evidence suggests possible custom or zero-day malware using fileless techniques.

---

## Impact
Potential unauthorized remote communication and risk of data exposure.

Severity: High

