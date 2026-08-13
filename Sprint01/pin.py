correct_pin = "3456"
attempts = 3
while attempts > 0:
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("Access granted")
        break
    else:
        attempts= attempts - 1
        print("Wrong PIN")
        print("Attempts remaining:", attempts)
    if attempts ==0:
        print("Account locked")