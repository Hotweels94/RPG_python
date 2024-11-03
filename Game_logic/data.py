from Classes.character import *
from Classes.object import *
from Classes.weapon import *
from Classes.event import *
from Classes.shop import *
from Game_logic.map import random_position_without_exclude_coordinates

# Creation of the player
player = Player("")

# Spawn coordinates of player and boss. It's forbidden because nothing spawn on their cases
forbidden_coords = [(3, 3), (0, 0)]

# Creation of the boss
boss = Boss("Dragon",10,1000,50,20,0,0,25,4,25, 0, 1000, "WoW, The dragon burned you !! ")

# Creation of all of the objects
list_objects = [
    health_potion("health potion", 10, *random_position_without_exclude_coordinates(forbidden_coords), 0),
    health_potion("health potion", 10, *random_position_without_exclude_coordinates(forbidden_coords), 0),
    attack_potion("attack potion", 10, *random_position_without_exclude_coordinates(forbidden_coords), 0),
    attack_potion("attack potion", 10, *random_position_without_exclude_coordinates(forbidden_coords), 0),
    defense_potion("defense potion", 5, *random_position_without_exclude_coordinates(forbidden_coords), 0),
    defense_potion("defense potion", 5, *random_position_without_exclude_coordinates(forbidden_coords), 0)
]

# Creation of all of the monsters
list_monster = [
    Monster("Wolf",1, 50, 5, 2, *random_position_without_exclude_coordinates(forbidden_coords), 10, 1.5, 20, 10 ,150, "Oh the wolf bite your head !!"),
    Monster("Gobelin",2, 75, 10, 4, *random_position_without_exclude_coordinates(forbidden_coords), 12, 1.7, 18, 20 ,200, "Oh the gobelin cut you with his sword !!"),
    Monster("Orc",4, 100, 15, 6, *random_position_without_exclude_coordinates(forbidden_coords), 18, 2, 22, 250, 50, "Wow the orc cut you up with his axe !!"),
    Monster("Elf",5, 115, 18, 7, *random_position_without_exclude_coordinates(forbidden_coords), 18, 1.7, 18, 250, 70, "Incredible the elf hit you with his arrow !!")
]

# Creation of all of the weapons
list_weapon = [
    Weapon("knife", 1, 0, 0, -1, -1, 0),
    Weapon("sword", 1.5, 2, 3, *random_position_without_exclude_coordinates(forbidden_coords), 0),
    Weapon("bow", 1.7, 10, 12, *random_position_without_exclude_coordinates(forbidden_coords), 0),
    Weapon("axe", 1.8, 10, 15, *random_position_without_exclude_coordinates(forbidden_coords), 0)
]

list_monster.append(boss)

list_event = [
    Thunder(5, 3, 4),
    Trap(15, 3, 5),
    Found_gold(25, 3, 6)
]

list_potion_shop = [
    health_potion("health potion", 10, -1, -1, 10),
    attack_potion("attack potion", 10, -1, -1, 20)
]

list_shop = [
    PotionShop(list_potion_shop, 5, 5)
]