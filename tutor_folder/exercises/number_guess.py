import random

answer = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == answer:
    print("Congratulations! You guessed the number.")
else:
    print("Sorry the correct nymber was", answer)