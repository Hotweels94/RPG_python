class Object:
    
    def __init__(self, name, value, position_x, position_y,):
        self.name = name
        self.value = value
        self.position_x = position_x
        self.position_y = position_y
        
    def Use(self, Character):
        pass
    
class health_potion (Object):
  def use(self,Player):
    Player.health += self.value
  
  def to_dict(self):
      return {
        "name": self.name,
        "value": self.value,
        "position_x": self.position_x,
        "position_y": self.position_y
    }

class attack_potion (Object):
  def use(self,Player):
    Player.attack += self.value
    
  def to_dict(self):
      return {
        "name": self.name,
        "value": self.value,
        "position_x": self.position_x,
        "position_y": self.position_y
    }

class defense_potion (Object):
  def use(self,Player):
    Player.defense += self.value
    
  def to_dict(self):
      return {
        "name": self.name,
        "value": self.value,
        "position_x": self.position_x,
        "position_y": self.position_y
    }
        