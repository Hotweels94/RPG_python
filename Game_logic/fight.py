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
                print("1. You can attack with one of your weapons")
                print("2. You can use an object from your inventory")
                print("3. Or you can run away")
                
                player_input = input("Your choice (1, 2 or 3) : ")
                print("\n")
                
                # Player choose to fight
                if player_input == "1":
                    player.attack_action(monster)
                    
                    # If the monster is dead we remove it of the list and give xp to the player
                    if monster.health <= 0: 
                        
                        os.system('cls')
                        list_monster.remove(monster)
                        player.xp += monster.drop_xp
                        player.gold += monster.gold
                        player.temp_attack = 0
                        player.temp_defence = 0
                        print("YOU KILLED THE LEVEL ",monster.level, monster.name + "!")
                        print("You win : ", monster.gold, " gold coins !")
                        if type(monster) == Boss:
                            monster.boss_dead = True
                        
                        # Player level up if he has enough xp
                        while player.xp >= player.max_xp:
                            player.level_up()
                
                # Player choose to use an object
                elif player_input == "2":
                    player.use_inventory()
                
                # Player choose to run away
                elif player_input == "3":
                    if type(monster) != Boss:
                        player.run_away(monster)
                        break
                    else:
                        print("You can't run away from this fight !")
                
                else: 
                    print("For next round, type 1, 2 or 3. Don't fail please ")
                    continue
            

                # Monster's turn
                if monster.health > 0:
                    monster.monster_fight(player)
                
            # Player dead
            if player.health <= 0:
                print("YOU ARE DEAD !!")
                print("Game Over")
                exit()
            break