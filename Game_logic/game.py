from Game_logic.map import *
from Game_logic.fight import *
from random import randint
import os

# Func to start the game
def start_game(player):

    # Spawn coordinates of player and boss. It's forbidden because nothing spawn on their cases
    forbidden_coords = [(3, 3), (0, 0)]

    # Creation of the boss
    boss = Boss("Dragon",10,1000,50,20,0,0,25,4,25, 1000, "WoW, The dragon burned you !! ")
    
    # Creation of all of the objects
    list_objects = [
        health_potion("health potion", 10, 2, 2),
        attack_potion("attack potion", 10, *random_position_without_exclude_coordinates(forbidden_coords)),
        defense_potion("defense potion", 5, *random_position_without_exclude_coordinates(forbidden_coords))
    ]
    
    # Creation of all of the monsters
    list_monster = [
        Monster("Wolf",1, 50, 5, 2, 1,1, 10, 1.5, 20, 150, "Oh the wolf bite your head !!")
    ]
    
    os.system('cls')
    print("Ok ", player.name ," You are in the middle of a forest, what do you want to do ? ")
    
    # While the player and the boss ARE alive
    while player.health > 0 and boss.boss_dead == False:

        # Movement input and after we verify the position of the player
        player_input = input("Your movement (or quit the game) : ")
        print("\n")
        
        old_x, old_y = player.position_x, player.position_y
        
        if player_input.lower() == "up":
            player.position_y -= 1
            verify_object_and_player_position(player, list_objects)
            fight(player, list_monster)
            
        elif player_input.lower() == "down":
            player.position_y += 1
            verify_object_and_player_position(player, list_objects)
            fight(player, list_monster)
            
        elif player_input.lower() == "right":
            player.position_x += 1
            verify_object_and_player_position(player, list_objects)
            fight(player, list_monster)
            
        elif player_input.lower() == "left":
            player.position_x -= 1
            verify_object_and_player_position(player, list_objects)
            fight(player, list_monster)
            
        elif player_input.lower() == "quit":
            exit()
            
        else:
            print("Please enter a good direction")
            continue
        
        # If the player try to go out of the map
        if not verify_player_position(player):
            player.position_x, player.position_y = old_x, old_y
            print("You hit a Wall, you don't move of your case and please choose another direction")
            print("You are on x : ", player.position_x, " y : ", player.position_y)
    
    if boss.boss_dead == True:
        print("YOU KILLED THE BOSS")
        print("Congratulation, you finish the game, you are a real adventurer ", player.name, " !")
        exit()