import random

n = random.randint(0, 10)

guesses = 0

while True:
    guess = int(input("Guess a number between 0 and 10: "))

    if n == guess:
        print("Topdingiz!")
        break

    guesses += 1

    if guesses >= 3:
        print("Topolmadingiz, afsus!")
        print(f"To'g'ri javob: {n}")
        break
