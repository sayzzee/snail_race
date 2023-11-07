class Card:
    def __init__(self, type, value, game_rule=""):
        self.type = type
        self.value = value
        self.game_rule = game_rule
    def __repr__(self):
        if self.game_rule != "":
            if self.type == "sleep" or self.type == "vegetable":
                return f'{self.type}'
            else:
                return f'{self.type}:{self.value} - {self.game_rule}'


        return f'{self.type}:{self.value}'