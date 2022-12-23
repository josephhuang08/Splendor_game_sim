class Game:
    def __init__(self, players, board):
        self.players = players
        self.board = board
        self.turn = 0

    def get_current_player(self):
        return self.players[self.turn]

    def next_turn(self):
        self.turn = (self.turn + 1) % len(self.players)

    def play(self):
        while not self.game_over():
            player = self.get_current_player()
            self.board.display()
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

    def game_over(self):
        return any(player.points >= 15 for player in self.players)

    def buy_card(self, player):
        # Allow the player to choose and buy a card from the board
        pass

    def res_card(self, player):
        # Allow the player to choose and reserve a card from the board
        pass

    def pur_res_card(self, player):
        # Allow the player to choose and purchase a reserved card
        pass

from Player import Player
from Card import Card
    