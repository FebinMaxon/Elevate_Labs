Task 4: Firewall Setup and Traffic Filtering
Project Overview
The objective of this task was to install, configure, and test a firewall on a Linux system to manage network traffic security. Using UFW (Uncomplicated Firewall) on Kali GNU/Linux 2025.4, I implemented specific rules to block insecure protocols while maintaining secure remote access.
+1

Technical Implementation
1. Installation and Initialization
The firewall was installed using the standard Debian package manager.


Command: sudo apt update && sudo apt install ufw -y.


Activation: The service was enabled to start automatically on system boot.
+1

2. Configuration Rules
I configured the firewall to follow the principle of least privilege by explicitly defining allowed and denied traffic:
+2


Blocked Insecure Traffic (Port 23): Inbound Telnet traffic was blocked due to its lack of encryption.


Command: sudo ufw deny 23/tcp.


Allowed Secure Traffic (Port 22): SSH access was explicitly permitted to allow for secure remote administration.


Command: sudo ufw allow 22/tcp.

3. Testing and Verification
To ensure the rules were functioning correctly, I performed the following verification steps:


Status Check: Verified the active ruleset using sudo ufw status.
+1


Connection Testing: Used Netcat (nc) to test the blocked Telnet port.


Result: Connection refused, confirming the firewall successfully dropped the traffic

Conclusion
This task demonstrates the importance of a firewall as a primary security control. By monitoring and filtering traffic based on port numbers and protocols, I successfully reduced the system's attack surface while maintaining necessary functionality.