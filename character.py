class Character :
  def __init__(self, name, level, health, attack, defense, postion_x, postion_y):
    self.name = name
    self.level = level
    self.health = health
    self.attack = attack
    self.defense = defense
    self.inventory = []
    self.postion_x = postion_x
    self.postion_y = postion_y

class Player (Character):
  def __init__(self, name):
    super().__init__(name,1,100,10,5,3,3)

class Monster (Character):
  def __init__(self, name, level, health, attack, defense, postion_x, postion_y):
    super().__init__(name,level, health, attack, defense, postion_x, postion_y)

class Boss (Monster):
  def __init__(self, name, level, health, attack, defense, postion_x, postion_y):
    super().__init__(name,level, health, attack, defense, postion_x, postion_y)
    self.boss_dead = False