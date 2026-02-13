import re

def analyze_email():
    print("--- Phishing Risk Analyzer ---")
    print("Paste your email content below. (Press Enter then Ctrl+D or Ctrl+Z to finish):")
    
    # Allows for pasting multi-line emails from the terminal
    try:
        lines = []
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        email_content = "\n".join(lines)

    if not email_content.strip():
        print("No content provided.")
        return

    # 1. Scoring Logic
    risk_score = 0
    indicators = []

    # Check for Urgency
    urgency_patterns = ["urgent", "suspended", "immediately", "24 hours", "action required", "deactivation"]
    found_urgency = [word for word in urgency_patterns if word in email_content.lower()]
    if found_urgency:
        risk_score += len(found_urgency) * 2
        indicators.append(f"Urgent language detected: {', '.join(found_urgency)}")

    # Check for Generic Greetings
    greetings = ["dear customer", "dear user", "valued member", "dear account holder"]
    if any(greet in email_content.lower() for greet in greetings):
        risk_score += 3
        indicators.append("Generic greeting used instead of your name.")

    # Check for Suspicious Links
    urls = re.findall(r'(https?://[^\s]+)', email_content)
    if urls:
        risk_score += len(urls) * 2
        indicators.append(f"Found {len(urls)} link(s) for inspection.")
        if any(tld in "".join(urls) for tld in [".xyz", ".top", ".buzz", ".tk"]):
            risk_score += 5
            indicators.append("High-risk Top Level Domain (TLD) detected in links.")

    # 2. Determine Risk Level
    if risk_score >= 10:
        risk_level = "HIGH"
    elif 4 <= risk_score < 10:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    # 3. Final Output
    print("\n" + "="*30)
    print(f"RESULT: {risk_level} RISK")
    print("="*30)
    
    print("\nFindings:")
    for ind in indicators:
        print(f"- {ind}")

    print("\n--- Phishing Awareness Tips ---")
    print("1. Hover before clicking: Always check the actual destination URL.")
    print("2. Verify the sender: Check if the email address matches the company's official domain.")
    print("3. Never share credentials: Real companies will not ask for passwords via email.")
    print("4. Avoid urgency: If an email creates panic, it is likely a scam.")

if __name__ == "__main__":
    analyze_email()