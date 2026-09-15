print("Welcome to the Simple Calculator!")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("""
1. Addition
2. Subtraction
3. Multiplication
4. Division""")

operation = int(input("Choose an operation (1-4): "))

if operation == 1:
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif operation == 2:
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif operation == 3:
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif operation == 4:
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected. Please choose an option between 1 and 4.")