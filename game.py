from map import *
from fight import *
from random import randint

def start_game(player):
    boss = Boss("Boss",10,1000,50,20,0,0,25,4,25, 1000)
    
    list_objects = [
        health_potion("health potion", 10, 4, 3),
        attack_potion("attack potion", 10, 5, 2),
        defense_potion("defense potion", 10, 1, 4)
    ]
    
    list_monster = [
        Monster("Wolf",1, 50, 5, 2, 5, 5, 10, 1.5, 20, 150)
    ]
    
    print("Ok ", player.name ," You are in the middle of a forest, what do you want to do ? ")
    while player.health > 0 and boss.boss_dead == False:
        player_input = input("Your movement : ")
        
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
        
        if not verify_player_position(player):
            player.position_x, player.position_y = old_x, old_y
            print("You hit a Wall, you don't move of your case and please choose another direction")

    