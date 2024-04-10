import random

num = random.randint(1, 10)

guess = input("Guess the number: ")
int(guess, base=10)

if (guess == num):
    print("Correct guess")
    exit()
else:
    print('Incorrect guess, the number was: ${guess}')