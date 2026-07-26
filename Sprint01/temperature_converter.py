print("===Temprature Converter===")
print("1. Celsius to Farenheit")
print("2. Frenheit to Celsius")
choice = int(input("Choose an option (1 or 2): "))
if choice == 1:
    celsius = float(input("Enter temperature in celsius: "))
    farenheit = (celsius * 9 / 5) + 32
    print("\n Temperature in Farenheit:", farenheit)
elif choice == 2:
    farenheit = float(input("Enter temperature in farenheit: "))
    celsius = (farenheit - 32) * 5 / 9
    print("\n Temperature in Celsius:", round(celsius, 2))
else:
    print("Invalid choice.")