from Noble import NobleList
from Card import CardList

class Game:
    def __init__(self, players):
        # amount of players in game
        self.players = players
        # get the correct amount of nobles on to the board
        self.nobles_list = NobleList()
        self.nobles = self.nobles_list.new_nobles()
        # get the deck of cards
        self.card_list = CardList()
        # get the correct amount of gems
        if len(players) == 4:
            gem_count = 7
        else:
            gem_count = len(players) + 2
        self.avail_gems = {'red': gem_count, 'green': gem_count, 'blue': gem_count, 'black': gem_count, 'white': gem_count, 'gold': 5}
        # current cards on the field. Get level 2, 3rd card  = self.field_cards[1][2]
        self.field_cards = [
            [self.card_list.new_card(1) for _ in range(4)],
            [self.card_list.new_card(2) for _ in range(4)],
            [self.card_list.new_card(3) for _ in range(4)]
            ]
        # counts the number of rounds the game has progressed
        self.rounds = 1

    def get_players(self):
        return self.players
    
    def get_rounds(self):
        return self.rounds
    
    def display_players_info(self):
        pass

    def display_field_cards(self):
        for i in range(3):
            for card in self.field_cards[i]:
                pass
                
    def game_over(self):
        return any(player.points >= 15 for player in self.players)

    def play(self):
        while not self.game_over():
            for i , player in enumerate(self.players):
                print(f"{player.name}'s turn")
                print("Choose an action:")
                print("1. Buy a card")
                print("2. Reserve a card")
                print("3. Purchase reserved card")
                action = int(input())
                if action == 1:
                    self.buy_card(player)
                elif action == 2:
                    self.res_card(player)
                elif action == 3:
                    self.pur_res_card(player)
                self.next_turn()

    def buy_card(self, player):
        # Allow the player to choose and buy a card from the board
        print('Which card do you want to buy?')
        while True:
            try:
                level, position = map(int, input("Enter level and position: ").split())
                card = self.field_cards[level - 1][position - 1]
                break  # exit the loop if the input is valid
            except (ValueError, IndexError):
                print("Invalid input, please try again.")

    def res_card(self, player):
        # Allow the player to choose and reserve a card from the board
        pass

    def pur_res_card(self, player):
        # Allow the player to choose and purchase a reserved card
        pass
    