class Player:
    def __init__(self, name):
        self.name = name
        self.gems = {'red': 0, 'green': 0, 'blue': 0, 'black': 0, 'white': 0, 'gold': 0}
        self.gem_limit = 10
        self.points = 0
        self.pur_cards_type = {'red': 0, 'green': 0, 'blue': 0, 'black': 0, 'white': 0}
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
                1: lambda: dec_gem('red'),
                2: lambda: dec_gem('green'),
                3: lambda: dec_gem('blue'),
                4: lambda: dec_gem('black'),
                5: lambda: dec_gem('white'),
                6: lambda: dec_gem('gold')
            }
            return switcher.get(x, "invalid input")()
        
        # add new gems to players hand
        for gem_type, amount in new_gems.items():
            self.gems[gem_type] += amount

        # discard gems until gems in hand is equal to gem limit
        while sum(self.gems.values()) > self.gem_limit:
            print(f"total gems: {sum(self.gems.values())}")
            print("Which gem would you like to discard?")
            print(f"1 - red({self.gems['red']})")
            print(f"2 - green({self.gems['green']})")
            print(f"3 - blue({self.gems['blue']})")
            print(f"4 - black({self.gems['black']})")
            print(f"5 - white({self.gems['white']})")
            print(f"6 - gold({self.gems['gold']})")
            switch(int(input()))
    
    def can_afford(self, card):
        # get a copy of the dict and check if player can afford the card. 
        temp_gems = self.gems.copy()

        for gem_type, amount in card.get_cost().items():
            amount -= self.pur_cards_type[gem_type]
            temp_gems[gem_type] -= amount
            if temp_gems[gem_type] < 0:
                # when has not enough gems use gold as substitute 
                temp_gems['gold'] += temp_gems[gem_type]
            if temp_gems['gold'] < 0:
                # if need more gold gems than what player has then player cannot afford the card
                return False
        return True

    def buy_card(self, card):
        for gem_type, amount in card.cost.items():
            amount -= self.pur_cards_type[gem_type]
            self.gems[gem_type] -= amount
            if self.gems[gem_type] < 0:
                self.gems['gold'] += self.gems[gem_type]
                self.gems[gem_type] = 0
    
        self.pur_cards_type[card.get_gem_type()] += 1
        self.points += card.get_points()
        
    def res_card(self, card, get_gold):
        if get_gold:
            self.gems['gold'] += 1
        self.res_cards.append(card)
    
    def acquire_noble(self, noble):
        self.nobles.append(noble)
        self.points += noble.get_points()
    
    def display_info(self):
        # print the player's name and points
        print(f"player: {self.name}, points: {self.points}")
        # print the player's remaining gems
        print("gems: ", end='')
        for key, value in self.gems.items():
            print(f"{key}: {value}", end=' ')
        print()
        # print the player's purchased card type and number
        print("purchased: ", end='')
        for key, value in self.pur_cards_type.items():
            print(f"{key}: {value}", end=' ')
        print()
        # print player's reserved cards
        print(f"reserved cards({len(self.res_cards)}): ")
        for card in self.res_cards:
            print(f"level: {card.get_level()}, type: {card.get_gem_type()}, points: {card.get_points()}")
            print(f"cost: {card.get_cost()}")
            print('-----')
        print()