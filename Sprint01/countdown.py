import time
print ("====COUNTDOWN====")
number = int(input("Enter a starting number: "))
while number > 0:
    print(number)
    time.sleep(1)
    number = number - 1
print("GO!")