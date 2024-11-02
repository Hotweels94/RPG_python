class Event:
    def __init__(self, value, position_x, position_y):
        self.value = value
        self.position_x = position_x
        self.position_y = position_y
        
    def event_effect(self, Player):
        pass
    
    
class Thunder (Event):
    def event_effect(self, Player):
        Player.health -= self.value
        print("You were hit by lightning, you have now ", Player.health, " HP.")
        
class Trap (Event):
    def event_effect(self, Player):
        Player.health -= self.value
        print("You stepped on a goblin's trap, you have now ", Player.health, " HP.")
        
class Found_gold (Event):
    def event_effect(self, Player):
        Player.gold += self.value
        print("Oh it's a lucky day ! You've found : ", self.value, " gold coins on the ground ! You have now : ", Player.gold, " gold coins !")