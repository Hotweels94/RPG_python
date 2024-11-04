class Shop():
    def __init__(self, list_objects_shop, position_x, position_y):
        self.list_objects_shop = list_objects_shop
        self.position_x = position_x
        self.position_y = position_y
        
    def shop_sell(self, player):
        pass
    
class PotionShop(Shop):
    
    # Function of the shop when the player is on the shop case
    def shop_sell(self, player):
        print("Welcome to the potion shop! Here's what we have in stock:")
        for index, obj in enumerate(self.list_objects_shop, start=1):
            print(f"{index}. {obj.name} - price: {obj.price}")
            
        print("What do you want? \n")
        player_input = input("Your choice (name of the object or quit): \n")
        if player_input == "quit": 
            print("You quit")
            return
        
        selected_obj = None
        for obj in self.list_objects_shop:
            if obj.name == player_input:
                selected_obj = obj
                break
            
        if selected_obj:
            if player.gold >= selected_obj.price:
                print(f"You buy a {selected_obj.name}! You have: {player.gold - selected_obj.price} gold coins left.")
                player.gold -= selected_obj.price
                self.list_objects_shop.remove(selected_obj)
                player.inventory.append(selected_obj)
            else:
                print("Not enough money.")
        else:
            print("Item not found in the shop.")


class WeaponShop(Shop):
    
    # Function of the shop when the player is on the shop case
    def shop_sell(self, player):
        print("Welcome to the weapon shop! Here's what we have in stock:")
        for index, obj in enumerate(self.list_objects_shop, start=1):
            print(f"{index}. {obj.name} - price: {obj.price}")
            
        print("What do you want? \n")
        player_input = input("Your choice (name of the weapon or quit): \n")
        if player_input == "quit": 
            print("You quit")
            return
        
        selected_obj = None
        for obj in self.list_objects_shop:
            if obj.name == player_input:
                selected_obj = obj
                break
            
        if selected_obj:
            if player.gold >= selected_obj.price:
                print(f"You buy a {selected_obj.name}! You have: {player.gold - selected_obj.price} gold coins left.")
                player.gold -= selected_obj.price
                self.list_objects_shop.remove(selected_obj)
                player.weapon.append(selected_obj)
            else:
                print("Not enough money.")
        else:
            print("Item not found in the shop.")