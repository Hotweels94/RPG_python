from Classes.character import *
from Classes.object import *
from Classes.weapon import *
from Game_logic.map import random_position_without_exclude_coordinates

# Creation of the player
player = Player("")

# Spawn coordinates of player and boss. It's forbidden because nothing spawn on their cases
forbidden_coords = [(3, 3), (0, 0)]

# Creation of the boss
boss = Boss("Dragon",10,1000,50,20,0,0,25,4,25, 1000, "WoW, The dragon burned you !! ")

# Creation of all of the objects
list_objects = [
    health_potion("health potion", 10, *random_position_without_exclude_coordinates(forbidden_coords)),
    health_potion("health potion", 10, *random_position_without_exclude_coordinates(forbidden_coords)),
    attack_potion("attack potion", 10, *random_position_without_exclude_coordinates(forbidden_coords)),
    attack_potion("attack potion", 10, *random_position_without_exclude_coordinates(forbidden_coords)),
    defense_potion("defense potion", 5, *random_position_without_exclude_coordinates(forbidden_coords)),
    defense_potion("defense potion", 5, *random_position_without_exclude_coordinates(forbidden_coords))
]

# Creation of all of the monsters
list_monster = [
    Monster("Wolf",1, 50, 5, 2, *random_position_without_exclude_coordinates(forbidden_coords), 10, 1.5, 20, 150, "Oh the wolf bite your head !!"),
    Monster("Gobelin",2, 75, 10, 4, *random_position_without_exclude_coordinates(forbidden_coords), 12, 1.7, 18, 200, "Oh the gobelin cut you with his sword !!"),
    Monster("Orc",4, 100, 15, 6, *random_position_without_exclude_coordinates(forbidden_coords), 18, 2, 22, 250, "Wow the orc cut you up with his axe !!"),
    Monster("Elf",5, 115, 18, 7, *random_position_without_exclude_coordinates(forbidden_coords), 18, 1.7, 18, 250, "Incredible the elf hit you with his arrow !!")
]

# Creation of all of the weapons
list_weapon = [
    Weapon("knife", 1, 0, 0, 3, 3),
    Weapon("sword", 1.5, 2, 3, *random_position_without_exclude_coordinates(forbidden_coords)),
    Weapon("bow", 1.7, 10, 12, *random_position_without_exclude_coordinates(forbidden_coords)),
    Weapon("axe", 1.8, 10, 15, *random_position_without_exclude_coordinates(forbidden_coords))
]

list_monster.append(boss)