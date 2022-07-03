import random
import sys

number = random.randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    guessed_number = int(
        input(f'Please guess a number between {sys.argv[1]} and {sys.argv[2]}: '))
    if (number == guessed_number):
        print('You are a genius')
        break
    else:
        print('please try again')
        continue
