from Noble import NobleList
from Card import CardList
from Player import Player

class Game:
    def __init__(self, num_player):
        # amount of players in game
        self.num_players = num_player
        # create players
        self.players = []
        for i in range (num_player):
            name = input(f"Player {i + 1}. Enter your name: ")
            self.players.append(Player(name))
        # init the correct amount of nobles on to the board
        self.nobles_list = NobleList()
        self.nobles = self.nobles_list.new_nobles(num_player + 1)
        # init the deck of cards
        self.card_list = CardList()
        # set the correct amount of gems
        if num_player == 4:
            gem_count = 7
        else:
            gem_count = num_player + 2
        self.avail_gems = {'red': gem_count, 'green': gem_count, 'blue': gem_count, 'black': gem_count, 'white': gem_count, 'gold': 5}
        # init the current cards on the field
        self.field_cards = [
            [self.card_list.new_card(1) for _ in range(4)],
            [self.card_list.new_card(2) for _ in range(4)],
            [self.card_list.new_card(3) for _ in range(4)]
            ]
        # counts the number of rounds the game has progressed
        self.rounds = 0

    def get_players(self):
        return self.players
    
    def get_rounds(self):
        return self.rounds

    def display_field_cards(self):
        def print_cost(cost):
            out_str = ""
            for gem_type, amount in cost.items():
                if amount > 0: 
                    out_str += ' ' + gem_type + '(' + str(amount) + ')'
            return out_str

        for i in range(3):
            print(f"Level {i + 1} cards")
            print("-" * 15)
            for card in self.field_cards[i]:
                print(f"| Gem: {card.get_gem_type()}\t Points: {card.get_points()}\t Cost: [{print_cost(card.get_cost())} ]")
            print()

    def game_over(self):
        if any(player.points >= 15 for player in self.players):
            print("Game over")
            print("---------------")
            for player in self.players:
                print(f"Player: {player.get_name()} has {player.get_points()}.")
            print("---------------")
            print(f"Total rounds played: {self.rounds}")
            return True
        else:
            return False

    # TODO: when player quit's choosing gems or when player cannot afford a card. The player's turn is skipped. X Get bool return. if false do the loop again
    # TODO: The order of avail_gems is messed up and gold gem is missing
    # TODO: when buy_card & res_card, allow player to quit
    # TODO: when a avail_gem is less than 4, the player cannot take 2 gems
    def play(self):
        while not self.game_over():
            self.rounds += 1
            print('Round: ', self.rounds)
            for player in self.players:
                self.display_field_cards()
                print(f"{player.get_name()}'s turn")
                print("Choose an action:")
                print("1. Collect gems")
                print("2. Buy a card")
                print("3. Reserve a card")
                print("4. Purchase reserved card")
                action = int(input())
                if action == 1:
                    self.collect_gems(player)
                elif action == 2:
                    self.buy_card(player)
                elif action == 3:
                    self.res_card(player)
                elif action == 4:
                    self.pur_res_card(player)
                player.display_info()
            
    def select_card_from_board(self):
        while True:
            # The player must enter a valid input to exit the loop
            try:
                # input example: 1 2. This level 1, 2nd card on the board
               level, pos = map(int, input("Enter level and position: ").split())
               break
            except (ValueError, IndexError):
                print("Invalid input, please try again.")

        return self.field_cards[level - 1][pos - 1]

    def collect_gems(self, player):
        collected_gems = {'red': 0, 'green': 0, 'blue': 0, 'black': 0, 'white': 0}
        print(f'Avaiable gems: {self.avail_gems}')
        print('Select the gems you wish to collect')
        # input example: 1 2 3. Get Red, Green and blue gem
        print('| 1: Red | 2: Green | 3: Blue | 4: Black | 5: White | 0: Quit')
        while True:
            user_input = input().split()
            # check if user input is: 1. no more than three gems 3. three gems but 2 the same.
            if len(user_input) > 3 or (len(user_input) == 3 and len(user_input) != len(set(user_input))):
                print("Invalid input, please try again.")
                continue

            for gem in user_input:
                if gem == '0':
                    return
                if int(gem) > 5:
                    print("Invalid input, please try again.")
                    continue
                elif gem == '1':
                    collected_gems['red'] += 1
                elif gem == '2':
                    collected_gems['green'] += 1
                elif gem == '3':
                    collected_gems['blue'] += 1
                elif gem == '4':
                    collected_gems['black'] += 1
                elif gem == '5':
                    collected_gems['white'] += 1
                else:
                    print("Invalid input, please try again.")
            break

        # update the avail_gem and player's gems
        # https://www.geeksforgeeks.org/python-subtraction-of-dictionaries/
        self.avail_gems = {key: self.avail_gems[key] - collected_gems[key] for key in set(self.avail_gems) & set(collected_gems)}
        player.add_gem(collected_gems)
        
    def buy_card(self, player):
        # Allow the player to choose and buy a card from the board
        print('Select the card you wish to purchase')
        card = self.select_card_from_board()
        # get card from the board and check if player can arrord or not
        if player.can_afford(card):
            gems_returned = player.buy_card(card)
            for gem_type, amount in gems_returned.items():
                self.avail_gems[gem_type] += amount
            #TODO: give the board a new card
        else:
            print('You do not have enough gems to purchase this card')

    def res_card(self, player):
        # Allow the player to choose and reserve a card from the board
        print('Select the card you wish to reserve')
        card = self.select_card_from_board()
        if self.avail_gems['gold'] > 0:
            player.res_card(card, True)
            self.avail_gems['gold'] -= 1
        else:
            player.res_card(card, False)

    def pur_res_card(self, player):
        # Allow the player to choose and purchase a reserved card
        pass
    