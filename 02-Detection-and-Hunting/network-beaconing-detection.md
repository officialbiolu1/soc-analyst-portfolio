# Network Beaconing Detection Strategy

---

## Scope

Behavioral detection methodology for identifying potential command-and-control (C2) communication based on traffic patterns rather than signature-based alerts.

---

## Detection Characteristics

- Repeated outbound connections to same external IP
- Consistent timing intervals between connections
- Low-volume periodic traffic
- DNS queries to low-reputation or newly registered domains

---

## Log Sources

- Firewall Logs  
- Proxy Logs  
- DNS Logs  
- Sysmon Event ID 3 (Network Connection)  
- Sysmon Event ID 22 (DNS Query)  

---

## Hunting Methodology

- Group outbound traffic by destination IP  
- Identify recurring connection intervals  
- Assess domain age and reputation  
- Correlate network activity with process creation telemetry  
- Investigate associated user sessions and endpoint behavior  

---

## MITRE ATT&CK Mapping

- T1071 – Application Layer Protocol  
- T1041 – Exfiltration Over C2 Channel  

---

## Operational Coverage

Supports detection of:

- Beaconing behavior  
- C2 communication patterns  
- Data staging or exfiltration activity  
- Malware maintaining persistence through external connectivity  
