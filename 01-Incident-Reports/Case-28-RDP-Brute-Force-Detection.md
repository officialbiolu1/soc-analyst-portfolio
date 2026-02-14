# Case 28 – RDP Brute Force Detection

## Incident Type
Credential Brute Force Leading to Successful Remote Access

---

## Summary
Security monitoring identified 50+ failed RDP login attempts (Event ID 4625) from a single external IP address, followed by a successful remote interactive login (Event ID 4624, Logon Type 10). The pattern indicated brute-force activity resulting in credential compromise.

---

## Detection Source
- Windows Security Event Logs
- Event ID 4625 – Failed Logon
- Event ID 4624 – Successful Logon
- Event ID 4688 – Process Creation
- Sysmon Event ID 1 – Process Creation

---

## Key Indicators
- High volume of failed RDP logons from one external IP
- Successful login immediately following failures
- Logon Type 10 (Remote Interactive)
- Same target account across attempts
- Temporal correlation between failures and success

---

## Investigation Actions
- Filtered and correlated Event IDs 4625 and 4624
- Verified Logon Type and source IP consistency
- Confirmed successful authentication following brute-force pattern
- Reviewed post-authentication activity for:
  - Privilege escalation
  - Suspicious process execution
  - New user creation (Event ID 4720)
  - Lateral movement attempts

---

## Findings
- Clear brute-force pattern resulting in valid account access
- Account likely compromised through repeated password attempts
- Elevated risk of post-compromise activity

---

## MITRE ATT&CK Mapping
- T1110 – Brute Force  
- T1078 – Valid Accounts  

---

## Containment
- Disabled compromised account
- Forced credential reset
- Revoked active sessions
- Blocked malicious source IP
- Reviewed environment for lateral movement

---

## Severity
High
