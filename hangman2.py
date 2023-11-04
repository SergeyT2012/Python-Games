import random

HANGMAN_PICS = ['''		
	+---+		
	    |		
	    |		
	    |		
	    ===''', '''		
	+---+		
	O   |		
	    |		
	    |		
	    ===''', '''		
	+---+		
	O   |		
	|   |		
	    |		
	    ===''', '''		
	+---+		
	O   |		
       /|   |		
	    |		
	    ===''', '''		
	+---+		
	O   |		
       /|\  |		
	    |		
	    ===''', '''		
	+---+		
       O   |		
      /|\  |		
      /    |		
	    ===''', '''		
	+---+		
       O   |		
      /|\  |		
      / \  |		
	    ===''', '''
       +---+
       [O  |
       /|\ |
       / \ |
       ===''', '''
       +---+
       [O] |
       /|\ |
       / \ |
       ===''']

wordDict = {   'Colors':'red orange yellow green blue indigo violet white black brown'.split(),		
            'Shapes':'square triangle rectangle circle ellipse rhombus trapazoid chevron pentagon hexagon septagon octogon'.split(),		
            'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantalope mango strawberry tomato'.split(),		
            'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return wordDict[wordKey][wordIndex], wordKey

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)
    
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i]+ secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('please write ONE letter.')
        elif guess in alreadyGuessed:
            print('you dummy, you wrote that letter already, open your eyes.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('this game is in english, so write ONLY latin letters please. NUMBERS ARE NOT ALLOWED TOO.')
        else:
            return guess
        

def playAgain():
    print('want to play again? (please enter Y/N)')
    return input().lower().startswith('y')

print('''                                 
                                  _____
          |   |     /\\    |\\  |  |       |\\    /|    /\\    |\\  |
          |---|    /--\\   | \\ |  |  --|  | \\  / |   /--\\   | \\ | 
          |   |   /    \\  |  \\|  |____|  |  \\/  |  /    \\  |  \\|
      ''')

difficulty = ''

while difficulty not in ['E','M','H']:
    print('pick a difficulty. e - easy, m - medium, h - hard.')
    difficulty = input().upper()

if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]

if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(wordDict) 
gameIsDone = False

while True:
    print('the secret word is from ' + secretSet + '.')
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess 

        foundAllLetters = True
        
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break 
        
        if foundAllLetters:
            print('wow, you did it. good job, the word was ' + secretWord + '.')
            gameIsDone = True
        
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('you lost. thats ok, its expected for some players. the word was ' + secretWord + '.')
            gameIsDone = True
    
    if gameIsDone:
        if playAgain():
            missedLetters =''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(wordDict)
        else:
            break