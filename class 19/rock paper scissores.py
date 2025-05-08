import random

rsp = ['rock','paper','scissors']

while True:
    c= random.choice(rsp)
    u = input('enter your choice \n rock \n paper \n scissors \n :-')

    if c == u.lower():
        print('it is a draw!')

    elif ( c == 'rock' and u == 'paper') or (c=='paper' and u == 'scissors') or (c == 'scissors' and u == 'paper'):
        print('user wins!!')

    else:
        print('computer wins!!')

    ch = input('would you like to play again? (y/n)')
    if ch.lower() == 'n':
        break