import random

suits = ("Hearts", "Diamonds", "Clubs", "Spades")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}


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
        self.money = 1000
        self.hand = []
        self.hand_value = 0

    def __str__(self):
        return "Player " + str(self.name) + ": $" + str(self.money)

    def add_card(self, new_card):
        self.hand.append(new_card)
        # Re-evaluate hand value
        value = 0
        # Add card values
        for card in self.hand:
            value += card.value

        # Check when over 21 if an Ace is in the hand
        for card in self.hand:
            if value > 21 and card.rank == 'Ace':
                value -= 10

        self.hand_value = value

    def clear_hand(self):
        self.hand = []
        self.hand_value = 0

    def bet(self, amount):
        if amount <= self.money:
            self.money -= amount
            return True
        else:
            return False

    def award(self, amount):
        self.money += amount


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
