from Classes.character import *
from Classes.object import *
from random import randint

# Verify position of the player on the map
def verify_player_position(player):
    
    print("x : ", player.position_x, " y : ", player.position_y )
    if player.position_x >= 3 and player.position_y >= 0 and player.position_x <= 6 and player.position_y <= 6:
        print("You are in the Forest \n")
        return True
        
    if player.position_x >= 0 and player.position_y >= 0 and player.position_x <= 2 and player.position_y <= 3:
        print("You are in the Dungeon \n")
        return True
        
    if player.position_x >= 0 and player.position_y >= 4 and player.position_x <= 2 and player.position_y <= 6:
        print("You are in the Cave \n")
        return True
    
    if player.position_x < 0 or player.position_y < 0 or player.position_x > 6 or player.position_y > 6:
        return False
    
    return True

# Verify if the player found an object
def verify_object_and_player_position(player, list_objects):
    for obj in list_objects:
        if player.position_x == obj.position_x and player.position_y == obj.position_y:
            player.inventory.append(obj)
            print("YOU'VE FOUND AN OBJECT ! :", obj.name)
            list_objects.remove(obj)
            break 

def random_position_without_exclude_coordinates(forbidden_coords):
    while True:
        x = randint(0, 6)
        y = randint(0, 6)
        if (x, y) not in forbidden_coords:
            return (x, y)