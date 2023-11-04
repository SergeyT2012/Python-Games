import random

rps = 'rock paper scissors'.split()


def displayIntro():
    print('Hello fellow human. I am the computer, and I challange you on a game of ROCK PAPER SCISSORS! Choose Game Mode First.')

def computerGuess():
    cguess = random.randint(0, len(rps) - 1)
    return rps[cguess]

def userGuess():
    NewUGuess = ''
    while NewUGuess != 'rock' and NewUGuess != 'paper' and NewUGuess != 'scissors':
        print('Please write in English, and only rock, paper or scissors.')
        NewUGuess = input().lower()
    uGuess = NewUGuess
    return uGuess

def playAgain(mode):
    print('Want to play again or choose other gamemode? (y/n/c)')
    userInputPlayAgain = input().lower()
    if userInputPlayAgain.startswith('c'):
        mode = changeMode()
        return mode, True
    elif userInputPlayAgain.startswith('y'):
        return mode, True
    else: 
        return mode, False

def changeMode():
    mode = ''
    while mode not in ['CW', 'UW', 'FG']:
        print('pick a gamemode: only computer wins - CW, only user wins - UW, and fair game - FG')
        mode = input().upper()
    print('You selected : '+ mode)
    return mode


playAgainResult = True

displayIntro()

print()

mode = changeMode()

while playAgainResult == True:
    
    uGuess = ''
    GameIsDone = ''
    print('Select your Material : rock, paper or scissors')
    uGuess = userGuess()

    if mode == 'CW':
        print('R O C K  P A P E R  S C I S S O R S')
        if uGuess == 'rock':
            print('I won! I chose paper.')
        elif uGuess == 'paper':
            print('I won! I chose scissors.')
        else:
            print('I won! I chose rock.')
    elif mode == 'UW':
        print('R O C K  P A P E R  S C I S S O R S')
        if uGuess == 'paper':
            print('i lost. i chose rock.')
        elif uGuess == 'rock':
            print('i lost. i chose scissors.')
        else:
            print('i lost. i chose paper.')
    else:
        print('R O C K  P A P E R  S C I S S O R S')
        cGuess = computerGuess()
        if uGuess == cGuess:
            print('We chose the same thing. Try again.')
        elif (uGuess == 'rock' and cGuess == 'paper') or (uGuess == 'scissors' and cGuess == 'rock') or (uGuess == 'paper' and cGuess == 'scissors'):
            print('You lost. I chose ' + cGuess + '.')
        else:
            print('You won! I chose ' + cGuess + '.')
    GameIsDone = True

    if GameIsDone:
        print('R O C K  P A P E R  S C I S S O R S')

    mode, playAgainResult = playAgain(mode)



