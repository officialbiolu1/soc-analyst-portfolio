# Case 29 – Malicious Office Macro Execution

## Incident Type
Phishing-Based Initial Access with PowerShell Execution

---

## Summary
Security monitoring detected Microsoft Word (winword.exe) spawning PowerShell with an encoded command. The execution chain indicated likely macro-enabled document abuse leading to remote script execution.

---

## Detection Source
- Sysmon Event ID 1 – Process Creation  
- Parent Process: winword.exe  
- Child Process: powershell.exe with -EncodedCommand  

---

## Key Indicators
- Office application spawning PowerShell
- Use of encoded PowerShell command
- Suspicious parent-child process relationship
- Potential remote script download behavior

---

## Investigation Actions
- Reviewed Sysmon Event ID 1 for process lineage
- Extracted and decoded Base64 command payload
- Analyzed outbound connections (Sysmon Event ID 3)
- Reviewed DNS queries (Sysmon Event ID 22)
- Checked file creation activity (Sysmon Event ID 11)
- Investigated registry locations for persistence artifacts

---

## Findings
- Encoded PowerShell payload executed from Office process
- Payload attempted remote script retrieval
- Activity consistent with phishing document macro abuse
- Elevated risk of follow-on compromise

---

## MITRE ATT&CK Mapping
- T1204 – User Execution  
- T1059.001 – PowerShell  
- T1027 – Obfuscated Files or Information  

---

## Containment
- Isolated affected endpoint
- Blocked command-and-control domain
- Removed persistence mechanisms
- Reset compromised user credentials

---

## Severity
High
