import unittest

from Board import Board
from Player import Player
from Card import Card, CardList
from Noble import Noble, NobleList
from Game import Game

class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Create a test player object and add gems
        self.player = Player("John")
        #self.player.add_gem({'blue': 1, 'green': 1, 'black': 0, 'red': 3, 'white': 1, 'gold': 1})
        # create 5 cards
        self.cards = [
            Card(level=1, gem_type='black', cost={'blue': 1, 'green': 1}, points=0),
            Card(level=1, gem_type='blue', cost={'red': 3, 'green': 1}, points=1),
            Card(level=2, gem_type='white', cost={'blue': 2, 'green': 1, 'black': 2}, points=2),
            Card(level=3, gem_type='black', cost={'white': 3, 'green': 1, 'red': 2}, points=2),
            Card(level=3, gem_type='red', cost={'blue': 1, 'green': 1, 'white': 2, 'red': 3, 'black': 2}, points=2),
            ]
        self.player.res_card(self.cards[2], True)
        self.noble = [
            Noble({'blue': 1}, 3)
        ]
        
    def test_add_gem(self):
        # Test adding gems to the player's gem count
        self.player.add_gem({'blue': 1, 'green': 1, 'black': 1, 'red': 0, 'white': 0, 'gold': 0})
        self.assertEqual(self.player.get_gems(), {'blue': 1, 'green': 1, 'black': 1, 'red': 0, 'white': 0, 'gold': 1})
        # test when player has more than 10 gems
        self.player.add_gem({'blue': 2, 'white': 1, 'black': 4})
        self.assertEqual(sum(self.player.get_gems().values()), 10)

    def test_can_afford(self):
        # Test if player can afford the card
        self.player.add_gem({'red': 3, 'gold': 1})
        self.assertFalse(self.player.can_afford(self.cards[3]))
        self.assertTrue(self.player.can_afford(self.cards[1]))

    def test_pur_card(self):
        self.player.add_gem({'green': 1, 'blue': 1, 'red': 3, 'white': 1})
        # Test a successful purchase when the player has enough gems
        self.player.buy_card(self.cards[0]) # buys first card (type: black)
        self.assertEqual(self.player.get_gems(), {'blue': 0, 'green': 0, 'black': 0, 'red': 3, 'white': 1, 'gold': 1})
        # Test when player must use gold token to buy a card
        self.player.buy_card(self.cards[1]) # buys second card (type: blue)
        self.assertEqual(self.player.get_gems(), {'blue': 0, 'green': 0, 'black': 0, 'red': 0, 'white': 1, 'gold': 0}) 
        self.assertEqual(self.player.get_pur_cards_type(), {'blue': 1, 'green': 0, 'black': 1, 'red': 0, 'white': 0})
        self.assertEqual(self.player.get_points(), 1)
        
    def test_res_card(self):
        # Test reserving a card and adding it to the player's reserved card list
        self.player.res_card(self.cards[0], True)
        self.assertIn(self.cards[0], self.player.get_res_cards())

    def test_acquire_noble(self):
        # Test player aquiring a noble
        self.player.acquire_noble(self.noble[0])
        self.assertEqual(self.player.get_points(), 3)
    
    def test_display_info(self):
        self.player.display_info()

class TestCard(unittest.TestCase):
    def setUp(self):
        # Set up a list of cards to use for testing
        self.card_list = CardList()

    def test_init(self):
        # test if the total amount of cards are correct
        self.assertEqual(len(self.card_list.level1), 40)
        self.assertEqual(len(self.card_list.level2), 30)
        self.assertEqual(len(self.card_list.level3), 20)

    def test_new_card(self):
        # Test new_card. assertFalse becase new_card will be removed from the deck thus not in the card_list
        self.assertFalse(self.card_list.new_card(1) in self.card_list.level1)
        self.assertFalse(self.card_list.new_card(2) in self.card_list.level2)
        self.assertFalse(self.card_list.new_card(3) in self.card_list.level3)

        # Test new_card with invalid level
        self.assertIsNone(self.card_list.new_card(4))

        # Test new_card with valid level but empty list
        self.card_list.level1 = []
        self.assertIsNone(self.card_list.new_card(1))

class TestNobleList(unittest.TestCase):
    def setUp(self):
        # Create a test Noble object and a NobleList object
        self.noble_list = NobleList()

    def test_new_nobles(self):
        # Test new_nobles with valid input. Check if each noble is different
        nobles = self.noble_list.new_nobles(5)
        self.assertEqual(len(nobles), 5)
        self.assertTrue(all(isinstance(noble, Noble) for noble in nobles))
        for i in range(len(nobles)):
            for j in range(i + 1, len(nobles)):
                self.assertNotEqual(nobles[i], nobles[j])

def test_player():
    test = unittest.TestLoader().loadTestsFromTestCase(TestPlayer)
    unittest.TextTestRunner().run(test)

def test_card():
    test = unittest.TestLoader().loadTestsFromTestCase(TestCard)
    unittest.TextTestRunner().run(test)

def test_noble():
    test = unittest.TestLoader().loadTestsFromTestCase(TestNobleList)
    unittest.TextTestRunner().run(test)

def test_all():
    unittest.main()

if __name__ == '__main__':
    #test_player()
    #test_card()
    #test_noble()
    test_all()