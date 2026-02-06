# Account Takeover Response Playbook

## Purpose
Respond to suspected account compromise across SaaS, email, VPN, and cloud identity (IAM/SSO).

## Trigger / Detection Signals
- Impossible travel / anomalous geo-location
- Multiple failed logins followed by success
- New device/browser fingerprint
- MFA push fatigue / unusual MFA prompts
- Password reset or email/phone change not initiated by user
- New OAuth app consent / new API token created
- Privilege escalation (role change, admin grant)

## Initial Triage (First 15 Minutes)
- Confirm user identity via trusted channel (not email from the account)
- Identify impacted account type: SaaS / Email / SSO / Cloud IAM
- Determine scope: single user vs multiple users / org-wide indicators
- Preserve evidence: export/auth logs and alert details

## Investigation Checklist
### Authentication
- Review login history (time, geo, IP, device, user agent)
- Check MFA events (push approvals, bypass, changes)
- Identify source IPs and correlate with other accounts

### Account Changes
- Review password resets, recovery method changes, forwarding rules
- Check role/permission changes and admin grants
- Review creation of tokens, app passwords, API keys

### Activity Review
- Look for abnormal actions:
  - bulk downloads/export
  - mailbox searches and rule creation
  - creation of new users/invites
  - access to sensitive folders/projects
- Identify data accessed and time window of exposure

## Containment
- Disable account or force sign-out everywhere (revoke sessions/tokens)
- Reset password using secure workflow
- Enforce MFA (prefer phishing-resistant where possible)
- Remove malicious OAuth apps / revoke third-party consents
- Remove forwarding rules, filters, recovery changes
- Block suspicious IPs/ASNs where feasible
- For admin/privileged accounts: rotate keys, revoke API tokens

## Recovery
- Restore legitimate settings (roles, rules, recovery options)
- Verify no persistence remains (tokens, apps, secondary accounts)
- Require re-enrollment of MFA if compromise suspected
- Review related accounts for reuse of password or similar indicators
- Monitor for re-compromise (24–72 hours heightened monitoring)

## Communication
- Notify affected user and relevant stakeholders
- If sensitive data accessed: follow internal escalation and legal/privacy process

## MITRE ATT&CK Mapping
- T1078 – Valid Accounts
- T1098 – Account Manipulation
- T1114 – Email Collection (if mailbox accessed)
- T1213 – Data from Information Repositories / Cloud Storage (if bulk download)

## Output / Artifacts
- Incident timeline (key actions and timestamps)
- IOC list (IPs, user agents, OAuth app IDs, token IDs)
- Confirmed impacted data/resources
- Lessons learned + recommended control improvements
