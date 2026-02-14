# RDP Brute Force Response Playbook

## Purpose
Provide structured response actions for suspected RDP brute force activity resulting in repeated failed logon attempts and potential credential compromise.

---

## Detection Triggers
- High volume of Event ID 4625 (Failed Logon)
- Logon Type 10 (Remote Interactive)
- Multiple attempts from single external IP
- Successful Event ID 4624 following failures

---

## Initial Validation
- Confirm spike in 4625 events within defined timeframe
- Verify Logon Type 10
- Identify source IP address
- Check IP reputation (threat intel / blacklist)
- Confirm whether successful authentication occurred

---

## Impact Assessment
- Identify targeted user accounts
- Determine if successful login occurred
- Review post-authentication activity:
  - Process creation (4688 / Sysmon EID 1)
  - Privilege escalation attempts
  - Lateral movement indicators
- Check for new user creation (Event ID 4720)
- Determine exposure of sensitive systems

---

## Containment Actions
- Disable or lock compromised account
- Force credential reset
- Revoke active sessions
- Block malicious IP at firewall or perimeter device
- Enforce or validate MFA configuration

---

## Recovery
- Monitor authentication logs for recurrence
- Review RDP exposure and network segmentation
- Confirm no persistence mechanisms were established
- Notify affected user and document actions taken

---

## Preventive Controls
- Enforce account lockout policies
- Require MFA for RDP access
- Restrict RDP exposure to VPN-only access
- Strengthen password complexity requirements
