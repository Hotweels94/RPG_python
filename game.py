from character import *
from object import *

def start_game(player):
    boss = Boss("Boss",10,1000,50,20,0,0,8,10)
    
    list_objects = [
        health_potion("health potion", 10, 4, 3),
        attack_potion("attack potion", 10, 5, 2),
        defense_potion("defense potion", 10, 1, 4)
    ]
    
    print("Ok ", player.name ," You are in the middle of a forest, what do you want to do ? ")
    while player.health > 0 and boss.boss_dead == False:
        player_input = input("Your movement : ")
        
        old_x, old_y = player.postion_x, player.postion_y
        
        if player_input.lower() == "up":
            player.postion_y -= 1
            verify_object_and_player_position(player, list_objects)
            
        elif player_input.lower() == "down":
            player.postion_y += 1
            verify_object_and_player_position(player, list_objects)
            
        elif player_input.lower() == "right":
            player.postion_x += 1
            verify_object_and_player_position(player, list_objects)
            
        elif player_input.lower() == "left":
            player.postion_x -= 1
            verify_object_and_player_position(player, list_objects)
            
        else:
            print("Please enter a good direction")
            continue
        
        if not verify_player_position(player):
            player.postion_x, player.postion_y = old_x, old_y
            print("You hit a Wall, you don't move of your case and please choose another direction")

def verify_player_position(player):
    
    print("x : ", player.postion_x, " y : ", player.postion_y )
    if player.postion_x >= 3 and player.postion_y >= 0 and player.postion_x <= 6 and player.postion_y <= 6:
        print("You are in the Forest \n")
        return True
        
    if player.postion_x >= 0 and player.postion_y >= 0 and player.postion_x <= 2 and player.postion_y <= 3:
        print("You are in the Dungeon \n")
        return True
        
    if player.postion_x >= 0 and player.postion_y >= 4 and player.postion_x <= 2 and player.postion_y <= 6:
        print("You are in the Cave \n")
        return True
    
    if player.postion_x < 0 or player.postion_y < 0 or player.postion_x > 6 or player.postion_y > 6:
        return False
    
    return True

def verify_object_and_player_position(player, list_objects):
    for obj in list_objects:
        if player.postion_x == obj.postion_x and player.postion_y == obj.postion_y:
            player.inventory.append(obj)
            print("YOU'VE FOUND AN OBJECT ! :", obj.name)
            list_objects.remove(obj)
            break 
    
    