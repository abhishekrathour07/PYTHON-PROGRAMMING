import random
guess = random.randint(1, 10)
target = random.randint(1, 10)
print(target)
while (target != guess):
    guess = int(input('Guess a number between 1 and 10 until you get it right : '))

print('Well guessed!')