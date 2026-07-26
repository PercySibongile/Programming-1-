print("=====Password Strength Checker=====")
password = input("Enter a password: ")
length = len(password)
if length < 6:
    print("Weak Password")
elif length < 10:
    print("Medium Password")
else: 
    print("Strong Password")
print("Password Length:", length)