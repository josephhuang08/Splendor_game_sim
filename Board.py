

class Board:
    def __init__(self, nobles, cards, gems):
        self.nobles = nobles
        self.cards = cards
        self.gems = gems

    def display(self):
        print("Nobles:")
        for noble in self.nobles:
            print(noble)
        print()
        print("Field cards:")
        for card in self.field_cards:
            print(card)
        print()
        print(f"Cards left in deck: {len(self.deck_cards)}")
        print(f"Gems left on field: {self.gems}")

    def draw_card(self):
        if self.deck_cards:
            return self.deck_cards.pop()
        return None