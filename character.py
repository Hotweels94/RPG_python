class Character :
  def __init__(self, name, level, health, attack, defense, postion_x, postion_y, critic_hit, miss_hit):
    self.name = name
    self.level = level
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

class Monster (Character):
  def __init__(self, name, level, health, attack, defense, postion_x, postion_y, critic_hit, miss_hit):
    super().__init__(name,level, health, attack, defense, postion_x, postion_y, critic_hit, miss_hit)

class Boss (Monster):
  def __init__(self, name, level, health, attack, defense, postion_x, postion_y, critic_hit, miss_hit):
    super().__init__(name,level, health, attack, defense, postion_x, postion_y, critic_hit, miss_hit)
    self.boss_dead = False