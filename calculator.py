operator = input("Enter an Operator (+ - * /): ")
num1 = float(input("Enter the fisrt number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(result)
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print(f"{operator} is not a valid operartor")    