#Judson Dommer
from __future__ import print_function
import numpy
#This print the opening screen
print ('Welcome To Hangman!!')
print ('  -----|')
print ('  |    O')
print ('  |  /-|-\\')
print ('  |    |')
print ('  |   /-\\')
print ('  |  /---\\')
print ('------')
#This line asks the player to trigger or end the game
response = raw_input('Would You Like To Play Hangman? Y/N ')
if response == 'Y' or response == 'y':
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('Okay Lets Play!!')
    print('')
    print('  -----|')
    print('  |     ')
    print('  |     ')
    print('  |     ')
    print('  |     ')
    print('  |     ')
    print('------')
    print('')
elif response == 'N' or response == 'n':
    print('Okay, Goodbye!!')
    exit(0)
else:
    print('Sorry, I Didn\'t Understand That. Next Time Type Y Or N!')
    exit(0)

#These count and log guesses and will come in later
correctGuessed = []
incorrectGuessed = 0

#This is the list of words that can be chosen by the game
my_list = ['python', 'anaconda', 'cobra', 'viper', 'rattlesnake']

#This picks a random word from my_list
my_word = numpy.random.choice(my_list)
print ('_ ' * len(my_word))

#This function will determine how dead the hangman should be
def printHangman(numbWrong):
    print ('  -----|')
    if numbWrong >= 1:
        print ('  |    O')
    else:
        print ('  |    ')
    if numbWrong == 2:
        print ('  |    |')
        print ('  |    |')
    elif numbWrong <= 2:
        print ('  |     ')
        print ('  |     ')
    if numbWrong == 3:
        print('  |  /-|')
        print('  |    |')
    elif numbWrong >=4:
        print('  |  /-|-\\')
        print('  |    |')
    if numbWrong ==5:
        print('  |   /-')
        print('  |  /-')
        print('------')
    elif numbWrong >= 6:
        print('  |   /-\\')
        print('  |  /---\\')
        print('------')
    else:
        print('  |  ')
        print('  |  ')
        print('------')
#This control what prints after a guess
def printBlanks(word, correctLetters):
    solved = True
    for letter in word:
        letter = letter.lower()
        if letter in correctLetters:
            print(letter + ' ', end='')
        else:
            print ('_ ', end='')
            solved = False
    print ('')
    return solved
#This creates an infinite loop
while True:

#This asks the player for a guess
    guess = raw_input('Guess Something! ')
    print('')
    print('')

#This checks if a guess is correct and changes the variable of wrong guesses by 1, it also determines if you win or lose
    if guess in my_word:
            correctGuessed.append(guess)
            print (guess + ' Was Correct!!')
    else:
        incorrectGuessed +=  1
        print (guess + ' Was Incorrect')
    printHangman(incorrectGuessed)
    solved = printBlanks(my_word, correctGuessed)
    if solved:
        print ('Congratulations, You Win!!')
        break
    if incorrectGuessed >= 6 :
        print ('')
        print ('YOU LOST!!! ')
        break
