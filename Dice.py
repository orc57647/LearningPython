# This is a dice rolling betting game, please play responsibly. Made by Owen Conrad 9/29/2022

from random import randint
win_counter = 0
computer_counter = 0
total_games = 0
money = 0

'''
def Info():
    if confirmation == 'i' or confirmation == 'info':
        print('\n-------------------------------------------')
        print('The rules of this game are as follows:')
        print('1. Pick a Number between 1 and 6')
        print('2. If you roll the correct number you win $100, roll the wrong number you lose $10')
        print('3. Have fun and play responsibly!')
        print('-------------------------------------------\n')

    confirmation2 = input('\nNow would you like to play the games now that you know the rules? ')
    if confirmation2 == 'y' or confirmation2 == 'yes':
        Game()
    else:
        print('Have a great day!')
        quit()
    '''


def Game():
    computer = randint(1, 6)
    global win_counter, computer_counter, total_games, money

    if confirmation == 'yes' or confirmation == 'y':
        moves = int(input('\nA Die has sides numbered 1, 2, 3, 4, 5, and 6. Please choose one of these numbers: '))

        print('\nYou chose', moves)
        print('The die rolled a', computer)

        # Game Conditions
        if moves == 1 and computer == 1:
            print('Congrats you just earned $100!')
            money += 100
            win_counter += 1
            total_games += 1
        elif moves == 2 and computer == 2:
            print('Congrats you just earned $100!')
            money += 100
            win_counter += 1
            total_games += 1
        elif moves == 3 and computer == 3:
            print('Congrats you just earned $100!')
            money += 100
            win_counter += 1
            total_games += 1
        elif moves == 4 and computer == 4:
            print('Congrats you just earned $100!')
            money += 100
            win_counter += 1
            total_games += 1
        elif moves == 5 and computer == 5:
            print('Congrats you just earned $100!')
            money += 100
            win_counter += 1
            total_games += 1
        elif moves == 6 and computer == 6:
            print('Congrats you just earned $100!')
            money += 100
            win_counter += 1
            total_games += 1
        else:
            print('I am sorry but you lost. You lose $10')
            money -= 10
            computer_counter += 1
            total_games += 1

    else:
        print('\nHave a great day!')
        quit()

print('\nWelcome to "THE" die rolling game. You can play this game as many times as you want.')
print('\n-------------------------------------------')
print('The rules of this game are as follows:')
print('1. Pick a Number between 1 and 6')
print('2. If you roll the correct number you win $100, roll the wrong number you lose $10')
print('3. Have fun and play responsibly!')
print('-------------------------------------------\n')
confirmation = input('Would you like to play the game? ')

while 300 > money > -30:
    Game()
    print('\n-------------------------------------------')
    print('Your Win count is:', win_counter)
    print('Your Loss count is:', computer_counter)
    print('Total Games:', total_games)
    print('Your money total is:', '$', money)
    print('-------------------------------------------\n')

if money >= 300:
    print('You have won too much money. You have hit the limit and can no longer play this game.')
    print('\nGood Bye')
elif money <= -30:
    print('You have lost too much money. You have hit the limit and can no longer play this game.')
    print('\nGood Bye')