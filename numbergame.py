import random

playing=True
number=random.randint(0, 9)

print("Hey! This is a guessing game")
print("You need to guess the secret number between 0 and 9!")

while playing==True:
    guess=int(input())

    if number==guess:
        print("You have guessed the CORRECT NUMBER!!", number)
        break
    else:
        print("Try again")
        