import random
random_number = random.randint(1, 10)
lucky_number = int(input("Enter your lucky number (1-10): "))
if lucky_number == random_number:
    print("Today is your lucky day! ")
else:
    print("Better luck next time! ")
print ("Random number was:", random_number)