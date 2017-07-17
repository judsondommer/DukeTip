from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

#This list is our original data that will be used to create the equation
angles = [ -40, -20, 0, 20, 40, 60, 80]
measurements = [65.3333333333, 130, 383.6666666666, 642.6666666666, 717.6666666666, 626, 365.3333333333]

#These lines create the equation used to calculate the rocket distance.
result = np.polyfit(angles, measurements, 6)
eq = np.poly1d(result)

#This asks the user for an angle input to use in the equation
requestDistance = raw_input('Commander! At what angle should we launch our rocket? ')

#This will check to see if the user inputted a number that is usable
number = 0
try:
    number = float(requestDistance)
except ValueError:
    print ('Commander! Thats not a valid number to launch a rocket! Come back when you have your head on straight!')
    exit(0)

userResult = eq(number)

#This tells the user how far the rocket traveled
print ()
print ('Wow! Commander, our rocket traveled', userResult, 'miles! Thats very impressive!')
#These lines ask the user if they want to see the graph and equation, if the user accepts then it asks if the user wants to save the graph
infoRequest = raw_input('Commander! Would you like to learn more about the rocket? Y/N')
if infoRequest == 'Y' or infoRequest == 'y':
    print ('Of course Commander! Here is a graph and the equation used!')
    print (eq)
    #Here are the line and point graphs being created and shown
    plt.plot(angles, measurements, label='Graph')
    plt.plot(angles, measurements, 'ro', label = 'Graph')
    plt.show()
    saveRequest = raw_input('Commander! Would you like to save this graph? Y/N ')
    if saveRequest == 'Y' or saveRequest == 'y':
        #This is the graph being saved
        plt.savefig('uniquenametosearchandfind.png')
        print ('Yes Sir Commander! I have saved the graph! Good day!')
    elif saveRequest == 'N' or saveRequest == 'n':
        print ('Understandable Commander! Good day!')
    else:
        print ('Didn\'t quite hear that Commander... Good day then!')
elif infoRequest == 'N' or infoRequest == 'n':
    print('Understandable Commander! Good day!')
else:
    print('Didn\'t quite hear that Commander... Good day then!')
