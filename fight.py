from character import *
from object import *
from random import randrange

def fight(player, list_monster):
    for monster in list_monster:
        if player.position_x == monster.position_x and player.position_y == monster.position_y:
            print("YOU'VE FOUND A LEVEL ",monster.level, monster.name + " !")
            while player.health > 0 and monster.health > 0:
                print("What do you want to do ? ")
                print("1. You can attack with your weapon : ", player.weapon)
                print("2. Or you can use an object from your inventory")
                
                player_input = input("Your choice (1 or 2) : ")
                if player_input == "1":
                    player_test = randrange(1,100)
                    if player_test < player.critic_hit_chance:
                        monster.health -= player.attack * player.critic_hit 
                        print("CRITIC HIT !")
                        print(monster.name, " has ", monster.health, " HP")
                    elif player_test > 100 - player.miss_hit_chance:
                        print("Oof, you miss !")
                    else:
                        monster.health -= player.attack
                        print("You hit him !")
                        print(monster.name, " has ", monster.health, " HP")
                    print("\n")
                
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
            
            if monster.health <= 0:
                list_monster.remove(monster)
                player.xp += monster.drop_xp
                print("YOU KILL THE",monster.level, monster.name + "!")
                if player.level_up():
                    print("YOU LEVEL UP ! You are level ", player.level, " You have better stats !")
            break 