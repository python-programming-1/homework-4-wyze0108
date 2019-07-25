#! yize wu homework#4 Rock Paper Scissors

import random
you = ''
options = ['R', 'P', 'S']
def run(games = 1):
    print('PLAY by typing one of the following below: \n R for Rock, P for Paper, S for Scissors')
    x, y, z = 0, 0, 0
    score = {'you': x, 'computer': y, 'draw': z}
    while True:
        print('Please choose \'R\', \'P\', or \'S\' to play, \'SC/SCORE\' to check the score, or \'Q/QUIT\' to quit')
        games += 1
        computer = random.choice(options)
        you = input().upper()
        if you == 'SC' or you =='SCORE':
            print('your score = {} computer score = {} draws = {}'.
                      format(score['you'],score['computer'],score['draw']))
            continue
        elif you == 'Q' or you =='QUIT':
            print("Time to quit...")
            print('your final score = {} computer final score = {} draws = {}'.
                  format(score['you'], score['computer'], score['draw']))
            exit(0)
        elif not(you == 'R' or you == 'S' or you == 'P'):
            print("\n{} is invalid input! Please type a valid option".format(you))
            continue

        else:
            if you == 'R' and computer == 'R':
                score['draw'] += 1
                print('Computer chooses {}'.format(computer))
                print('DRAW')
            elif you == 'P' and computer == 'P':
                score['draw'] += 1
                print('Computer chooses {}'.format(computer))
                print('DRAW')
            elif you == 'S' and computer == 'S':
                score['draw'] += 1
                print('Computer chooses {}'.format(computer))
                print('DRAW')
            elif you == 'R' and computer == 'P':
                score['computer'] += 1
                print('Computer chooses {}'.format(computer))
                print('Computer wins!')
            elif you == 'R' and computer == 'S':
                score['you'] += 1
                print('Computer chooses {}'.format(computer))
                print('You win! ')
            elif you == 'P' and computer == 'R':
                score['you'] += 1
                print('Computer chooses {}'.format(computer))
                print('You Win!')
            elif you == 'S' and computer == 'R':
                 score['computer'] += 1
                 print('Computer chooses {}'.format(computer))
                 print('Computer wins!')
            elif you == 'P'and computer == 'S':
                score['computer'] += 1
                print('Computer chooses {}'.format(computer))
                print('Computer wins!')
            elif you == 'S' and computer == 'P':
                score['you'] += 1
                print('Computer chooses {}'.format(computer))
                print('You win!')

print('Want to play? Hit \'Y/YES\' to play or \'N/NO\' to exit\n')
start = input().upper()
if start == 'Y' or start == 'YES':
    run()
elif start == 'N' or start == 'NO':
    print('You''\'ve entered {} so exiting...'.format(start))
else:
    print('You''\'ve entered {} which is invalid so exiting..'
          '.'.format(start))