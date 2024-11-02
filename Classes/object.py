class Object:
    
    def __init__(self, name, value, position_x, position_y):
        self.name = name
        self.value = value
        self.position_x = position_x
        self.position_y = position_y
        self.used = False
        
    def Use(self, Player):
        pass
      
    def End_effect(self, Player):
      pass
    
class health_potion (Object):
  def use(self,Player):
    Player.health += self.value

class attack_potion (Object):
  def use(self,Player):
    Player.attack += self.value
    self.used = True
  
  def End_effect(self, Player):
    if self.used == True :
      Player.attack -= self.value

class defense_potion (Object):
  def use(self,Player):
    Player.defense += self.value
    self.used = True
    
  def End_effect(self, Player):
    if self.used == True :
      Player.defense -= self.value
    
        