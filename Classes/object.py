class Object:
    def __init__(self, name, value, position_x, position_y, price):
        self.name = name
        self.value = value
        self.position_x = position_x
        self.position_y = position_y
        self.price = price
        
    def Use(self, Player):
        pass
    
class health_potion (Object):
  def use(self,Player):
    Player.health += self.value

class attack_potion (Object):
  def use(self,Player):
    Player.temp_attack += self.value

class defence_potion (Object):
  def use(self,Player):
    Player.temp_defence += self.value
    
        