import time
import random

def displayIntro():
    print('''You are in lands inhabited by dragons. In front of you you see two caves. In one of them there is a friendly dragon who is ready to share his treasures with you. In the second, there is a greedy and hungry dragon that will instantly eat you.''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you enter? (press key 1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You walk into a cave...')
    time.sleep(2)
    print('A big dragon jumps infront of you! He opens his big mouth and...')
    time.sleep(2)

    friendlyCave = random.randint(1, 2)
    if chosenCave == str(friendlyCave):
        print('...shares his treasure with you!')
    else:
        print('...eats you!')

playAgain = 'yes'

while playAgain.lower().startswith('y'):
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Try again?(y/n)')
    playAgain = input()
