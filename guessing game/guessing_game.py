from random import randint
import time
number = randint(1,100)
tries = 0

print("Choose a random number from 1-100")

while tries != 10:
    guess = int(input("Please make your guess: "))

    if guess > number:
        print("Wrong, the number I guessed is lower than this, try again!")
        tries = tries + 1
    elif guess < number:
        print("Wrong, the number I guessed is higher than this, try again!")
        tries = tries + 1
    else:
        print("Good Job guessing on the right number")
        time.sleep(5)
        exit()

print(f"The number is {number}")
