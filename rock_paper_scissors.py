# Rock, paper, scissors
from random import randint

game_on = True
list = ['rock', 'paper', 'scissors']
while game_on:
    a = str(input('Choose rock, paper or scissors: '))
    b_idx = randint(0, 2)
    b = list[b_idx]
    if a == b:
        print('There is a tie, we both chose ' + str(b) +'.')
        message = "Let's try again "
    elif (a == 'scissors' and b == 'rock') or (b == 'scissors' and a == 'paper') or (b == 'paper' and a == 'scissors'):
        print('I win. HAHAHA')
        message = 'Do you try to try again, loser (y/n)? '
    elif (b == 'scissors' and a == 'rock') or (a == 'scissors' and b == 'paper') or (a == 'paper' and b == 'scissors'):
        print('You win :(')
        message = 'Give me another chance and I will beat you (y/n). '
    c = input(message)
    game_on = True if c == 'y' else False


