import random
import time

from war.cards import Deck, Player


def deal_cards(player_1, player_2, deck):
    while len(deck.all_cards) > 0:
        card_dealt = deck.deal_one()
        if len(deck.all_cards) % 2 == 0:
            player_1.add_cards(card_dealt)
        else:
            player_2.add_cards(card_dealt)


def draw_cards(player_1, player_2, table_cards):
    player_1_card = player_1.remove_one()
    player_2_card = player_2.remove_one()
    display_cards(player_1_card, player_2_card)

    table_cards.append(player_1_card)
    table_cards.append(player_2_card)
    random.shuffle(table_cards)

    player_1_last_card = len(player_1.all_cards) == 0
    player_2_last_card = len(player_2.all_cards) == 0

    return player_1_card, player_2_card, player_1_last_card, player_2_last_card


def display_cards(card_1, card_2):
    print(f'{card_1} ({card_1.value}) --- {card_2} ({card_2.value})')


def play_war(player_1, player_2):
    deck = Deck()
    deck.shuffle()

    deal_cards(player_1, player_2, deck)

    game_on = True
    winning_player = None

    turns = 0

    while game_on:
        turns += 1
        print(player_1)
        print(player_2)

        table_cards = []

        # Make sure no cards were lost
        if len(player_1.all_cards) + len(player_2.all_cards) != 52:
            raise Exception

        player_1_card, player_2_card, player_1_last_card, player_2_last_card = draw_cards(player_1, player_2, table_cards)

        if player_1_card.value > player_2_card.value or player_2_last_card:
            player_1.add_cards(table_cards)
            print(f'{player_1.name} wins this round!\n')
        elif player_2_card.value > player_1_card.value or player_1_last_card:
            player_2.add_cards(table_cards)
            print(f'{player_2.name} wins this round!\n')
        else:
            print('WAR!!!\n')
            at_war = True

            while at_war:
                for i in range(3):
                    if len(player_1.all_cards) == 1 or len(player_2.all_cards) == 1:
                        break
                    draw_cards(player_1, player_2, table_cards)

                print("")
                player_1_card, player_2_card, player_1_last_card, player_2_last_card = draw_cards(player_1, player_2, table_cards)
                print("")

                if player_1_card.value > player_2_card.value or player_2_last_card:
                    player_1.add_cards(table_cards)
                    print(f'{player_1.name} wins this round!\n')
                    at_war = False
                elif player_2_card.value > player_1_card.value or player_1_last_card:
                    player_2.add_cards(table_cards)
                    print(f'{player_2.name} wins this round!\n')
                    at_war = False
                else:
                    print("ANOTHER WAR!!!")

        if len(player_1.all_cards) == 0:
            print(f'{player_2.name} wins the Game!\n')
            game_on = False
            winning_player = player_2
        elif len(player_2.all_cards) == 0:
            print(f'{player_1.name} wins the Game!\n')
            game_on = False
            winning_player = player_1

        # elif turns > 1000:
        #     game_on = False

    print("Game Over")

    return winning_player


if __name__ == "__main__":
    # player_1_name = input("Player 1, what is your name? ")
    # print(f'Welcome {player_1_name}!\n')
    #
    # player_2_name = input("Player 2, what is your name? ")
    # print(f'Welcome {player_2_name}!\n')
    #
    # player_1 = Player(player_1_name)
    # player_2 = Player(player_2_name)

    player_1 = Player("Tanner")
    player_2 = Player("Kortnie")

    player_1_wins = 0
    player_2_wins = 0
    draws = 0

    time_start = time.time()
    num_of_games = 1000

    for i in range(num_of_games):
        winner = play_war(player_1, player_2)
        if winner == player_1:
            player_1_wins += 1
        elif winner == player_2:
            player_2_wins += 1
        elif winner is None:
            draws += 1
        player_1.clear_cards()
        player_2.clear_cards()

    total_time = time.time() - time_start

    print(f'{player_1.name} won {player_1_wins} times')
    print(f'{player_2.name} won {player_2_wins} times')
    print(f'There were {draws} draws')
    print()
    print(f'Played {num_of_games} in {total_time} seconds')
