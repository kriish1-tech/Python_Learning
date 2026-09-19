print("Welcome to the Simple Calculator!")

operations = ("+", "-", "*", "/", "exit")

while True:
    user_input = input("Enter an operation (+, -, *, /) or 'exit' to quit: ")

    if user_input == "exit":
        print("Exiting the calculator. Goodbye!")
        break
    elif user_input in operations:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if user_input == "+":
            result = num1 + num2
            print(f"The result of addition is: {result}")
        elif user_input == "-":
            result = num1 - num2
            print(f"The result of subtraction is: {result}")
        elif user_input == "*":
            result = num1 * num2
            print(f"The result of multiplication is: {result}")
        elif user_input == "/":
            if num2 != 0:
                result = num1 / num2
                print(f"The result of division is: {result}")
            else:
                print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation selected. Please choose a valid operation (+, -, *, /) or 'exit' to quit.")