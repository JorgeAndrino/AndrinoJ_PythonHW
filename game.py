# import the random package so that we can generate a random choice
from random import randint

# choices is an array => an array s a container that can hold multiples values
choices = ["rock", "paper", "scissors"]

# set the computer variable to the one of these choices
computer = choices[randint(0, 2)]

#set up the game loop so that we dont have to to restart all the time
player = False

while player is False:
    print("*****************************************\n")
    print("Choose your weapon!\n")
    print("*****************************************\n")

    player = input("choose rock, paper or scissors: \n\n")
    print("*****************************************\n")

    print("Computer choose ", computer, "\n")
    print("Player choose ", player, "\n")

    if player == "quit":
        exit()

    elif computer == player:
        print ("Tie! no one wins :(")

    elif player.lower() == "rock":
        if computer == "paper":
            print("YOU LOST", computer, "covers", player, "\n")
        else:
            print("YOU WIN", player, "smashes", computer, "\n")

    elif player.lower() == "paper":
        if computer == "scissors":
            print("YOU LOST", computer, "cuts", player, "\n")
        else:
            print("YOU WIN", player, "covers", computer, "\n")

    elif player.lower() == "scissors":
        if computer == "rock":
            print("YOU LOST", computer, "smashes", player, "\n")
        else:
            print("YOU WIN", player, "cuts", computer, "\n")
    
    else:
        print("You can use that Weapon right now!!, Try Again")

    player = False
    computer = choices[randint(0, 2)]

