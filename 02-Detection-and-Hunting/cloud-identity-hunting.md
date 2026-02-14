# Cloud Identity & SaaS Account Hunting

---

## Scope

Hunting methodology for identifying suspicious authentication behavior, token abuse, privilege escalation, and identity compromise in SaaS and cloud environments.

---

## Log Sources

- Audit Logs  
- Sign-in Logs  
- Admin Activity Logs  

---

## Detection Use Cases

### Impossible Travel

Pattern:
- Login from geographically distant locations  
- Short time interval between sessions  

Hunting Approach:
- Compare login geolocation and timestamps  
- Identify impossible travel scenarios  
- Validate user activity legitimacy  

MITRE ATT&CK:
- T1078 – Valid Accounts  

---

### Suspicious OAuth / Application Consent

Pattern:
- New application registration  
- Admin consent granted  
- API token or access key creation  

Hunting Approach:
- Monitor OAuth app registrations  
- Review granted permissions  
- Identify excessive API scopes  
- Correlate token creation with login anomalies  

MITRE ATT&CK:
- T1098 – Account Manipulation  

---

### MFA Disablement Followed by Login

Pattern:
- MFA method removed or modified  
- Subsequent successful authentication  

Hunting Approach:
- Monitor MFA configuration changes  
- Correlate with login activity  
- Identify privilege escalation behavior  

MITRE ATT&CK:
- T1556 – Modify Authentication Process  

---

## Operational Coverage

This module supports detection and hunting for:

- Identity compromise  
- OAuth abuse and token persistence  
- Privilege escalation  
- Session hijacking indicators  
- Cloud account takeover activity  
