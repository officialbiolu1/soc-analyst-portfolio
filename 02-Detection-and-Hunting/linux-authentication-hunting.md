# Linux Authentication Hunting  
SSH & Privilege Escalation Monitoring

---

## Scope

Hunting methodology for identifying brute force attempts, unauthorized access, and privilege escalation activity within Linux authentication logs.

---

## Log Sources

- /var/log/auth.log  
- /var/log/secure  
- journalctl  

---

## Detection Use Cases

### SSH Brute Force Activity

Pattern:
- Multiple "Failed password" attempts  
- Same source IP  
- Occurring within short timeframe  

Hunting Approach:
- Aggregate failed authentication attempts by source IP  
- Identify threshold-based anomalies  
- Correlate with successful authentication events  

Example Command:
    grep "Failed password" /var/log/auth.log

MITRE ATT&CK:
- T1110 – Brute Force  

---

### Suspicious Successful Login Following Failures

Pattern:
- Repeated failed authentication attempts  
- Followed by "Accepted password"  

Hunting Approach:
- Identify fail-to-success sequences  
- Validate source IP consistency  
- Review post-authentication activity  

MITRE ATT&CK:
- T1078 – Valid Accounts  

---

### Privilege Escalation Monitoring

Pattern:
- Unexpected sudo usage  
- Multiple failed sudo attempts  
- Elevation from non-administrative accounts  

Hunting Approach:
- Review sudo command execution logs  
- Identify abnormal privilege usage patterns  
- Validate legitimacy of elevation events  

Example Command:
    grep "sudo" /var/log/auth.log

MITRE ATT&CK:
- T1548 – Abuse Elevation Control Mechanism  

---

## Operational Coverage

This module supports detection and hunting for:

- SSH brute force attempts  
- Credential compromise indicators  
- Unauthorized access patterns  
- Privilege escalation activity  
