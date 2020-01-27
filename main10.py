#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
#prints greetings
colors = ['red','orange','yellow','green','blue','violet','purple']
#sets colors as a list
play_again = ''
#saves a variable
best_count = sys.maxsize            # the biggest number
#a way to store the best score

while (play_again != 'n' and play_again != 'no'):
    #starts a loop
    match_color = random.choice(colors)
    #chooses random color
    count = 0
    #sets count to 0
    color = ''
    #creates color variable
    while (color != match_color):
        #loops until color is the same as match_color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        #asks the favorite color
        color = color.lower().strip()
        #changes variable to lower case and strips spaces
        count += 1
        #adds 1 to count
        if (color == match_color):
            print('Correct!')
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
        #if else to see if the correct color was guessed and the print above tells you how many times you tried
    
    print('\nYou guessed it in {} tries!'.format(count))
    #winning statement with how many tries it took.

    if (count < best_count):
    #sees if the new count is less than the old
        print('This was your best guess so far!')
        #prints line
        best_count = count
        #sets the new best score

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()
    #ask if you would like to play again and sends you to the top if ur answer is not n or no

print('Thanks for playing!')
#prints thanks