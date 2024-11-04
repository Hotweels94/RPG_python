from Classes.character import *
from Classes.object import *
from Classes.weapon import *
from Classes.event import *
from Classes.shop import *
from Game_logic.map import random_position_without_exclude_coordinates

# Creation of the player
player = Player("")

# Spawn coordinates of player, boss and shops. It's forbidden because nothing spawn on their cases
forbidden_coords = [(3, 3), (0, 0), (5, 5), (2, 2)]

# Creation of the boss
boss = Boss("Dragon",10,300,20,10,0,0,20,2,5, 0, 1000, "WoW, The dragon burned you !! ")

# Creation of all of the objects
list_objects = [
    health_potion("health potion", 10, *random_position_without_exclude_coordinates(forbidden_coords), 0),
    health_potion("health potion", 10, *random_position_without_exclude_coordinates(forbidden_coords), 0),
    health_potion("health potion", 10, *random_position_without_exclude_coordinates(forbidden_coords), 0),
    health_potion("big health potion", 30, *random_position_without_exclude_coordinates(forbidden_coords), 0),
    health_potion("big health potion", 30, *random_position_without_exclude_coordinates(forbidden_coords), 0),
    attack_potion("attack potion", 10, *random_position_without_exclude_coordinates(forbidden_coords), 0),
    attack_potion("attack potion", 10, *random_position_without_exclude_coordinates(forbidden_coords), 0),
    defense_potion("defense potion", 5, *random_position_without_exclude_coordinates(forbidden_coords), 0),
    defense_potion("defense potion", 5, *random_position_without_exclude_coordinates(forbidden_coords), 0)
]

# Creation of all of the monsters
list_monster = [
    Monster("Wolf",1, 30, 5, 1, *random_position_without_exclude_coordinates(forbidden_coords), 5, 1.5, 10, 10 ,20, "Oh the wolf bite your head !!"),
    Monster("Wolf",1, 30, 5, 1, *random_position_without_exclude_coordinates(forbidden_coords), 5, 1.5, 10, 10 ,20, "Oh the wolf bite your head !!"),
    Monster("Gobelin",2, 50, 8, 3, *random_position_without_exclude_coordinates(forbidden_coords), 7, 1.6, 8, 20 ,40, "Oh the gobelin cut you with his sword !!"),
    Monster("Gobelin",2, 50, 8, 3, *random_position_without_exclude_coordinates(forbidden_coords), 7, 1.6, 8, 20 ,40, "Oh the gobelin cut you with his sword !!"),
    Monster("Orc",3, 80, 12, 5, *random_position_without_exclude_coordinates(forbidden_coords), 10, 1.75, 6, 35, 80, "Wow the orc cut you up with his axe !!"),
    Monster("Orc",3, 80, 12, 5, *random_position_without_exclude_coordinates(forbidden_coords), 10, 1.75, 6, 35, 80, "Wow the orc cut you up with his axe !!"),
    Monster("Elf",5, 100, 15, 7, *random_position_without_exclude_coordinates(forbidden_coords), 15, 1.82, 10, 50, 100, "Incredible the elf hit you with his arrow !!"),
    Monster("Elf",5, 100, 15, 7, *random_position_without_exclude_coordinates(forbidden_coords), 15, 1.82, 10, 50, 100, "Incredible the elf hit you with his arrow !!")
]

# Creation of all of the weapons
list_weapon = [
    Weapon("knife", 1, 0, 0, -1, -1, 0),
    Weapon("sword", 1.5, 2, 3, *random_position_without_exclude_coordinates(forbidden_coords), 0),
    Weapon("bow", 1.7, 10, 12, *random_position_without_exclude_coordinates(forbidden_coords), 0),
    Weapon("axe", 1.8, 10, 15, *random_position_without_exclude_coordinates(forbidden_coords), 0)
]

list_monster.append(boss)

# Creation of all of the events
list_event = [
    Thunder(5, *random_position_without_exclude_coordinates(forbidden_coords)),
    Trap(15, *random_position_without_exclude_coordinates(forbidden_coords)),
    Trap(15, *random_position_without_exclude_coordinates(forbidden_coords)),
    Found_gold(25, *random_position_without_exclude_coordinates(forbidden_coords)),
    Found_gold(25, *random_position_without_exclude_coordinates(forbidden_coords)),
    Found_gold(25, *random_position_without_exclude_coordinates(forbidden_coords))
]

# Creation of all of the potion in the shop
list_potion_shop = [
    health_potion("health potion", 10, -1, -1, 25),
    health_potion("big health potion", 30, -1, -1, 35),
    attack_potion("attack potion", 10, -1, -1, 40)
]

# Creation of all of the weapon in the shop
list_weapon_shop = [
    Weapon("katana", 1.6, 3, 3, -1, -1, 50),
    Weapon("Dagger", 2, 20, 25, -1, -1, 75)
]

# Creation of all of the shop
list_shop = [
    PotionShop(list_potion_shop, 5, 5),
    WeaponShop(list_weapon_shop, 2, 2)
]
