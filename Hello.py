#learning variable
print("===Simple Calculator===".upper())
print("Enter first number: ")
num1 = float(input())
print("Enter second number: ")
num2 = float(input())
print("Enter operation (+, -, *, /): ")
operation = input()
if operation == "+":
    result = num1 + num2
    print("The answer is: ", result)
elif operation == "-":
    result = num1 - num2
    print("The answer is: ", result)
elif operation == "*":
    result = num1 * num2
    print("The answer is: ", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("The answer is: ", result)       
    else:
        print("Error: Division by 0 is not allowed.")

else:
    print("Invalid operation. Please enter a valid operation (+, -, *, /).")
    exit()


