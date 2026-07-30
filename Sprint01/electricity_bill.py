print("======Electricity Bill Calculator======")
name = input(" Enter customer name: ")
units = float(input(" Enter electricity units used: "))
if units <= 100:
    bill = units * 15
elif units <= 300:
    bill = units * 20
else:
    bill = units * 25
print("\n======BILL======")
print("Customer:", name)
print("Units used:", units)
print("Total Bill: KES", bill)