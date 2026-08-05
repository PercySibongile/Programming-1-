print("===== Shopping Receipt =====")
customer = input("Enter customer name: ")
item = input("Enter item name: ")
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity
print("\n ==== RECEIPT ====")
print("Customer:", customer)
print ("Item:", item)
print("Price:", price)
print("Quantity:", quantity)
print("Total Cost: KES", total)
if total >= 6000:
    discount = total * 0.10
    final_total = total - discount
    print("Discount: KES", discount)
    print("Amount to pay: KES", final_total)
else:
    print("No Discount")
    print("Amount to pay: KES", total)