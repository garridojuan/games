from random import randint
import pandas as pd


def hangman(filename = 'pelis.txt', opportunities=6):
    filename = 'pelis.txt'
    words = pd.read_table('pelis.txt', header=None)
    errors = 0
    word = str(words.iloc[randint(0, len(words)), 0]).upper()
    list_of_char = []
    list_of_char2 = []

    while errors < opportunities:
        char = str(input('Guess a letter: ')).upper()
        if char in list_of_char:
            print('Character already tried, insert another please:  ')
            continue
        else:
            list_of_char.append(char)
        if len(char) > 1:
            if char == word:
                print('Good job!')
                break
            else:
                errors += 1
                print('Error! You have only ' + str(opportunities-errors) + ' opportunites left.')
                continue

        word_list = list(word)
        shown_word = []
        is_in = False
        for i in word_list:
            if i in ('.,?¿!¡') or (i == ' '):
                shown_word.append(i)
            elif i == char:
                shown_word.append(i)
                is_in = True
                list_of_char2.append(i)
            elif i in list_of_char2:
                shown_word.append(i)
            else:
                shown_word.append('_')
        if not is_in:
            errors += 1
            print('Error! You have only ' + str(opportunities-errors) + ' opportunites left.')

        shown_word2 = ''.join(shown_word)
        print(' '.join(shown_word))
        if shown_word2 == word:
            print('Good job!')
            break

    print('The solution was ' + word)