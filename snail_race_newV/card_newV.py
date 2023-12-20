class VegetableCard:
    def __init__(self, veggie):
        self.veggie = veggie

    def __repr__(self):
        return (f'{self.veggie}')
class NumberCard:
    def __init__(self, number, arrow):
        self.number = number
        self.arrow = arrow

    def __repr__(self):
        return (f'{self.number} + {self.arrow}')