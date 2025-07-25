# generate a random number and we are going to track  
# how many times it takes the user to guess this number

import random 

top_of_range = input("Type a number: ")
print(type(top_of_range))  # The type() function is used to check the type of any data or variable.

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
        
else:
    print('Please type a number next time.')
    quit()
    
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses = guesses + 1  #i can also right this in guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue
    
    if user_guess == random_number:
        print("You got it ")
        break
    
    elif user_guess > random_number:
        print("You were above the number!")
        
    else:
        print("You are below the number!")
        
print("you got it in",guesses,"guesses")
#print("you got it in" + str(guesses) + "guesses") 

