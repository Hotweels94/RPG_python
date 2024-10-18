from character import *

def start_game():
    player = Player((input("Enter your name: ")))
    boss = Boss("Boss",10,1000,50,20,6,6)
    
    print("You are int the middle of a forest, what do you want to do ? ")
    while player.health > 0 or boss.boss_dead == True:


    