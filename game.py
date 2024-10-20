from character import *

def start_game(player):
    boss = Boss("Boss",10,1000,50,20,6,6)
    print("Ok ", player.name ," You are in the middle of a forest, what do you want to do ? ")
    while player.health > 0 or boss.boss_dead == True:
        player_input = (input("Your movement : "))
        
        if player_input == "up" or player_input == "UP":
            print(player.postion_y)
            player.postion_y = player.postion_y - 1
            print(player.postion_y)
            verify_player_position(player)
            
        elif player_input == "down" or player_input == "DOWN":
            player.postion_y = player.postion_y + 1
            verify_player_position(player)
            
        elif player_input == "right" or player_input == "RIGHT":
            player.postion_x = player.postion_x + 1
            verify_player_position(player)
            
        elif player_input == "left" or player_input == "LEFT":
            player.postion_x = player.postion_x - 1
            verify_player_position(player)
            
        else:
            print("Please enter a good direction")


def verify_player_position(player):
    print("x : ", player.postion_x, " y : ", player.postion_y )
    if player.postion_x >= 3 and player.postion_y >= 0 and player.postion_x <= 6 and player.postion_y <= 6:
        print("You are in the Forest")
        
    if player.postion_x >= 0 and player.postion_y >= 0 and player.postion_x <= 2 and player.postion_y <= 3:
        print("You are in the Dungeon")
        
    if player.postion_x >= 0 and player.postion_y >= 4 and player.postion_x <= 2 and player.postion_y <= 6:
        print("You are in the Cave")