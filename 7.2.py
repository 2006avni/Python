tup = (1, 2, 3, 4, 2, 5, 3, 6, 3)
repeated_items = []
for item in tup:
    if tup.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)

print("Repeated items in tuple:",repeated_items)
