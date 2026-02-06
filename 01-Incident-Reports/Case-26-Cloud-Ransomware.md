# Case 26 — Cloud Ransomware via IAM Credential Compromise

## Incident Type
Cloud Ransomware Attack (Identity-Based / IAM Abuse)

---

## Summary
Overnight, multiple AWS resources were encrypted and backups destroyed. Investigation revealed unauthorized IAM activity including creation of a privileged user, generation of access keys, mass storage modification, and snapshot deletion. Activity confirmed a ransomware attack executed through compromised cloud credentials and abuse of administrative permissions rather than endpoint malware.

---

## Detection Source
- AWS CloudTrail Logs
- IAM Audit Logs
- S3 Access Logs
- Billing/Usage Anomalies

---

## Key Indicators
- New IAM user created outside change window
- Administrator policy attached to newly created account
- Access keys generated for persistent API access
- EC2 stop/start actions across multiple instances
- Mass S3 object modification/renaming
- Snapshot and backup deletion
- Ransom note uploaded to S3
- Sudden spike in API and storage activity

---

## Investigation Actions
- Reviewed CloudTrail timeline for suspicious API calls
- Traced IAM privilege escalation events
- Identified attacker-created accounts and keys
- Correlated S3 object modifications and encryption activity
- Confirmed deletion of recovery snapshots
- Scoped affected instances, buckets, and data exposure
- Preserved logs for forensic analysis
- Assessed blast radius across environment

---

## Findings
- Unauthorized IAM user created with full administrative privileges
- Access keys used to automate destructive actions via AWS APIs
- EC2 instances disrupted and associated storage encrypted
- S3 data modified and locked
- Backups intentionally deleted to prevent recovery
- No malware observed on endpoints (cloud-only attack)

Attack executed entirely through valid credentials and cloud control plane abuse.

---

## MITRE ATT&CK Mapping

| Tactic | Technique |
|--------|------------|
| Initial Access | T1078.004 – Valid Cloud Accounts |
| Persistence | T1098 – Account Manipulation |
| Privilege Escalation | T1548.005 – Abuse Elevation Control Mechanism (IAM Policy Abuse) |
| Defense Evasion | T1562 – Impair Defenses |
| Impact | T1486 – Data Encrypted for Impact |
| Impact | T1490 – Inhibit System Recovery |

---

## Containment
- Disabled compromised IAM users
- Revoked all access keys and active sessions
- Removed malicious policies and roles
- Blocked suspicious IPs where applicable
- Preserved CloudTrail and audit logs
- Restored resources from clean backups
- Rotated all credentials and enforced MFA
- Reviewed and tightened IAM permissions

---

## Root Cause
Compromised or exposed AWS credentials combined with excessive IAM privileges and lack of strong monitoring/MFA controls.

---

## Impact
Encryption of compute and storage resources, loss of backups, and temporary service disruption.

Severity: Critical

