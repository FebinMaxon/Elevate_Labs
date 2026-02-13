Phishing Email Analysis Report
Student: Febin Maxon

Internship Task: Task 2 - Analyze a Phishing Email Sample

Objective: Identify and document phishing characteristics in a suspicious email to demonstrate email threat analysis skills and awareness of social engineering tactics.

1. Selected Phishing Sample
For this analysis, I used a sample simulating a security alert from Microsoft.

Email Content:

From: accounts-security@micros0ft-support.net

Subject: URGENT: Unusual sign-in activity for your account

Body: > Dear Valued Customer,

Our automated systems have detected an unusual sign-in attempt... you must click the link below to verify your identity:

http://secure-login-portal.xyz/verification/auth

Failure to do so within 24 hours will lead to permanent deactivation.


Gemini said
This Report.md is structured to meet all your internship requirements. It combines the manual analysis steps with the technical implementation of your Python risk-scoring tool.

Phishing Email Analysis Report
Student: Febin Maxon

Internship Task: Task 2 - Analyze a Phishing Email Sample

Objective: Identify and document phishing characteristics in a suspicious email to demonstrate email threat analysis skills and awareness of social engineering tactics.

1. Selected Phishing Sample
For this analysis, I used a sample simulating a security alert from Microsoft.

Email Content:

From: accounts-security@micros0ft-support.net

Subject: URGENT: Unusual sign-in activity for your account

Body: > Dear Valued Customer,

Our automated systems have detected an unusual sign-in attempt... you must click the link below to verify your identity:

http://secure-login-portal.xyz/verification/auth

Failure to do so within 24 hours will lead to permanent deactivation.

2. Identified Phishing Indicators

Sender Spoofing:The email uses a typosquatted domain micros0ft-support.net (using a '0' instead of 'o'). Legitimate Microsoft emails use @microsoft.com.

Urgent Language:"Used phrases like ""URGENT,"" ""immediately,"" and threatened ""permanent deactivation"" within a 24-hour window to induce panic."

Generic Greeting:"Addressed as ""Dear Valued Customer"" instead of using my actual name, which is a common trait of bulk phishing campaigns."

Mismatched/Suspicious URL:"The link points to a .xyz top-level domain. Upon inspection, this does not lead to an official Microsoft domain."

Header Discrepancies:"Analysis Note: Manual inspection of the Return-Path shows it does not match the From address, indicating typical spoofing."

3. Technical Implementation: Interactive Risk Analyzer
I developed a Python script to automate the detection of these traits. The script calculates a risk score based on the presence of the indicators mentioned above.

Code Logic:

High Risk (10+ points): Multiple indicators like urgent language + suspicious TLDs.

Medium Risk (4-9 points): Some indicators found (e.g., generic greeting + one link).

Low Risk (<4 points): Minimal suspicious traits found.

Test Run Results: When I pasted the phishing_sample.txt into the terminal, the script produced the following:

Result: HIGH RISK

Findings: Urgent language detected, generic greeting used, and high-risk TLD (.xyz) found.

4. Awareness of Phishing Tactics
Through this task, I have developed a better understanding of:

Social Engineering: How attackers use fear and time pressure to bypass critical thinking.

Technical Obfuscation: How typosquatting and deceptive URLs are used to trick users into visiting credential harvesting sites.

Defense-in-Depth: Why relying on both human intuition (manual inspection) and technical tools (automated scanners) is necessary for robust email security.

5. Conclusion
The analyzed email is a classic example of a credential harvesting attempt. By identifying the combination of technical flaws (spoofed domain) and psychological triggers (urgency), I was able to successfully classify this as a high-risk threat. This exercise has significantly improved my ability to perform primary email forensics.

Tools Used: Python 3.
Project Folder: Task-2-Phishing-Analysis
Script Name: Phishing_Analyzer.py