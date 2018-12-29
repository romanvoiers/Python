lucky_numbers = [12, 31, 89, 19, 0]
friends = ["Lola", "Roman", "Risky", "Maria", "Jon", "Don"]

print(friends)


friends.append("Creed")  # .appends adds at the end of the list with another value
print(friends)

friends.insert(0, "Risky")  # .insert adds a new value where you want in the list
print(friends)

friends.remove("Lola")  # . remove removes specific element
print(friends)

friends.pop()  # .pop takes the last value of the list
print(friends)

print(friends.index("Risky"))  # finds the index of a chosen value

print(friends.count("Risky"))  # counts how many of the chosen value

friends.sort()  # Places the list in order
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()  # places list from highest to lowest
print(lucky_numbers)

friends2 = friends.copy()  # makes a copy of the list
print(friends2)

friends.extend(lucky_numbers)  # .extends puts lists together
print(friends)


friends.clear()  # .clear erases the whole list
print(friends)

