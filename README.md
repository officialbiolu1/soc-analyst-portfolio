# SOC Analyst Portfolio – Bioluwaosi Bajomo

Security Operations and Threat Detection repository containing structured incident investigations, behavioral hunting methodologies, detection engineering logic, and automation across Windows, Linux, and cloud environments.

---

# Repository Architecture

## 01 – Incident Reports

Structured end-to-end investigations including:

- Zero-Day Suspicion
- Cloud Ransomware
- SaaS Account Breach
- RDP Brute-Force Detection
- Malicious Office Macro Execution
- Cloud IAM Abuse Investigation

Each case contains:
- Alert source
- Investigation methodology
- Log correlation
- MITRE ATT&CK mapping
- Root cause analysis
- Containment actions
- Impact assessment

---

## 02 – Detection and Hunting

Behavior-driven detection development across environments.

### Windows Endpoint Monitoring
- Authentication analysis (4624 / 4625)
- Process creation monitoring (4688)
- Sysmon process correlation
- Office → PowerShell execution analysis
- Registry persistence detection

### Linux Authentication Monitoring
- SSH anomaly analysis
- Failed login pattern detection
- Privilege escalation investigation
- Command auditing

### Cloud Identity Monitoring
- IAM misuse detection
- Suspicious API activity
- Geolocation anomaly analysis
- Privilege escalation monitoring

### Network Beaconing Detection
- Repeated outbound connection analysis
- Command-and-control pattern identification
- Temporal traffic correlation

---

## 03 – Detection Rules (Sigma)

Custom detection logic developed for:

- Suspicious PowerShell Encoded Command
- RDP Brute-Force Detection
- Office Spawning PowerShell

Each rule includes:
- Logsource definition
- Detection logic
- MITRE ATT&CK mapping
- False positive considerations

---

## 04 – Playbooks

Operational response workflows for:

- Account Takeover
- RDP Brute-Force

Each playbook defines:
- Triage actions
- Investigation workflow
- Containment procedures
- Escalation criteria

---

## 05 – Automation Scripts

Log analysis utilities:

- failed_login_counter.sh
- suspicious_parent_child_parser.py

Designed to support rapid identification of authentication abuse and suspicious parent-child process execution.

---

## 06 – Cheatsheets

Operational reference material:

- Windows Event ID reference
- Authentication investigation quick reference

---

## 07 – Screenshots

Supporting investigation artifacts from endpoint, Linux, and cloud log analysis.

---

# Core Competencies

- Authentication anomaly detection
- Endpoint compromise analysis
- Ransomware investigation
- Cloud IAM abuse detection
- MITRE ATT&CK alignment
- Log correlation and timeline reconstruction
- Detection rule development
- Behavioral threat hunting
- SOC response workflow design
- Automation-assisted triage

---

Repository updated as detection coverage expands.
