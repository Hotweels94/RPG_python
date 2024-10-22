from map import *

def start_game(player):
    boss = Boss("Boss",10,1000,50,20,0,0,8,10)
    
    list_objects = [
        health_potion("health potion", 10, 4, 3),
        attack_potion("attack potion", 10, 5, 2),
        defense_potion("defense potion", 10, 1, 4)
    ]
    
    list_monster = [
        Monster("Wolf", 1, 20, 5, 2, 5, 5, 2, 5)
    ]
    
    print("Ok ", player.name ," You are in the middle of a forest, what do you want to do ? ")
    while player.health > 0 and boss.boss_dead == False:
        player_input = input("Your movement : ")
        
        old_x, old_y = player.postion_x, player.postion_y
        
        if player_input.lower() == "up":
            player.postion_y -= 1
            verify_object_and_player_position(player, list_objects)
            fight(player, list_monster)
            
        elif player_input.lower() == "down":
            player.postion_y += 1
            verify_object_and_player_position(player, list_objects)
            fight(player, list_monster)
            
        elif player_input.lower() == "right":
            player.postion_x += 1
            verify_object_and_player_position(player, list_objects)
            fight(player, list_monster)
            
        elif player_input.lower() == "left":
            player.postion_x -= 1
            verify_object_and_player_position(player, list_objects)
            fight(player, list_monster)
            
        else:
            print("Please enter a good direction")
            continue
        
        if not verify_player_position(player):
            player.postion_x, player.postion_y = old_x, old_y
            print("You hit a Wall, you don't move of your case and please choose another direction")

    