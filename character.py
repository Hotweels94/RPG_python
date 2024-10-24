class Character :
  def __init__(self, name, level, health, attack, defense, position_x, position_y, critic_hit_chance, critic_hit, miss_hit_chance):
    self.name = name
    self.level = level
    self.xp = 0
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
    
  def level_up(self):
    if self.xp >= 100:
      self.xp = self.xp * self.level_multiplicator
      self.level += 1
      self.level_multiplicator += 0.5
      self.health += 15
      self.attack += 5
      self.defense += 5 
      self.critic_hit_chance += 2
      self.miss_hit_chance -= 1
      self.critic_hit += 0.5
      return True

class Monster (Character):
  def __init__(self, name, level, health, attack, defense, position_x, position_y, critic_hit_chance, critic_hit, miss_hit, drop_xp):
    super().__init__(name,level, health, attack, defense, position_x, position_y, critic_hit_chance, critic_hit, miss_hit)
    self.drop_xp = drop_xp 
    self.run_away = False

class Boss (Monster):
  def __init__(self, name, level, health, attack, defense, position_x, position_y, critic_hit_chance, critic_hit, miss_hit, drop_xp):
    super().__init__(name,level, health, attack, defense, position_x, position_y, critic_hit_chance, critic_hit, miss_hit, drop_xp)
    self.boss_dead = False