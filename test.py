import unittest

from Board import Board
from Player import Player
from Card import Card
from Noble import Noble
from Game import Game

class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Create a test player object and add gems
        self.player = Player("John")
        self.player.add_gem({'blue': 1, 'green': 1, 'black': 0, 'red': 3, 'white': 1, 'gold': 1})
        # create 5 cards
        self.cards = [
            Card(level=1, gem_type='green', cost={'blue': 1, 'green': 1}, points=0),
            Card(level=1, gem_type='blue', cost={'red': 3, 'green': 1}, points=1),
            Card(level=2, gem_type='white', cost={'blue': 2, 'green': 1, 'black': 2}, points=2),
            Card(level=3, gem_type='black', cost={'white': 3, 'green': 1, 'red': 2}, points=2),
            Card(level=3, gem_type='red', cost={'blue': 1, 'green': 1, 'white': 2, 'red': 3, 'black': 2}, points=2),
            ]
        self.noble = [
            Noble({'blue': 1}, 3)
        ]

    def test_add_gem(self):
        # Test adding gems to the player's gem count
        self.player.add_gem({'blue': 1, 'green': 1, 'black': 1, 'red': 0, 'white': 0, 'gold': 0})
        self.assertEqual(self.player.get_gems(), {'blue': 2, 'green': 2, 'black': 1, 'red': 3, 'white': 1, 'gold': 1})
        # test when player has more than 10 gems
        self.player.add_gem({'blue': 2, 'white': 1})
        self.assertEqual(sum(self.player.get_gems().values()), 10)

    def test_pur_card(self):
        # Test purchasing a card and subtracting the cost from the player's gem count
        self.player.buy_card(self.cards[0]) # buys first card
        self.assertEqual(self.player.get_gems(), {'blue': 0, 'green': 0, 'black': 0, 'red': 3, 'white': 1, 'gold': 1})
        self.player.buy_card(self.cards[1]) # buys second card
        self.assertEqual(self.player.get_gems(), {'blue': 0, 'green': 0, 'black': 0, 'red': 0, 'white': 1, 'gold': 1})
        self.assertEqual(self.player.get_pur_cards_type(), {'blue': 1, 'green': 1, 'black': 0, 'red': 0, 'white': 0})
        self.assertEqual(self.player.get_points(), 1)

    def test_res_card(self):
        # Test reserving a card and adding it to the player's reserved card list
        self.player.res_card(self.cards[0])
        self.assertEqual(self.player.get_res_cards(), [self.cards[0]])
        self.assertEqual(self.player.get_res_card_count(), 1)

    def test_acquire_noble(self):
        # Test player aquiring a noble
        self.player.acquire_noble(self.noble[0])
        self.assertEqual(self.player.get_points(), 3)

if __name__ == '__main__':
    unittest.main()