import random

number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")

while True:
    guess = int(input("Guess a number between 1 and 100 (or type 'exit' to quit): "))
    if guess == number:
        print("Congratulations! You guessed the number.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")