from character import *

def start_game(player):
    boss = Boss("Boss",10,1000,50,20,6,6)
    print("Ok ", player.name ," You are in the middle of a forest, what do you want to do ? ")
    while player.health > 0 or boss.boss_dead == True:
        player_input = (input("Your movement : "))
        
        old_x, old_y = player.postion_x, player.postion_y
        
        if player_input.lower() == "up":
            player.postion_y -= 1
            
        elif player_input.lower() == "down":
            player.postion_y += 1
            
        elif player_input.lower() == "right":
            player.postion_x += 1
            
        elif player_input.lower() == "left":
            player.postion_x -= 1
            
        else:
            print("Please enter a good direction")
            continue
        
        if not verify_player_position(player):
            player.postion_x, player.postion_y = old_x, old_y
            print("You hit a Wall, you don't move of your case and please choose another direction")

def verify_player_position(player):
    
    print("x : ", player.postion_x, " y : ", player.postion_y )
    if player.postion_x >= 3 and player.postion_y >= 0 and player.postion_x <= 6 and player.postion_y <= 6:
        print("You are in the Forest")
        return True
        
    if player.postion_x >= 0 and player.postion_y >= 0 and player.postion_x <= 2 and player.postion_y <= 3:
        print("You are in the Dungeon")
        return True
        
    if player.postion_x >= 0 and player.postion_y >= 4 and player.postion_x <= 2 and player.postion_y <= 6:
        print("You are in the Cave")
        return True
    
    if player.postion_x < 0 or player.postion_y < 0 or player.postion_x > 6 or player.postion_y > 6:
        return False
    
    return True