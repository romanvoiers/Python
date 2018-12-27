num1 = input("What is the first number? ")
num2 = input("What is the second number? ")
operation = input("What mathematical operation you will be using? +,-,/,*,** ?: ")

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


# By default python takes input as a string, you have to convert them into numbers using int.
# or use float for decimal numbers
