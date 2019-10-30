# import the random package so that we can generate a random choice
from random import randint

#set up variables for players and AI lives
player_lives = 5
computer_lives = 5

# choices is an array => an array s a container that can hold multiples values
choices = ["rock", "paper", "scissors"]

# set the computer variable to the one of these choices
computer = choices[randint(0, 2)]

#set up the game loop so that we dont have to to restart all the time
player = False

while player is False:
    print("*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*\n")
    print("Enemy Lives: ", computer_lives, "\5")
    print("Hero Lives(YOU): ", player_lives, "\5")
    print("Choose your weapon!\n")
    print("*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*\n")

    player = input("choose rock, paper or scissors: \n\n")
    player = player.lower()
    print("*****************************************\n")

    print("Your Enemy choose ", computer, "\n")
    print("You choose ", player, "\n")

    if player == "quit":
        exit()

    elif computer == player:
        print ("Tie! You are safe... for now")

    elif player.lower() == "rock":
        if computer == "paper":
            print("YOU LOST", computer, "covers", player, "\n")
            player_lives = player_lives -1
            computer_lives = computer_lives +1
        else:
            print("YOU WIN", player, "smashes", computer, "\n")
            computer_lives = computer_lives -1
            player_lives = player_lives +1

    elif player.lower() == "paper":
        if computer == "scissors":
            print("YOU LOST", computer, "cuts", player, "\n")
            player_lives = player_lives -1
            computer_lives = computer_lives +1
        else:
            print("YOU WIN", player, "covers", computer, "\n")
            computer_lives = computer_lives -1
            player_lives = player_lives +1

    elif player.lower() == "scissors":
        if computer == "rock":
            print("YOU LOST", computer, "smashes", player, "\n")
            player_lives = player_lives -1
            computer_lives = computer_lives +1
        else:
            print("YOU WIN", player, "cuts", computer, "\n")
            computer_lives = computer_lives -1
            player_lives = player_lives +1
    
    else:
        print("You can use that Weapon right now!!, Try Again")

    if player_lives is 0:
        print("GAME OVER SUCKA!!! Play Again?..")
        choice = input("Y / N")
        print(choice)

        if (choice is "N") or (choice is "n"):
            print("You chose to quit...")
            exit()
        
        elif (choice is "Y") or (choice is "y"):
            player_lives = 5
            computer_lives = 5
            player = False
            computer =  choices[randint(0,2)]


    elif computer_lives is 0:
        print("YOU WON MY DUDE, CONGRATS!!! Play Again?..\n")
        choice = input("Y / N")
        print(choice)

        if (choice is "N") or (choice is "n"):
            print("You chose to quit...")
            exit()
        
        elif (choice is "Y") or (choice is "y"):
            player_lives = 5
            computer_lives = 5
            player = False
            computer =  choices[randint(0,2)]    
        
    else:
        player = False
        computer = choices[randint(0,2)]


    player = False
    computer = choices[randint(0, 2)]

