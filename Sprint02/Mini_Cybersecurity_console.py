print("=============================")
print("    CYBER SECURITY CONSOLE")
print("==============================")
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("\nACCES GRANTED")
    print("Welcome,", username)
    while True:
        print("\n==== SECURITY MENU ====")
        print("1. Scan message")
        print("2. Check password strength")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            message = input("Enter message to scan: ").lower()
            threats = ["virus", "malware", "phishing", "hack"]
            detected = []
            for threat in threats:
                if threat in message:
                    detected.append(threat)
            if len(detected) > 0:
                print("THREAT DETECTED!")
                for threat in detected:
                    print("-", threat)
            else:
                print("No threats detected.")
        if choice == "2":
            password_check = input("Enter password to test: ")
            if len(password_check) < 6:
                print("Weak password")
            elif len(password_check) < 10:
                print("Medium password")
            else:
                print("Strong password")
        elif choice == "3":
            print("Exiting Security console...")
            break
        else:
            print("Invalid option.")
    else:
        print("ACCESS DENIED")   
    
