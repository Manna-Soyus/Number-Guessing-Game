import random
number = random.randint(1, 20)
attempts = 5
print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 20.")
print("You have", attempts, "attempts.")
for i in range(attempts):
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < number:
        print("Too low! Try Again")
    else:
        print("Too high! Try Again")
else:
    print("Sorry! You have used all your attempts.")
    print("The correct number was:", number)
