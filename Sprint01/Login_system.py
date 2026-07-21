print ("===Simple Login System===")
correct_username = "admin"
correct_password = "2007"
attempts = 0
while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("\nLogin Successful!")
        print("Welcome,", username)
        break
    else:
        attempts = attempts + 1
        print("Incorrect username or password.")
        print("Attempts remaining:", 3 - attempts)
    if attempts == 3:
        print("\nAccount Locked!")
        print("Too many failed login attempts.")