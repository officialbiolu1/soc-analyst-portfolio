# Windows Endpoint Detection & Hunting  
Sysmon + Security Log Telemetry

---

## Scope

Detection logic developed to identify credential abuse, malicious execution chains, persistence mechanisms, and command-and-control behavior using Windows Security Logs and Sysmon telemetry.

---

## Log Sources

- Windows Security Log
- Sysmon Operational Log

---

## High-Value Event IDs

### Authentication Events
- 4624 – Successful Logon
- 4625 – Failed Logon
- 4672 – Special Privileges Assigned
- 4648 – Explicit Credential Logon

### Process & System Activity (Sysmon)
- 1 – Process Creation
- 3 – Network Connection
- 11 – File Creation
- 13 – Registry Modification
- 22 – DNS Query

---

## Detection Use Cases

### Brute Force with Successful Authentication

**Pattern**
- Multiple 4625 events from a single source IP
- Followed by Event ID 4624 (Logon Type 10)

**Detection Logic**
- Aggregate failed logons by source IP
- Apply threshold within defined timeframe
- Alert on fail-to-success correlation

**MITRE ATT&CK**
- T1110 – Brute Force  
- T1078 – Valid Accounts  

---

### Suspicious Parent-Child Execution

**Pattern**
- winword.exe → powershell.exe  
- excel.exe → cmd.exe  
- Browser → scripting engine

**Detection Logic**
- Monitor abnormal parent-child process chains
- Flag Office spawning scripting engines

**MITRE ATT&CK**
- T1059 – Command & Scripting Interpreter  

---

### Beaconing Behavior

**Pattern**
- Repeated outbound connections to same external IP
- Consistent interval timing

**Detection Logic**
- Monitor Sysmon Event ID 3
- Identify recurring external communication patterns

**MITRE ATT&CK**
- T1071 – Application Layer Protocol  

---

### Registry Persistence Monitoring

**Pattern**
- Modifications to:
  - Run keys
  - Services
  - Scheduled tasks

**Detection Logic**
- Monitor Sysmon Event ID 13
- Alert on changes to startup locations

**MITRE ATT&CK**
- T1547 – Boot or Logon Autostart Execution  

---

## Operational Coverage

This module covers detection engineering for:

- Credential attacks
- Malicious process execution
- Persistence establishment
- Command-and-control activity
