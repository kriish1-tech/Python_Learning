print("Welcome to the Number Checker!")

num = int(input("Please enter a number: "))

if num > 0:
    print(f"{num} is a positive number.")
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")
elif num < 0:
    print(f"{num} is a negative number.")
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")
else:
    print(f"{num} is zero.")