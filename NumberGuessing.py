# Exercise 1 1/18/2023
import random

def main():
    guess_counter = 1
    low = 1
    high = 100
    ans = random.randint(low, high)

    print('\nWelcome to "THE" guess the random number game. The number ranges from 1-100.')
    guess = int(input('\nPlease input your guess: '))

    while ans != guess:
        if guess > ans:
            print(f'Guess {guess_counter}: Your guess is too high!')
            high = guess
            print(f'Range Helper: {low} to {high}')
            guess = int(input('\nPlease input your guess: '))
            guess_counter += 1

        elif guess < ans:
            print(f'Guess {guess_counter}: Your guess is too low!')
            low = guess
            print(f'Range Helper: {low} to {high}')
            guess = int(input('\nPlease input your guess: '))
            guess_counter += 1

        else:
            break

    print('\nCongrats you won the game!')
    print(f'The number was {ans} and it took you {guess_counter} attempts.')

main()
