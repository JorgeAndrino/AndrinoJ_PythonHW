from random import randint

choices = ["rock", "paper", "scissors"]

def winorlose(status):
    print("Game Over")
    print("@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*@*")

    print("You", status, "! Would you like to play again?")

    choice = input("Y / N")
    print(choice)

    if (choice is "N") or (choice is "n"):
        print("You chose to quit...")
        exit()
        
    elif (choice is "Y") or (choice is "y"):
        global player_lives
        global computer_lives
        global player
        global computer
        global choices
        player_lives = 1
        computer_lives = 1
        player = False
        computer =  choices[randint(0,2)]