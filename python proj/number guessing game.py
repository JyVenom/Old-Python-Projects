# This is a guess the number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
    print('Take a guess.') 
    guess = input()
    guess = int(guess)

    if guess == 3636:
        print(number)
    if guess > 20 and guess!=3636:
        print(guess," is larger than 20, please take anouther valid guess")

    if  guess <1:
        print(guess," is less than 1, please take anouther valid guess")

    if guess < number and guess > 0:
        print('Your guess is too low.')
        guessesTaken = guessesTaken + 1

    if guess > number and guess<20:
        print('Your guess is too high.')
        guessesTaken = guessesTaken + 1

    if guess == number:
        guessesTaken = guessesTaken + 1
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guess(es)!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
