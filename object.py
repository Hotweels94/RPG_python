class Object:
    
    def __init__(self, name, value, postion_x, postion_y,):
        self.name = name
        self.value = value
        self.postion_x = postion_x
        self.postion_y = postion_y
        
    def Use(self, Character):
        pass
    
class health_potion (Object):
  def use(self,Player):
    Player.health += self.value

class attack_potion (Object):
  def use(self,Player):
    Player.attack += self.value

class defense_potion (Object):
  def use(self,Player):
    Player.defense += self.value
        