cust_num = input("Enter customer number: ")
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 1.0
elif units <= 300:
    bill = 100 + (units - 100) * 1.25
elif units <= 500:
    bill = 350 + (units - 300) * 1.50
else:
    bill = 650 + (units - 500) * 1.75

print("\nElectric Bill")
print("Customer Number:", cust_num)
print("Units Consumed:", units)
print(f"Amount to be paid: Rs. {bill:.2f}")