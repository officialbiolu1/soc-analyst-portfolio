# Case 30 – Cloud IAM Abuse Investigation

## Incident Type
Suspicious Cloud Account Activity and Privilege Escalation

---

## Summary
Cloud audit logs identified a login from an unfamiliar geographic region associated with an administrative account. Investigation revealed MFA was disabled shortly before authentication, followed by privilege escalation through assignment of an administrative role.

---

## Detection Source
- Cloud Audit Logs
- IAM Activity Logs
- Authentication Logs

---

## Key Indicators
- Login from foreign IP address
- Location anomaly compared to baseline behavior
- MFA disabled prior to login
- Administrative role assignment
- Privilege escalation activity

---

## Investigation Actions
- Reviewed authentication history including source IP, device metadata, and geolocation
- Verified MFA state changes and timeline correlation
- Analyzed IAM role assignments and policy modifications
- Checked for API key creation and usage
- Investigated potential data access or abnormal download activity
- Assessed persistence mechanisms within IAM policies and roles

---

## Findings
- Account accessed from anomalous foreign IP
- MFA disabled shortly before login event
- New administrative privileges assigned post-authentication
- No confirmed data exfiltration
- Elevated risk of full environment compromise

---

## MITRE ATT&CK Mapping
- T1078 – Valid Accounts  
- T1098 – Account Manipulation  
- T1556 – Modify Authentication Process  

---

## Containment
- Disabled affected account
- Revoked active sessions and API keys
- Re-enabled MFA enforcement
- Reviewed and restricted IAM role permissions
- Increased monitoring for follow-on activity

---

## Impact
Temporary administrative privilege escalation with no confirmed data loss.

---

## Severity
High
