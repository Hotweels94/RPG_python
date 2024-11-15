from random import randrange

class Character :
  def __init__(self, name, level, health, attack, defence, position_x, position_y, critic_hit_chance, critic_hit, miss_hit_chance, gold):
    self.name = name
    self.level = level
    self.xp = 0
    self.max_xp = 100
    self.level_multiplicator = 1
    self.health = health
    self.attack = attack
    self.defence = defence
    self.inventory = []
    self.position_x = position_x
    self.position_y = position_y
    self.critic_hit_chance = critic_hit_chance
    self.critic_hit = critic_hit
    self.miss_hit_chance = miss_hit_chance
    self.gold = gold

class Player (Character):
  def __init__(self, name):
    super().__init__(name, 1, 100, 10, 3, 3, 3, 10, 2, 15, 50)
    self.weapon = []
    self.temp_attack = 0
    self.temp_defence = 0
    
  # First choice in fight, the player attack his enemy
  def attack_action(self, monster):
    
    print("Your weapons :")
    print("\n")
    for wea in self.weapon:
      print(wea.name, ": Stat : ", wea.stat , " Miss chance more stat : ", wea.miss_chance_hit, " Critic chance more stat : ", wea.critic_chance_hit)
    
    player_weapon_choice = input("Name of your weapon : ")
    
    selected_weapon = None
    for wea in self.weapon:
      if wea.name == player_weapon_choice:
        selected_weapon = wea
        break
    
    try:
      player_test = randrange(1,100)      
      # Critic hit
      if player_test < selected_weapon.critic_chance_hit + self.critic_hit_chance:
          monster.health -= ( self.attack + self.temp_attack ) * self.critic_hit * selected_weapon.stat - monster.defence
          print("CRITIC HIT !")
          if monster.health < 0:
            monster.health = 0
          print(monster.name, " has ", monster.health, " HP")
          
      # Miss
      elif player_test > 100 - (selected_weapon.miss_chance_hit + self.miss_hit_chance):
          print("Oof, you miss !")
          
      # Normal hit
      else:
          monster.health -= ( self.attack + self.temp_attack ) * selected_weapon.stat - monster.defence
          print("You hit him !")
          if monster.health < 0:
            monster.health = 0
          print(monster.name, " has ", monster.health, " HP")
    except:
      print("Next time write the name of the weapon please")
        
    print("\n")
    
  # Second choice, he can use an object from his inventory
  def use_inventory(self):
    print("Your objects : \n")   
    for obj in self.inventory:
        print(obj.name) 
        
    player_input = input("Your choice (name of the object or quit) : ")
    if player_input == "quit": 
        print("You quit")
        
    selected_obj = None
    for obj in self.inventory:
        if obj.name == player_input:
            selected_obj = obj
            break
    
    # Player choice
    if player_input != "quit":
        if selected_obj:
            selected_obj.use(self)
            if player_input == "health potion":
                print("You use your health_potion! You have: ", self.health, " HP")
            elif player_input == "attack potion":
                print("You use your attack_potion! You have: ", self.attack, " attack points more")
            elif player_input == "defence potion":
                print("You use your defence_potion! You have: ", self.defence, " defence points more")
            self.inventory.remove(selected_obj)

        else:
            print("Invalid object name.")
        print("\n")
      
  # Third option, he can run away
  def run_away(self, monster):
    print("You ran away !")
    print("\n")
     
  # Level up method if the player has more xp than he need to level up
  def level_up(self):
    self.xp -= self.max_xp
    self.level += 1
    self.level_multiplicator += 0.5
    self.max_xp = self.max_xp * self.level_multiplicator
    self.health += 15
    self.attack += 5
    self.defence += 5 
    self.critic_hit_chance += 2
    self.miss_hit_chance -= 1
    self.critic_hit += 0.5
    print("YOU LEVEL UP ! You are level ", self.level, " You have better stats ! \n")
    return True

  # Show player stats
  def print_player_stats(self):
    print(f"Your stats:")
    print(f"Name: {self.name}")
    print(f"Level: {self.level}")
    print(f"XP: {self.xp}/{self.max_xp}")
    print(f"Health: {self.health}")
    print(f"Attack: {self.attack}")
    print(f"Defence: {self.defence}")
    print(f"Position: ({self.position_x}, {self.position_y})")
    print(f"Critic Hit Chance: {self.critic_hit_chance}%")
    print(f"Critic Hit Multiplier: {self.critic_hit}")
    print(f"Miss Hit Chance: {self.miss_hit_chance}%")
    print(f"Gold: {self.gold}")
    print("\n")

class Monster (Character):
  def __init__(self, name, level, health, attack, defence, position_x, position_y, critic_hit_chance, critic_hit, miss_hit, gold, drop_xp, special_hit):
    super().__init__(name,level, health, attack, defence, position_x, position_y, critic_hit_chance, critic_hit, miss_hit, gold)
    self.drop_xp = drop_xp 
    self.special_hit = special_hit
    
  # The monster fight
  def monster_fight(self, player):
    monster_test = randrange(1,100)
    
    # Special hit
    if monster_test < self.critic_hit_chance:
        player.health -= self.attack * self.critic_hit - ( player.defence + player.temp_defence)
        print(self.special_hit)
        print("You have ", player.health, " HP")
        
    # Miss
    elif monster_test > 100 - self.miss_hit_chance:
        print("Nice, ", self.name, "doesn't hit you")
        print("You have ", player.health, " HP")
        
    # Normal hit
    else:
        player.health -= self.attack - ( player.defence + player.temp_defence)
        print(self.name, " hits you !")
        print("You have ", player.health, " HP")
        
    print("\n")

class Boss (Monster):
  def __init__(self, name, level, health, attack, defence, position_x, position_y, critic_hit_chance, critic_hit, miss_hit, gold, drop_xp, special_hit):
    super().__init__(name,level, health, attack, defence, position_x, position_y, critic_hit_chance, critic_hit, miss_hit, gold ,drop_xp, special_hit)
    self.boss_dead = False