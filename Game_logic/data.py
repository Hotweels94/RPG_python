from Classes.character import *
from Classes.object import *
from Game_logic.map import random_position_without_exclude_coordinates

# Creation of the player
player = Player("")

# Spawn coordinates of player and boss. It's forbidden because nothing spawn on their cases
forbidden_coords = [(3, 3), (0, 0)]

# Creation of the boss
boss = Boss("Dragon",10,1000,50,20,0,0,25,4,25, 1000, "WoW, The dragon burned you !! ")

# Creation of all of the objects
list_objects = [
    health_potion("health potion", 10, 2, 2),
    attack_potion("attack potion", 10, *random_position_without_exclude_coordinates(forbidden_coords)),
    defense_potion("defense potion", 5, *random_position_without_exclude_coordinates(forbidden_coords))
]

# Creation of all of the monsters
list_monster = [
    Monster("Wolf",1, 50, 5, 2, 1,1, 10, 1.5, 20, 150, "Oh the wolf bite your head !!"),
    Monster("Wolf",1, 50, 5, 2, 4,4, 10, 1.5, 20, 20, "Oh the wolf bite your head !!"),
    Monster("Wolf",1, 50, 5, 2, 5,5, 10, 1.5, 20, 70, "Oh the wolf bite your head !!")
]


