class Character :
  def __init__(self, name, level, health, attack, defense, postion_x, postion_y, critic_hit, miss_hit):
    self.name = name
    self.level = level
    self.xp = 0
    self.level_multiplicator = 1
    self.health = health
    self.attack = attack
    self.defense = defense
    self.inventory = []
    self.postion_x = postion_x
    self.postion_y = postion_y
    self.critic_hit = critic_hit
    self.miss_hit = miss_hit

class Player (Character):
  def __init__(self, name):
    super().__init__(name,1,100,10,5,3,3,10,15)
    self.weapon = "knife"
    
  def level_up(self):
    if self.xp >= 100:
      self.xp = self.xp * self.level_multiplicator
      self.level += 1
      self.level_multiplicator += 0.5
      self.health += 15
      self.attack += 5
      self.defense += 5 
      self.critic_hit += 2
      self.miss_hit -= 1

class Monster (Character):
  def __init__(self, name, level, health, attack, defense, postion_x, postion_y, critic_hit, miss_hit):
    super().__init__(name,level, health, attack, defense, postion_x, postion_y, critic_hit, miss_hit)

class Boss (Monster):
  def __init__(self, name, level, health, attack, defense, postion_x, postion_y, critic_hit, miss_hit):
    super().__init__(name,level, health, attack, defense, postion_x, postion_y, critic_hit, miss_hit)
    self.boss_dead = False