from random import randint
win_counter = 0
computer_counter = 0
tie_counter = 0

def Game():
    moves = ['Rock', 'Paper', 'Scissors']
    computer = moves[randint(0, 2)]
    global win_counter, computer_counter, tie_counter

    if confirmation == 'yes' or confirmation == 'y':
        print('\n-------------------------------------------')
        print('Please choose your move from the following')
        moves = input("Rock | Paper | Scissors: ")

        print('\nYou threw', moves)
        print('Your opponent threw', computer)

        # Game Conditions for Rock
        if moves == 'Rock' and computer == 'Paper':
            print('\nYou lost! Paper covers Rock!')
            computer_counter += 1
        elif moves == 'Rock' and computer == 'Scissors':
            print('\nYou won, Rock crushes Scissors!')
            win_counter += 1

        # Game Conditions for Paper
        elif moves == 'Paper' and computer == 'Scissors':
            print('\nYou lost! Scissors cut Paper!')
            computer_counter += 1
        elif moves == 'Paper' and computer == 'Rock':
            print('\nYou won, Paper covers Rock!')
            win_counter += 1

        # Game Conditions for Scissors
        elif moves == 'Scissors' and computer == 'Rock':
            print('\nYou lost! Rock crushes Scissors!')
            computer_counter += 1
        elif moves == 'Scissors' and computer == 'Paper':
            print('\nYou won, Scissors cut Paper!')
            win_counter += 1

        # Tie condition
        else:
            print('Its a tie!')
            tie_counter += 1

    else:
        print('Good Bye')
        quit()

print('\nWelcome to "THE" Rock, Paper, Scissors game. This game plays first to 3 wins')
confirmation = input('\nWould you like to play the game? ')

while win_counter < 3 and computer_counter < 3:
    Game()
    print('\nYour Win counts are:', win_counter)
    print('Your Tie counts are:', tie_counter)
    print('Your Loss counts are:', computer_counter)

if win_counter == 3:
    print('\nCongrats you won the Game!')
elif computer_counter == 3:
    print('\nYou lost the game. Better luck next time!')