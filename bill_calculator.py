# Simple bill calculator

item_price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity: "))

total = item_price * quantity

print(f"{quantity} items at {item_price:.2f} each = {total:.2f}")
