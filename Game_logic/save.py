import pickle

# Function to save the game with pickle
def save(player, list_monster, list_objects, list_weapon, list_event, file="save.pkl"):
    with open(file, "wb") as f:
        pickle.dump({
            "player": player,
            "monsters": list_monster,
            "objects": list_objects,
            "weapon": list_weapon,
            "event": list_event
        }, f)
    print("Game Save !")
    exit()
   
# Function to load the game with pickle
def load(file="save.pkl"):
    try:
        with open(file, "rb") as f:
            data = pickle.load(f)
            player = data["player"]
            list_monster = data["monsters"]
            list_objects = data["objects"]
            list_weapon = data["weapon"]
            list_event = data["event"]
            print("Game loaded successfully!")
            return player, list_monster, list_objects, list_weapon, list_event
    except FileNotFoundError:
        print("No save file found.")
        return None, None, None, None, None