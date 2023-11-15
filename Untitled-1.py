import copy
import random

def initialize_deck():
    ranks = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    deck = copy.deepcopy(ranks)
    random.shuffle(deck)
    return deck

def play_goofspiel(num_rounds):
    deck = initialize_deck()
    deck1 = initialize_deck()
    deck2 = initialize_deck()
    random.shuffle(deck1)
    random.shuffle(deck2)
    player1_score = 0
    player2_score = 0

    for round_num in range(1, num_rounds + 1):
        prize_card = deck.pop()

        #print(f"\nRound {round_num}: Prize card is {prize_card}")

        player1_card = prize_card
        player2_card = deck2.pop()

        #print(f"Player 1 plays {player1_card}")
        #print(f"Player 2 plays {player2_card}")

        if player1_card > player2_card:
            #print("Player 1 wins the round!")
            player1_score += prize_card
        elif player1_card < player2_card:
            #print("Player 2 wins the round!")
            player2_score += prize_card
        else:
            #print("It's a tie! No one wins the round.")
            player1_score += ( prize_card/2 )
            player2_score += ( prize_card/2 )
    print("\nGame Over")
    print(f"Player 1's score: {player1_score}")
    print(f"Player 2's score: {player2_score}")
    if player1_score > player2_score:
        print("Player 1 wins!")
    elif player2_score > player1_score:
        print("Player 2 wins!")
    else:
        print("Draw")

    return player1_score > player2_score

if __name__ == "__main__":
    num_games = 20
    num_rounds = 13
    player1_wins = 0
    player2_wins = 0

    for game_num in range(1, num_games + 1):
        print(f"\n===== Game {game_num} =====")
        if play_goofspiel(num_rounds):
            print("Player 1 wins the game!")
            player1_wins += 1
        else:
            print("Player 2 wins the game!")
            player2_wins += 1

    print("\nTotal Wins Across Games:")
    print(f"Player 1: {player1_wins}")
    print(f"Player 2: {player2_wins}")
