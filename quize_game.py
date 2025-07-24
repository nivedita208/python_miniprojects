# description : we want to ask the users a bunch of questions 
# and then if they give us the right ans to that question we will kind of add 
# one to there score then at the end of the program we will printout what they got out
#of the number of questions (if there was 10 questions we will say hey u got 3 out of 10 ect)
print("Welcome to Meoww World!")
playing = input("Do you want to play? ").lower()  #lower() its a pythons method

score = 0

if playing != "yes":
    quit()          # quite() used to Exits the Python interpreter
    
name =  input("What's your name, feline friend? ")
print("Welcome " + name + " Let's begin!")

answer = input("What sound does a cat make? ").lower()
if answer == "meow":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect")
    
answer = input("What is a group of kittens called? ").lower()
if answer == "kindle":
    print("Correct!")
    score += 1
else:
    print("Nope! It's 'Kindle' ")
    
answer = input("Which big cat is the largest? ").lower()
if answer == "tiger":
    print("Purr-fect!!Correct!")
    score += 1
else:
    print("Oops it's 'tiger")
    
answer = input("What do cats love to chase? ").lower()
if answer in ["mice", "mouse"]:
    print("Correct! Classic kitty behaviour")
    score += 1
    
else:
    print("Not quite! they love chasing mice ")
    
answer = input("Which famous cartoon cat is known for chasing Jerry? ").lower()
if answer == "tom":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
    
print("You answered " + str(score) + " questions correctly!" )
print("You got " + str((score/5)*100) + "%")

percentage =  (score / 5) * 100
if percentage == 100:
    print(" You're a purr-fect cat expert!")
elif percentage >= 80:
    print(" Great job, you really know your cats!")
elif percentage >= 50:
    print(" Not bad, but your inner cat needs more training!")
else:
    print(" Better luck next time! Time to hang out with some kitties and learn.")