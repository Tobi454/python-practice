import random

secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 7

print("Welcome to the Guessing Game!")
print("You have", max_attempts, "attempts to guess the number.")

while attempts < max_attempts:

    guess = int(input("Guess a number between 1 and 100: "))
    
    attempts += 1

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100")
        continue

    if guess > secret_number:
        print("Too high")

    elif guess < secret_number:
        print("Too low")

    else:
        print("Correct!")
        print("You guessed the number in", attempts, "attempts")
        break

if guess != secret_number:
    print("Game Over!")
    print("The secret number was:", secret_number)