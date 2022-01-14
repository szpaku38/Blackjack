import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Returns random card from the deck."""
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a draw!"
    elif c_score == 0:
        return "Computer has a blackjack! You lose."
    elif u_score == 0:
        return "You have a blackjack! You won."
    elif u_score > 21:
        return "You went over! You lose."
    elif c_score > 21:
        return "Computer went over. You won!"
    elif u_score > c_score:
        return "You have a higher score. You won!"
    else:
        return "You lose. Computer has a higher score."


def play_game():
    print(logo)
    computer_cards = []
    user_cards = []
    is_game_over = False

    for _ in range(2):
        computer_cards.append(deal_card())
        user_cards.append(deal_card())

    while not is_game_over:
        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)

        print("Your cards: " + str(user_cards) +
              ", current score: " + str(user_score))
        print("Computer's first card: " + str(computer_cards[0]))

        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_card = input("Do You want to draw another card? y/n: ")
            if draw_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? y/n: ") == "y":
    play_game()
