class Player:
    def __init__(self, name):
        self.name = name
        self.gems = {'blue': 0, 'green': 0, 'black': 0, 'red': 0, 'white': 0, 'gold': 0}
        self.gem_limit = 10
        self.points = 0
        self.pur_cards_type = {'blue': 0, 'green': 0, 'black': 0, 'red': 0, 'white': 0}
        self.res_cards = []
        self.nobles = []

    def get_name(self):
        return self.name

    def get_gems(self):
        return self.gems

    def get_points(self):
        return self.points

    def get_pur_cards_type(self):
        return self.pur_cards_type

    def get_res_cards(self):
        return self.res_cards

    def get_nobles(self):
        return self.nobles

    def add_gem(self, new_gems):
        # add gems to player's hand and check if player have more than 10 gems
        def switch(x):
            # choose which gem to discard
            def dec_gem(gem_type):
                if self.gems[gem_type] > 0:
                    self.gems[gem_type] -= 1
                    print(f'Current gems = {self.gems}')
                    return 'discarded a gem'
                else:
                    print('not enough gems, choose again.')

            switcher = {
                1: lambda: dec_gem('blue'),
                2: lambda: dec_gem('green'),
                3: lambda: dec_gem('black'),
                4: lambda: dec_gem('red'),
                5: lambda: dec_gem('white')
            }
            return switcher.get(x, "invalid input")()
        
        # add new gems to players hand
        for gem_type, amount in new_gems.items():
            self.gems[gem_type] += amount

        # discard gems until gems in hand is equal to gem limit
        while sum(self.gems.values()) > self.gem_limit:
            print(f"total gems: {sum(self.gems.values())}")
            print("Which gem would you like to discard?")
            print(f"1 - blue({self.gems['blue']})")
            print(f"2 - green({self.gems['green']})")
            print(f"3 - black({self.gems['black']})")
            print(f"4 - red({self.gems['red']})")
            print(f"5 - white({self.gems['white']})")
            switch(int(input()))

    def buy_card(self, card) :
        #TODO Check if player can afford the card
        for gem_type, amount in card.cost.items():
            amount -= self.pur_cards_type[gem_type]
            self.gems[gem_type] -= amount
        self.pur_cards_type[card.get_gem_type()] += 1
        self.points += card.get_points()
        
    def res_card(self, card):
        self.res_cards.append(card)
    
    def acquire_noble(self, noble):
        self.nobles.append(noble)
        self.points += noble.get_points()