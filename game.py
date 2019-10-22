# import the random package so that we can generate a random choice
from random import randint

# choices is an array => an array s a container that can hold multiples values
choices = ["Rock", "Paper", "Scissors"]

# set the computer variable to the one of these choices
computer = choices[randint(0, 2)]

#set up the game loop so that we dont have to to restart all the time
player = False

while player is False:
    player = input("chose Rock, Paper or Scissors\n")

    print("computer chose ", computer, "\n")
    print("player chose ", player, "\n")

    if player == "quit":
        exit()

    elif computer == player:
        print ("Tie! no one wins :(")

    player = False
    computer = choices[randint(0, 2)]

