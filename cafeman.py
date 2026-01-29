import time

# Define the menu of the cafe
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Salad': 60,
    'Coffee': 70,
    'Tea': 20,
    'FrenchFries': 80
}

# Greet the user
print("Welcome to Python Cafe")
time.sleep(1)  # Adding a slight delay to make the experience feel more interactive

print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

# Initialize order total
order_total = 0

while True:
    # Take order input
    item = input("Enter the name of item you want to order: ")

    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order")
    else:
        print(f"Ordered item {item} is not available yet!")

    # Ask if the customer wants to add another item
    another_order = input("Do you want to add another item? (Yes/no): ").strip().lower()

    if another_order == "no":
        break  # Exit the loop if the user says "no"

# Display the total order amount
print(f"\nThe total amount of items to pay is Rs{order_total}")

time.sleep(1)  # Adding a small delay before ending for a smooth exit
