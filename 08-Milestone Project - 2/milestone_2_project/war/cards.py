import random

suits = ("Hearts", "Diamonds", "Clubs", "Spades")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                new_card = Card(suit, rank)
                self.all_cards.append(new_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def __str__(self):
        if len(self.all_cards) == 1:
            return "Player " + str(self.name) + " has " + str(len(self.all_cards)) + " card."
        else:
            return "Player " + str(self.name) + " has " + str(len(self.all_cards)) + " cards."

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def clear_cards(self):
        self.all_cards = []


if __name__ == "__main__":
    my_deck = Deck()
    print("First Card:")
    print(my_deck.all_cards[0])
    print("Last Card:")
    print(my_deck.all_cards[-1])
    print("")

    my_deck.shuffle()
    print("New First Card:")
    print(my_deck.all_cards[0])
    print("New Last Card:")
    print(my_deck.all_cards[-1])
    print("")

    my_card = my_deck.deal_one()
    print("Dealt Card:")
    print(my_card)
    print("")

    new_player = Player("Tanner")
    print("New Player:")
    print(new_player)
    print("")

    new_player.add_cards(my_card)
    print("Added one card:")
    print(new_player)
    print(new_player.all_cards)
    print("")

    new_player.remove_one()
    print("Removed one card:")
    print(new_player)
    print(new_player.all_cards)
    print("")

    new_player.add_cards([my_card, my_card, my_card])
    print("Added three cards:")
    print(new_player)
    print(new_player.all_cards)
    print("")
