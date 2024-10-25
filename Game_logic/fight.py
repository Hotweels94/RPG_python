import os
from Classes.character import *
from Classes.object import *
from random import randrange

# Fight func 
def fight(player, list_monster):
    
    # For the monster in the list 
    for monster in list_monster:
        if player.position_x == monster.position_x and player.position_y == monster.position_y:
            os.system('cls')
            print("YOU'VE FOUND A LEVEL ",monster.level, monster.name + " !")
            
            # While both are alive
            while player.health > 0 and monster.health > 0:
                print("What do you want to do ? \n")
                print("1. You can attack with your weapon : ", player.weapon)
                print("2. You can use an object from your inventory")
                print("3. Or you can run away (the monster will diseapear but you will don't win any xp)")
                
                player_input = input("Your choice (1, 2 or 3) : ")
                print("\n")
                
                # Player choose to fight
                if player_input == "1":
                    player_test = randrange(1,100)
                    
                    # Critic hit
                    if player_test < player.critic_hit_chance:
                        monster.health -= player.attack * player.critic_hit * player.weapon_stat - monster.defense
                        print("CRITIC HIT !")
                        print(monster.name, " has ", monster.health, " HP")
                        
                    # Miss
                    elif player_test > 100 - player.miss_hit_chance:
                        print("Oof, you miss !")
                        
                    # Normal hit
                    else:
                        monster.health -= player.attack * player.weapon_stat - monster.defense
                        print("You hit him !")
                        print(monster.name, " has ", monster.health, " HP")
                        
                    print("\n")
                
                # Player choose to use an object
                elif player_input == "2":
                    print("Your objects : \n")   
                    for obj in player.inventory:
                        print(obj.name) 
                        
                    player_input = input("Your choice (name of the object or quit) : ")
                    if player_input == "quit": 
                        print("You quit")
                        
                    selected_obj = None
                    for obj in player.inventory:
                        if obj.name == player_input:
                            selected_obj = obj
                            break
                    
                    # Player choice
                    if player_input != "quit":
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
                
                # Player choose to run away
                elif player_input == "3":
                    print("You ran away !")
                    print("\n")
                    monster.run_away = True
                    monster.health = 0
            
                # The monster fight
                monster_test = randrange(1,100)
                
                # Special hit
                if monster_test < monster.critic_hit_chance:
                    player.health -= monster.attack * monster.critic_hit - player.defense
                    print(monster.special_hit)
                    print("You have ", player.health, " HP")
                    
                # Miss
                elif monster_test > 100 - monster.miss_hit_chance:
                    print("Nice, ", monster.name, "doesn't hit you")
                    print("You have ", player.health, " HP")
                    
                # Normal hit
                else:
                    player.health -= monster.attack - player.defense
                    print(monster.name, " hits you !")
                    print("You have ", player.health, " HP")
                    
                print("\n")
                
            # If the monster is dead we remove it of the list and give xp to the player
            if monster.health <= 0 and monster.run_away == False: 
                
                os.system('cls')
                list_monster.remove(monster)
                player.xp += monster.drop_xp
                print("YOU KILL THE",monster.level, monster.name + "!")
                
                # Player level up if he has enough xp
                if player.level_up():
                    print("YOU LEVEL UP ! You are level ", player.level, " You have better stats !")
                
            # Player dead
            if player.health <= 0:
                os.system('cls')
                print("YOU ARE DEAD !!")
                print("Game Over")
                exit()
                 
            # if the player choose to run away
            if monster.run_away == True and monster.health <= 0:
                list_monster.remove(monster)
            break 