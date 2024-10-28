from random import randrange

class Character :
  def __init__(self, name, level, health, attack, defense, position_x, position_y, critic_hit_chance, critic_hit, miss_hit_chance):
    self.name = name
    self.level = level
    self.xp = 0
    self.max_xp = 100
    self.level_multiplicator = 1
    self.health = health
    self.attack = attack
    self.defense = defense
    self.inventory = []
    self.position_x = position_x
    self.position_y = position_y
    self.critic_hit_chance = critic_hit_chance
    self.critic_hit = critic_hit
    self.miss_hit_chance = miss_hit_chance

class Player (Character):
  def __init__(self, name):
    super().__init__(name, 1, 100, 10, 3, 3, 3, 10, 2, 15)
    self.weapon = "knife"
    self.weapon_stat = 1
    
  def to_dict(self):
    return {
      "name": self.name,
      "level": self.level,
      "xp": self.xp,
      "max_xp": self.max_xp,
      "level_multiplicator": self.level_multiplicator,
      "health": self.health,
      "attack": self.attack,
      "defense": self.defense,
      "inventory": self.inventory,
      "position_x": self.position_x,
      "position_y": self.position_y,
      "critic_hit_chance": self.critic_hit_chance,
      "critic_hit": self.critic_hit,
      "miss_hit_chance": self.miss_hit_chance,
      "weapon": self.weapon,
      "weapon_stat": self.weapon_stat
    }
    
  # First choice in fight, the player attack his enemy
  def attack_action(self, monster):
    player_test = randrange(1,100)      
    # Critic hit
    if player_test < self.critic_hit_chance:
        monster.health -= self.attack * self.critic_hit * self.weapon_stat - monster.defense
        print("CRITIC HIT !")
        if monster.health < 0:
          monster.health = 0
        print(monster.name, " has ", monster.health, " HP")
        
    # Miss
    elif player_test > 100 - self.miss_hit_chance:
        print("Oof, you miss !")
        
    # Normal hit
    else:
        monster.health -= self.attack * self.weapon_stat - monster.defense
        print("You hit him !")
        if monster.health < 0:
          monster.health = 0
        print(monster.name, " has ", monster.health, " HP")
        
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
                print("You use your attack_potion! You have: ", self.attack, " attack points")
            elif player_input == "defense potion":
                print("You use your defense_potion! You have: ", self.defense, " defense points")
            self.inventory.remove(selected_obj)

        else:
            print("Invalid object name.")
        print("\n")
      
  # Third option, he can run away
  def run_away(self, monster):
    print("You ran away !")
    print("\n")
    monster.run_away = True
    monster.health = 0
     
  # Level up method if the player has more xp than he need to level up
  def level_up(self):
    self.xp = 0
    self.level += 1
    self.level_multiplicator += 0.5
    self.max_xp = self.max_xp * self.level_multiplicator
    self.health += 15
    self.attack += 5
    self.defense += 5 
    self.critic_hit_chance += 2
    self.miss_hit_chance -= 1
    self.critic_hit += 0.5
    print("YOU LEVEL UP ! You are level ", self.level, " You have better stats ! \n")
    return True

class Monster (Character):
  def __init__(self, name, level, health, attack, defense, position_x, position_y, critic_hit_chance, critic_hit, miss_hit, drop_xp, special_hit):
    super().__init__(name,level, health, attack, defense, position_x, position_y, critic_hit_chance, critic_hit, miss_hit)
    self.drop_xp = drop_xp 
    self.run_away = False
    self.special_hit = special_hit
    
  def to_dict(self):
    return {
      "name": self.name,
      "level": self.level,
      "health": self.health,
      "attack": self.attack,
      "defense": self.defense,
      "position_x": self.position_x,
      "position_y": self.position_y,
      "critic_hit_chance": self.critic_hit_chance,
      "critic_hit": self.critic_hit,
      "miss_hit_chance": self.miss_hit_chance,
      "drop_xp": self.drop_xp,
      "run_away": self.run_away,
      "special_hit": self.special_hit
    }

class Boss (Monster):
  def __init__(self, name, level, health, attack, defense, position_x, position_y, critic_hit_chance, critic_hit, miss_hit, drop_xp, special_hit):
    super().__init__(name,level, health, attack, defense, position_x, position_y, critic_hit_chance, critic_hit, miss_hit, drop_xp, special_hit)
    self.boss_dead = False
    
  def to_dict(self):
    return {
      "name": self.name,
      "level": self.level,
      "health": self.health,
      "attack": self.attack,
      "defense": self.defense,
      "position_x": self.position_x,
      "position_y": self.position_y,
      "critic_hit_chance": self.critic_hit_chance,
      "critic_hit": self.critic_hit,
      "miss_hit_chance": self.miss_hit_chance,
      "drop_xp": self.drop_xp,
      "special_hit": self.special_hit,
      "boss_dead": self.boss_dead
    }