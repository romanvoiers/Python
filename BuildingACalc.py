num1 = input("What is the first number? ")
num2 = input("What is the second number? ")
operation = input("What mathematical operation you will be using? +,-,/ or *?: ")

if operation == "+":
    result = int(num1) + int(num2)
    print(result)

if operation == "-":
    result = int(num1) - int(num2)
    print(result)

if operation == "/":
    result = float(num1) / float(num2)
    print(result)

if operation == "*":
    result = int(num1) * int(num2)
    print(result)
