from game import start_game
from character import *

def launch_screen():
    player_choice = False

    while player_choice != True:
        print("MAIN MENU \n")
        print("1. Create a new game \n")
        print("2. Controls \n")
        print("3. About the game \n")
        print("4. Quit \n")
        player_input = int(input("Choice : "))

        if player_input == 1:
            player_choice = True
            player = Player((input("Enter your name: ")))
            start_game(player)
        elif player_input == 2:
            print("To move, you need to tap the direction where you want to move.")
            print("The directions are : 'left', 'right', 'up' and 'down' ")
        elif player_input == 3:
            print("This RPG is made by Ryan Amsellem--Bousignac as a project for Paris Ynov Campus \n")
        elif player_input == 4:
            player_choice = True
            exit()
    

launch_screen()