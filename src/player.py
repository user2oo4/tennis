class Player:
    def __init__(self, player_id, name, country):
        self.player_id = player_id
        self.name = name
        self.country = country
    
    def __repr__(self):
        return f"Player({self.player_id}, {self.name}, {self.country})"
    