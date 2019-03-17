import random as r

print('Hello what is your name?')
name = input()
secretNumber = r.randint(1,20)

for guesses in range(1,6):
    print('Guess the number between 1 and 20')
    guess = int(input())
    if guess < secretNumber:
        print('Nope. Higher')
    elif guess > secretNumber:
        print('Nope. Lower')
    else:
        break
if guess == secretNumber:
    print ('Congratulations ' + name + '! You guessed the secret number: ' + str(secretNumber) + ' in ' + str(guesses) + ' guesses')

else:
    print('Boooo ' + name + '! You didn\'nt guess the secret number: ' + str(secretNumber))