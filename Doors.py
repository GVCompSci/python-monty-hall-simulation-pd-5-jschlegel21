from random import randint

car=randint(1,3)
guess=int(input('What door would you like to choose 1,2,or 3?'))
switch='h'

if guess==1 and car==1:
    print('A goat is behind door number 3')
    switch=input('Would you like to switch to door number 2?')
    if switch.lower()=='yes':
        print('The car was behind door number',car,'you guessed door number 2')
        print('Enjoy your new goat')
    else:
        print('the car was behind door number',car,'you guessed door number 1')
        print('Enjoy your new car')
        
if guess==1 and car==2:
    print('A goat is behind door number 3')
    switch=input('Would you like to switch to door number 2?')
    if switch.lower()=='yes':
        print('The car was behind door number',car,'you guessed door number 2')
        print('Enjoy your new car')
    else:
        print('the car was behind door number',car,'you guessed door number 1')
        print('Enjoy your new goat')
        
if guess==1 and car==3:
    print('A goat is behind door number 2')
    switch=input('Would you like to switch to door number 3?')
    if switch.lower()=='yes':
        print('The car was behind door number',car,'you guessed door number 3')
        print('Enjoy your new car')
    else:
        print('the car was behind door number',car,'you guessed door number 1')
        print('Enjoy your new goat')
        
if guess==2 and car==1:
    print('A goat is behind door number 3')
    switch=input('Would you like to switch to door number 1?')
    if switch.lower()=='yes':
        print('the car was behind door number',car,'you guessed door number 1')
        print('Enjoy your new car')
    else:
        print('the car was behind door number',car,' you guessed door number 2')
        print('Enjoy your new goat')
        
if guess==2 and car==2:
    print('A goat is behind door number 3')
    switch=input('Would you like to switch to door number 1?')
    if switch.lower()=='yes':
        print('The car was behind door number',car,'you guessed door number 2')
        print('Enjoy your new car')
    else:
        print('the car was behind door number',car,'you guessed door number 1')
        print('Enjoy your new goat')
        
if guess==2 and car==3:
    print('A goat is behind door number 1')
    switch=input('Would you like to switch to door number 3?')
    if switch.lower()=='yes':
        print('The car was behind door number',car,'you guessed door number 3')
        print('Enjoy your new car')
    else:
        print('the car was behind door number',car,'you guessed door number 2')
        print('Enjoy your new goat')
        
if guess==3 and car==1:
    print('A goat is behind door number 2')
    switch=input('Would you like to switch to door number 1?')
    if switch.lower()=='yes':
        print('the car was behind door number',car,'you guessed door number 1')
        print('Enjoy your new car')
    else:
        print('the car was behind door number',car,' you guessed door number 3')
        print('Enjoy your new goat')
        
if guess==3 and car==2:
    print('A goat is behind door number 1')
    switch=input('Would you like to switch to door number 2?')
    if switch.lower()=='yes':
        print('The car was behind door number',car,'you guessed door number 2')
        print('Enjoy your new car')
    else:
        print('the car was behind door number',car,'you guessed door number 1')
        print('Enjoy your new goat')
        
if guess==3 and car==3:
    print('A goat is behind door number 1')
    switch=input('Would you like to switch to door number 2?')
    if switch.lower()=='yes':
        print('The car was behind door number',car,'you guessed door number 3')
        print('Enjoy your new car')
    else:
        print('the car was behind door number',car,'you guessed door number 2')
        print('Enjoy your new goat')