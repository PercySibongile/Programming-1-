print("====PASSWORD CRACKER SIMULATOR====")
target = input("Enter a password for the simulator: ")
common_passwords = [
    "1234",
    "password",
    "admin",
    "12345678",
    "qwerk",
    "letion",
    "python"
]
attempts = 0
found = False
for password in common_passwords:
    attempts = attempts + 1
    print("Trying:", password)
    if password == target:
        print("\nPASSWORD FOUND!")
        print("Password:", password)
        print("Attempts:", attempts)
        found = True
        break
if found == False:
    print("\nPassword was not found.")
    print("Attempts:", attempts)

