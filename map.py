from character import *
from object import *

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
    
def fight(player, list_monster):
    for monster in list_monster:
        if player.postion_x == monster.postion_x and player.postion_y == monster.postion_y:
            print("YOU'VE FOUND A LEVEL ",monster.level, monster.name + "!")
            while player.health > 0 and monster.health > 0:
                print("What do you want to do ? ")
                print("1. You can attack with your weapon : ", player.weapon)
                print("2. Or you can use an object from your inventory")
                
                player_input = input("Your choice (1 or 2) : ")
                if player_input == "1":
                    pass
                
                elif player_input == "2":
                    print("Your objects :")   
                    for obj in player.inventory:
                        print(obj.name) 
                        
                    player_input = input("Your choice (name of the object) : ")
                    selected_obj = None
                    for obj in player.inventory:
                        if obj.name == player_input:
                            selected_obj = obj
                            break
                    
                    if selected_obj:
                        selected_obj.use(player)
                        if player_input == "health potion":
                            print("You use your health_potion! You have: ", player.health, " HP")
                        elif player_input == "attack potion":
                            print("You use your attack_potion! You have: ", player.attack, " attack points")
                        elif player_input == "defense potion":
                            print("You use your defense_potion! You have: ", player.defense, " defense points")
                        player.inventory.remove(selected_obj)
                    else:
                        print("Invalid object name.")
                    print("\n")
                    
            list_monster.remove(monster)
            break 