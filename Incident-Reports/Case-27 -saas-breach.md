# Case 27 — SaaS Account Takeover & Data Exfiltration

## Incident Type
SaaS Account Compromise (Cloud Identity Breach)

---

## Summary
SOC detected abnormal SaaS activity including foreign logins, unauthorized OAuth integration, and large-scale data downloads. Investigation confirmed account takeover and data exfiltration.

---

## Detection Source
- SaaS Audit Logs
- Authentication Logs
- File Access Logs
- OAuth / Integration Logs

---

## Key Indicators
- Login from unusual country/device
- Impossible travel pattern
- New OAuth application authorized
- Mass file downloads (50GB+)
- Password resets and security changes
- User reported suspicious activity

---

## Investigation Actions
- Reviewed authentication history (IP, device, MFA events)
- Checked file download/export logs
- Inspected admin and privilege changes
- Audited OAuth integrations and tokens
- Traced attacker entry point (phishing/credential theft)
- Scoped affected users and exposed data

---

## Findings
- Compromised valid cloud account
- Malicious OAuth app enabled persistence
- Large data export confirmed
- Multiple sensitive files accessed

---

## MITRE ATT&CK Mapping

| Tactic | Technique |
|-------|-----------|
| Initial Access | T1078.004 – Valid Cloud Account |
| Persistence | T1098 – Account Manipulation |
| Collection | T1213 – Data from Cloud Storage |
| Exfiltration | T1567 – Exfiltration via Cloud Service |
| Defense Evasion | T1562 – Disable Security Controls |

---

## Containment
- Disabled affected accounts
- Revoked all sessions/tokens
- Removed malicious OAuth apps
- Forced password reset + MFA
- Blocked suspicious IPs

---

## Root Cause
Credential theft (likely phishing) combined with OAuth persistence abuse.

---

## Impact
Confirmed data exfiltration from cloud storage.

Severity: High
