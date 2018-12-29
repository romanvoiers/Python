# can be used as an inventory system

friends = ["Mike", "John", "Don", "Roman", "Maria"]
print(friends[1])  # Shows a specific element by index. Goes by 0,1,2....
print("I hate " + friends[2])
print(friends[-1])  # Negatives pick from the back of the list
print(friends[3:5])  # Takes a range. First number inclusive second exclusive
friends[0] = "Lola"
print(friends[0])


items = ["potion", "Sword", "Armor"]
print(items)
print(" You dropped the potion")
del(items[0])  # Deletes an item out of the list
print(items)

