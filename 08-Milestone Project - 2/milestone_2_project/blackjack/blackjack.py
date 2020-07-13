from cards import Deck, Player

# Game Play¶
# To play a hand of Blackjack the following steps must be followed:
#
# Create a deck of 52 cards
# Shuffle the deck
# Ask the Player for their bet
# Make sure that the Player's bet does not exceed their available chips
# Deal two cards to the Dealer and two cards to the Player
# Show only one of the Dealer's cards, the other remains hidden
# Show both of the Player's cards
# Ask the Player if they wish to Hit, and take another card
# If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
# If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
# Determine the winner and adjust the Player's chips accordingly
# Ask the Player if they'd like to play again


def play_game():
    player_name = input("What is your name? ")
    print(f'Welcome {player_name}!\n')
    player = Player(player_name)

    game_on = True
    while game_on:
        player.clear_hand()
        print(player)

        # Create a deck of 52 cards, Shuffle the deck
        deck = Deck()
        deck .shuffle()

        dealer = Player("Dealer")

        # Ask the Player for their bet
        # Make sure that the Player's bet does not exceed their available chips
        bet_amount = ask_bet(player)

        # Deal two cards to the Dealer and two cards to the Player
        dealer.add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())
        player.add_card(deck.deal_one())
        player.add_card(deck.deal_one())

        hitting = True
        player_bust = False
        print('Player Hitting')
        while hitting and not player_bust:
            # Show only one of the Dealer's cards, the other remains hidden
            # Show both of the Player's cards
            show_table(dealer, player, hide=True)

            # Ask the Player if they wish to Hit, and take another card
            hit = ask_hit(player)
            if hit:
                player.add_card(deck.deal_one())
                # If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
                if player.hand_value > 21:
                    print('PLAYER BUST!!!')
                    player_bust = True
            else:
                hitting = False

        if not player_bust:
            # If a Player Stands, play the Dealer's hand.
            # The dealer will always Hit until the Dealer's value meets or exceeds 17
            print('Dealer Hitting')
            while dealer.hand_value < 17:
                show_table(dealer, player, hide=True)

                dealer.add_card(deck.deal_one())
                if dealer.hand_value > 21:
                    print('DEALER BUST!!!')

        show_table(dealer, player, hide=False)

        # Determine the winner and adjust the Player's chips accordingly
        player_wins = determine_winner(dealer, player)
        if player_wins:
            player.award(bet_amount*2)
            print(f'{player.name} WINS')
        else:
            print(f'Dealer WINS')
        print(f'{player.name}: {player.hand_value}, Dealer: {dealer.hand_value}')

        # Ask the Player if they'd like to play agaim

        play_again = ask_play_again()
        if not play_again or player.money <= 0:
            game_on = False
        else:
            pass


def determine_winner(dealer, player):
    if player.hand_value > 21:
        return False
    elif dealer.hand_value > 21:
        return True
    elif player.hand_value < dealer.hand_value:
        return False
    else:
        return True


def ask_play_again():
    valid_response = False
    while not valid_response:
        answer = input('\nPlay Again (Y/N)? ')
        if answer.lower() == 'y':
            valid_response = True
            return True
        elif answer.lower() == 'n':
            valid_response = True
            return False
        else:
            print('Please answer with Y or N \n')


def ask_hit(player):
    print(f'Your hand has a value of {player.hand_value}')
    valid_response = False
    while not valid_response:
        answer = input('Would you like to hit (Y/N)? ')
        if answer.lower() == 'y':
            valid_response = True
            return True
        elif answer.lower() == 'n':
            valid_response = True
            return False
        else:
            print('Please answer with Y or N \n')


def show_table(dealer, player, hide=True):
    if hide:
        show_cards(dealer, hide=True)
    else:
        show_cards(dealer, hide=False)
    show_cards(player, hide=False)


def show_cards(player, hide=True):
    print(f'{player.name} Cards:')
    if len(player.hand) == 0:
        print('None')
    else:
        for ind, card in enumerate(player.hand):
            if ind == 0 and hide:
                print('HIDDEN')
            else:
                print(card)
    print("")


def ask_bet(player):

    valid_bet = False
    while not valid_bet:
        bet_amount = input(f'{player.name}, how much would you like to bet? ')
        try:
            bet_amount = int(bet_amount)
            transaction_success = player.bet(bet_amount)
            if transaction_success:
                valid_bet = True
            else:
                print(f'Insufficient funds, you have ${player.money} available.\n')

        except Exception as e:
            print('Invalid bet entered, please enter valid number.\n')

    return bet_amount


if __name__ == "__main__":
    play_game()