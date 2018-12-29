num1 = input("What is the first number? ")
operation = input("What mathematical operation you will be using? +,-,/,*,** ?: ")
num2 = input("What is the second number? ")

if operation == "+":
    result = int(num1) + int(num2)
    print(str(num1) + " + " + (str(num2) + " = " + (str(result))))

if operation == "-":
    result = int(num1) - int(num2)
    print(str(num1) + " - " + (str(num2) + " = " + (str(result))))

if operation == "/":
    result = int(num1) / int(num2)
    print(str(num1) + " / " + (str(num2) + " = " + (str(result))))

if operation == "*":
    result = int(num1) * int(num2)
    print(str(num1) + " * " + (str(num2) + " = " + (str(result))))

if operation == "**":
    result = int(num1) ** int(num2)
    print(str(num1) + " ** " + (str(num2) + "= " + (str(result))))




