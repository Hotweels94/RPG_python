import os
from Game_logic.game import start_game
from Game_logic.data import player, list_monster, list_objects, list_weapon, list_event
from Game_logic.save import load

# Func to launch the game
def launch_screen():  
    player_choice = False
    
    # Choice of the player
    while player_choice != True:
        print("MAIN MENU \n")
        print("1. Create a new game \n")
        print("2. Load your game \n")
        print("3. Controls \n")
        print("4. About \n")
        print("4. Quit \n")
        player_input = int(input("Choice : "))
        
        if player_input == 1:
            player_choice = True
            player.name = ((input("Enter your name: ")))
            start_game(player, list_monster, list_objects, list_weapon, list_event)
            
        elif player_input == 2:
            # load the save
            loaded_player, loaded_monsters, loaded_objects, loaded_weapon, loaded_event = load()
            if loaded_player:
                load_player = loaded_player
                load_list_monster = loaded_monsters
                load_list_objects = loaded_objects
                load_list_weapon = loaded_weapon
                load_list_event = loaded_event
                start_game(load_player, load_list_monster, load_list_objects, load_list_weapon, load_list_event)
                
        elif player_input == 3:
            print("To move, you need to tap the direction where you want to move.")
            print("The directions are : 'left', 'right', 'up' and 'down' ")
            
        elif player_input == 4:
            print("This RPG is made by Ryan Amsellem--Bousignac as a project for Paris Ynov Campus \n")
            
        elif player_input == 5:
            player_choice = True
            exit()   
    
os.system('cls')
launch_screen()