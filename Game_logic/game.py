from Game_logic.map import *
from Game_logic.fight import *
from random import randint
from Game_logic.data import boss
from Game_logic.save import save
import os

# Func to start the game
def start_game(player, list_monster, list_objects, list_weapon, list_event, list_shop):
    
    os.system('cls')
    print("Ok ", player.name ," You are in the middle of a forest, what do you want to do ? ")
    if not player.weapon:
        player.weapon.append(list_weapon[0])

    # While the player AND the boss are alive
    while player.health > 0 and boss.boss_dead == False:

        # Player input and after we verify the position of the player
        player_input = input("Your decision (move, map, save or quit) : ")
        print("\n")
        
        old_x, old_y = player.position_x, player.position_y
        
        if player_input.lower() == "up":
            player.position_y -= 1
            verify_object_and_player_position(player, list_objects)
            verify_weapon_and_player_position(player, list_weapon)
            verify_event_and_player_position(player, list_event)
            verify_shop_and_player_position(player, list_shop)
            fight(player, list_monster)
            
        elif player_input.lower() == "down":
            player.position_y += 1
            verify_object_and_player_position(player, list_objects)
            verify_weapon_and_player_position(player, list_weapon)
            verify_event_and_player_position(player, list_event)
            verify_shop_and_player_position(player, list_shop)
            fight(player, list_monster)
            
        elif player_input.lower() == "right":
            player.position_x += 1
            verify_object_and_player_position(player, list_objects)
            verify_weapon_and_player_position(player, list_weapon)
            verify_event_and_player_position(player, list_event)
            verify_shop_and_player_position(player, list_shop)
            fight(player, list_monster)
            
        elif player_input.lower() == "left":
            player.position_x -= 1
            verify_object_and_player_position(player, list_objects)
            verify_weapon_and_player_position(player, list_weapon)
            verify_event_and_player_position(player, list_event)
            verify_shop_and_player_position(player, list_shop)
            fight(player, list_monster)
            
        elif player_input.lower() == "save":
            save(player, list_monster, list_objects, list_weapon, list_event, list_shop)
            exit()
            
        elif player_input.lower() == "quit":
            exit()
            
        elif player_input.lower() == "map":
            show_map(player)
            
        else:
            print("Please enter a good direction")
            continue
        
        # If the player try to go out of the map
        if not verify_player_position(player):
            player.position_x, player.position_y = old_x, old_y
            print("You hit a Wall, you don't move of your case and please choose another direction")
            print("You are on x : ", player.position_x, " y : ", player.position_y)
            
    if player.health <= 0:
        print("YOU ARE DEAD !!")
        print("Game Over")
        exit()
    
    if boss.boss_dead == True:
        print("YOU KILLED THE BOSS")
        print("Congratulation, you finish the game, you are a real adventurer ", player.name, " !")
        exit()