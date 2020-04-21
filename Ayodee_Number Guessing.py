print ('''*******************************************************************************
                    Python Number Guessing Game
                    AYO OMOLADE
                    Slack username : Ayodee
                    Email Address : omoladee11@gmail.com
******************************************************************************''')

#Random
import random

#Check input for integer
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("This is not a number! Try again.")
       continue
    else:
       return userInput 
       break 
        
#Main Program
Play = True

while Play:
    print ("Welcome to the Number Guessing Game")
    
    #Get User Level
    Level = int(input('''Please choose a level of difficulty.
                      \nFor Easy - 1 \nFor Medium - 2 \nFor Hard - 3
                      \nPlease select a level: '''))

    #Easy level
    if int(Level) == 1:
        Right_No = random.randint(1,10)
        print("Guess a number between 1 and 10.\nYou have six(6) tries to get the number right.")
        chances = 0
        while chances < 6:
            User_No = inputNumber("\nEnter your guess: ")
            if User_No == Right_No:
                print("YOU GOT IT RIGHT!!!")
                break
            else:
                print("That was Wrong")
                print("You have used " + str(int(chances+1)) + " out of 6 chances")
            chances +=1
        if not chances < 6:
            print("GAME OVER!!! \nThe number is ", Right_No)
            

    #Medium level
    if int(Level) == 2:
        Right_No = random.randint(1,20)
        print("Guess a number between 1 and 20.\nYou have four(4) tries to get the number right.")
        chances = 0
        while chances < 4:
            User_No = inputNumber("\nEnter your guess: ")
            if User_No == Right_No:
                print("YOU GOT IT RIGHT!!!")
                break
            else:
                print("That was Wrong")
                print("You have used " + str(int(chances+1)) + " out of 4 chances")
            chances +=1
        if not chances < 4:
            print("GAME OVER!!! \nThe number is ", Right_No)
   
    #Hard level
    if int(Level) == 3:
        Right_No = random.randint(1,50)
        print("Guess a number between 1 and 50.\nYou have three(3) tries to get the number right.")
        chances = 0
        while chances < 3:
            User_No = inputNumber("\nEnter your guess: ")
            if User_No == Right_No:
                print("YOU GOT IT RIGHT!!!")
                break
            else:
                print("That was Wrong")
                print("You have used " + str(int(chances+1)) + " out of 3 chances")
            chances +=1
        if not chances < 3:
            print("GAME OVER!!! \nThe number is ", Right_No)

    New_Game = str(input("\nThanks for playing. \nWould you like to play again? Y/N: "))
    if New_Game.lower() == "n":
        Play = False
        print("\nThank you for playing. Come back to play some other time")
    else:
        Play = True
