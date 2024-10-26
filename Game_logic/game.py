from Game_logic.map import *
from Game_logic.fight import *
from random import randint
from Game_logic.data import *
import os
import json

# Func to start the game
def start_game(player):
    
    os.system('cls')
    print("Ok ", player.name ," You are in the middle of a forest, what do you want to do ? ")
    
    # While the player AND the boss are alive
    while player.health > 0 and boss.boss_dead == False:

        # Movement input and after we verify the position of the player
        player_input = input("Your movement (or quit / save the game) : ")
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
            
        elif player_input.lower() == "save":
            save_data = {
                "player": [player.to_dict()],
                "monsters": [monster.to_dict() for monster in list_monster],
                "objects": [obj.to_dict() for obj in list_objects]
            }
            save("save.json", save_data)
            exit()
            
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

def custom_serializer(obj):
    if hasattr(obj, 'to_dict'):
        return obj.to_dict()
    return str(obj)  

def save(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4, default=custom_serializer)
    print("Save is created !")
    
def load(file):
    with open(file, "r") as f:
        return json.load(f)
    
    