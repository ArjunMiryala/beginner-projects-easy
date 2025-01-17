from ast import Continue
import random

top_of_range = input("type a number: ")

if top_of_range.isdigit():                                              # checking whether the string is digit string(contains digits only)  
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Plase enter a number greater than 0")
        quit()
else:
    print("Please enter only numbers")
    quit()

random_number = random.randint(0, top_of_range)                          # starts from 0 and ends and includes at 11
#                                                                        #randrange(-4, 11) # does not include 10 but starts from -2.
#                                                                        #if we put ranint(start, end) it will incldue ending number also.
guesses = 0

while True:
    guesses += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():                 #cheking if the user guess is digit string 
        user_guess = int(user_guess)         #converting user guess to int
    else:
        print('please type a number next time')
        Continue                                #stopiing loop here and starting this loop again

    if user_guess == random_number:
        print("you got it!")
        break                               # if the guess is right the loop will stop 
    elif user_guess > random_number:
        print("you were above the number!")
    else:
        print("you were below the number!" )

print("You got it in", guesses, "guesses")