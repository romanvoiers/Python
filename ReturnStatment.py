def cube(num):
    return num * num * num  # Returns the answer after the parameter has been passed in.


print(cube(2))  # Passing in a parameter, then printing out the answer


def square(num2):
    return num2 * num2
    print("This will not print because return breaks out of the function")


result = square(2)
print(result)
