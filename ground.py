import random
class Field:

    def __init__(self):
        FIELD = [['cucumber', 'peas', 'carrot', 'pepper', 'onion', 'tomato'],
                 ['pepper', 'onion', 'cucumber', 'peas', 'tomato', 'carrot'],
                 ['peas', 'tomato', 'pepper', 'carrot', 'cucumber', 'onion'],
                 ['cucumber', 'pepper', 'onion', 'carrot', 'peas', 'tomato']]
        for i in range(4):
            side = random.randrange(-1, 2, 2)
            FIELD[i] = FIELD[i][::side]
            random.shuffle(FIELD)
        self.field = FIELD
        print(self.field)