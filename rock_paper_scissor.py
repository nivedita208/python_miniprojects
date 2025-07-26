import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]
print("Lets start the game :)")

while True:
    #asking user to input rock paper scissors
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    #below How we can check if user input is equal to more than one thing
    if user_input not in options:
        print("please type rock,paper, or scissor to enjoy the game meow")
        continue
    
    random_number = random.randint(0, 2)
    # rock: 0 , paper: 1, scissors: 2 
    computer_pick =  options[random_number]
    print("Computer picked", computer_pick + ".")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        
    else:
        print("You lost!")
        computer_wins += 1
        
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
    
print("It was fun playing with u sweety meowww!")
print("Hare Krishna!!!")
        
    