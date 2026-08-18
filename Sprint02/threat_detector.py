print("====CYBER THREAT DETECTOR====")
message = input("Enter a message to scan: ").lower()
threats = ["virus", "malware", "phishing", "hack", "ransomware"]
detected = []
for threat in threats:
    if threat in message:
        detected.append(threat)
print("\n====SCAN COMPLETE====")
if len(detected) > 0:
    print("WARNING: Suspicious keywords detected!")
    for threat in detected:
        print("-", threat)
else:
    print("No suspicious keywords detected.")