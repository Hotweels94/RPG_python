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
    
  def level_up(self):
    print("YOU LEVEL UP ! You are level ", self.level, " You have better stats !")
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