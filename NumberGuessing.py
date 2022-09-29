import random
n = random.randint(1, 100)
guess = 1

print('\nWelcome to "THE" guess the random number game. The number ranges from 1-100.')

ans = int(input('\nPlease input your guess: '))

while n != ans:
    if ans > n:
        print('\nYour guess is too high!')
        ans = int(input('Please input your guess: '))
        guess += 1
    elif ans < n:
        print('\nYour guess is too low!')
        ans = int(input('Please input your guess: '))
        guess += 1
    else:
        break

print('\nCongrats you won the game!')
print('The number was', n, 'and it took you', guess, 'attempts.')