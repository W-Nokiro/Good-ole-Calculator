
print("Welcome To The Good Ole Calculator")
x = 1
while x < 100:
    try:
        num1 = float(input("First number: "))
        operation = input("Calculation to do (only \"*\", \"/\", \"+\", \"-\"):")
        if operation == "+" or operation == "-" or operation == "*" or operation == "/":
           num2 = float(input("Second Number: "))
           x += 100
        elif x >= 2:
            print("Are you sure that your operation is in the list?")

        else:
            num2 = 1.0
            x += 1
            print("Unavailable operation")
    except ValueError as err:
        print("Please enter a valid number \n   err code:")
        print(err)
try:
    resultConv = None
    result = None
    if operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    elif operation == "+":
        result = num1 + num2
    elif operation == "-":
       result = num1 - num2
    resultConv = int(result)
    if result == resultConv:
        print(f"Result: {resultConv}")
    elif result != resultConv:
        print(f"Result: {result}")
except ZeroDivisionError as err:
    print("*bell rings* shame, shame... \n err code:")
    print(err)