VPN Implementation & Network Privacy Analysis
📖 Project Overview
This project explores the role of Virtual Private Networks (VPNs) in safeguarding digital privacy and securing communications over public networks. By implementing a secure tunnel using ProtonVPN, this project demonstrates how to effectively mask network identities, bypass ISP tracking, and defend against Man-in-the-Middle (MITM) attacks.

🎯 Objectives
Understand the core architecture of VPN tunneling.

Implement a professional-grade VPN client (ProtonVPN) on Windows.

Analyze the impact of encryption (AES-256) on data packets.

Verify privacy protection through IP masking and DNS leak testing.

🛠️ Tools Used
Client: ProtonVPN (Free Tier)

OS: Windows 10/11

Verification Tools: DNSLeakTest.com, IPChicken, CMD (ipconfig/curl)

Protocols Tested: WireGuard, OpenVPN

🚀 Implementation Steps
1. Setup & Installation
Created a verified account on the ProtonVPN platform.

Downloaded and installed the Windows GUI client.

Configured "Smart Protocol" to allow the client to select the best tunneling method.

2. Establishing the Tunnel
Authenticated via the secure login portal.

Used the Quick Connect feature to link to a secure server in [Insert Country, e.g., Netherlands].

Enabled the Kill Switch to prevent accidental data leaks during connection drops.

3. Verification
IP Check: Confirmed that the public IP address changed from the local ISP address to the VPN server's IP.

DNS Leak Test: Verified that all DNS queries were routed through the VPN tunnel, preventing ISP "snooping."

📸 Deliverables
Connection Steps: Screenshots detailing the authentication and server selection process.

Status Report: Evidence of the "Connected" state and the newly assigned virtual IP address.

Technical Summary: A detailed breakdown of the encryption and tunneling protocols used.

📑 Key Concepts
VPN Tunneling: The process of encapsulating private data packets inside a public, encrypted header.

AES-256 Encryption: The cryptographic standard used to ensure that even if data is intercepted, it remains unreadable.

No-Logs Policy: Ensures that the VPN provider does not store browsing history or connection timestamps.

🛡️ Security Analysis
By routing traffic through an encrypted tunnel, we achieved:

Anonymity: Websites see the VPN IP, not our actual hardware identity.

Integrity: Data cannot be modified by third parties in transit.

Bypassing Geo-Blocks: Accessing content restricted by geographic location.

🤝 Credits
Project Lead: [Your Name]

Tooling Provider: Proton Technologies AG

Research Material: GitHub Documentation & Network Security Fundamentals