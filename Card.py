import csv
import random

class Card:
    def __init__(self, gem_type, cost, points, level):
        self.gem_type = gem_type
        self.cost = cost
        self.points = points
        self.level = level

    def get_gem_type(self):
        return self.gem_type

    def get_cost(self):
        return self.cost

    def get_points(self):
        return self.points

    def get_level(self):
        return self.level

class CardList:
    def __init__(self):
        self.level1 = []
        self.level2 = []
        self.level3 = []
        with open('data/cardlist.csv', 'r') as file:
            # Create a reader object and skip the first row of csv file
            reader = csv.reader(file, delimiter=';')
            next(reader) 
            # Iterate through the rows of the file. Each row contains Color;green;red;blue;white;black;WP;Level
            for row in reader:
                # convert the list of cost of gems into int
                temp = [row[1], row[2], row[3], row[4], row[5]]
                cost = [int(x) if x else 0 for x in temp]
                # Create a Card object and set its attributes
                new_card = Card(row[0], cost, int(row[6]), int(row[7]))
                if new_card.get_level() == 1 :
                    self.level1.append(new_card)
                elif new_card.get_level() == 2 :
                    self.level2.append(new_card)
                elif new_card.get_level() == 3 :
                    self.level3.append(new_card)
        # shuffle the cards
        random.shuffle(self.level1)
        random.shuffle(self.level2)
        random.shuffle(self.level3)


    def new_card(self, level):
        # returns a card to the board and removes it from the deck
        if level == 1 and self.level1:
            return self.level1.pop(0)
        elif level == 2 and self.level2:
            return self.level2.pop(0)
        elif level == 3 and self.level3:
            return self.level3.pop(0)
        else:
            return None # no more cards left in deck
            
'''
list = CardList()
new_card = list.new_card(1)
print(new_card.get_gem_type(), new_card.get_cost(), new_card.get_points(), new_card.get_level())
'''