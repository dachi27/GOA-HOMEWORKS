number1 = int(input("enter the first number here: "))
operation = input("enter the operation here: ")
number2 = int(input("enter the second number here: "))
if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
else:
    print("wrong operation")