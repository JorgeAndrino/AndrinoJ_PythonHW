from random import randint

choices = ["rock", "paper", "scissors"]

computer = choices[randint(0, 2)]

player = False


def chooseweapon(status):
    print("Choose your weapon!\n")
    print("*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*\n")

    player = input("choose rock, paper or scissors: \n\n")
    player = player.lower()
    print("*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*\n")

     print("Your Enemy choose ", computer, "\n")
    print("You choose ", player, "\n")


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
