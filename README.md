# Smart_Logs_Analyazer
I developed a Python-based Log Analyzer that parses system logs and detects suspicious activities like brute-force 
login attempts using regex pattern matching. It identifies malicious IPs and generates alerts, simulating real SOC monitoring.

🛡️ Smart Log Analyzer – SOC Monitoring Tool
📌 Description

I developed Smart Log Analyzer as a Python-based cybersecurity tool to analyze system logs and detect suspicious activities. 
This project simulates the role of a Security Operations Center (SOC) analyst by identifying potential threats such as brute-force 
login attempts and unusual access patterns. The goal is to understand log monitoring, threat detection, and basic incident analysis.

🚀 Features
I can analyze system log files 📄
I can detect multiple failed login attempts 🔐
I can identify potential brute-force attacks ⚠️
I can track suspicious IP addresses 🌐
I can generate alert-based reports 📊
🧠 Technologies Used
Python 🐍
Regular Expressions (Regex)
File Handling
Data Structures (Dictionary, defaultdict)
🔍 How It Works
Reads log file line by line
Uses pattern matching (Regex) to extract IP addresses
Counts failed login attempts per IP
Flags IPs exceeding threshold as suspicious
Displays alerts in a structured report
📊 Sample Output
=== Suspicious Activity Report ===

[ALERT] Possible brute-force attack from IP: 192.168.1.10 (Attempts: 3)
[INFO] IP: 192.168.1.20 (Attempts: 2)
💡 Key Learning Outcomes
Understanding of SOC analyst workflow
Hands-on experience in log analysis
Basic threat detection techniques
Practical use of Python in cybersecurity
🚀 Future Enhancements
Real-time log monitoring ⏱️
GUI dashboard using Tkinter 🖥️
Web-based interface using Flask 🌐
Integration with threat intelligence feeds 🔗
