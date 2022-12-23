class Player:
    def __init__(self, name):
        self.name = name
        self.gems = {'blue': 0, 'green': 0, 'black': 0, 'red': 0, 'white': 0, 'gold': 0}
        self.gem_limit = 10
        self.points = 0
        self.pur_cards_type = {'blue': 0, 'green': 0, 'black': 0, 'red': 0, 'white': 0}
        self.pur_cards_count = 0
        self.res_cards = []
        self.res_card_count = 0
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

    def get_res_card_count(self):
        return self.res_card_count

    def get_nobles(self):
        return self.nobles

    def add_gem(self, new_gems):
        def switch(x):
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

        total_gems = sum(self.gems.values()) + sum(new_gems.values())
        while total_gems > self.gem_limit:
            print("Which gem would you like to discard?")
            print(f"1 - blue({self.gems['blue']})")
            print(f"2 - green({self.gems['green']})")
            print(f"3 - black({self.gems['black']})")
            print(f"4 - red({self.gems['red']})")
            print(f"5 - white({self.gems['white']})")
            result = switch(int(input()))
            total_gems -= 1 if result == 'discarded a gem' else 0

        for gem_type, amount in new_gems.items():
            self.gems[gem_type] += amount

    def buy_card(self, card) :
        #TODO Check if player can afford the card
        for gem_type, amount in card.cost.items():
            amount -= self.pur_cards_type[gem_type]
            self.gems[gem_type] -= amount
        self.pur_cards_type[card.get_gem_type()] += 1
        self.pur_cards_count += 1
        self.points += card.get_points()
        
    def res_card(self, card):
        self.res_cards.append(card)
        self.res_card_count += 1
    
    def acquire_noble(self, noble):
        self.nobles.append(noble)
        self.points += noble.get_points()