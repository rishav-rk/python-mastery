# Implement a number guessing game where the user has 5 chances to guess a random number between 1 and 50. Provide hints if the guess is too high or too low.
import random

chances = 5
won = False

number_to_guess = random.randint(1, 50)
print(number_to_guess)

while chances > 0:
    user_guess = int(input("Guess number: "))

    if user_guess == number_to_guess:
        won = True
        break
    elif user_guess > number_to_guess:
        print("Guess is too high")
    else:
        print("Guess is too low")
    
    chances -= 1

if won:
    print("Wohooo🥳... You Won🎊🎉")
else:
    print("Sorry......☹️🥲 You Lost")