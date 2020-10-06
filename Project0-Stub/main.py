def get_random_numbers():
    return 0, 0, 0, 0


def user_pick_numbers():
    return 0, 0, 0, 0


def get_total_winnings(winning_ticket, user_ticket):
    return check_for_straight_win(winning_ticket, user_ticket) \
           + check_for_one_off_win(winning_ticket, user_ticket)


def check_for_straight_win(winning_ticket, user_ticket):
    return 0


def check_for_one_off_win(winning_ticket, user_ticket):
    return 0


def ask_to_play_again():
    return input("Do you want to play again? Y/N").upper()


def ask_player_for_easy_pick_or_manual():
    return 'easy'


total_spent = 0
total_won = 0
play_again = 'Y'

while play_again == 'Y':
    total_spent += 1

    winning_ticket = get_random_numbers()

    if ask_player_for_easy_pick_or_manual() == "easy":
        user_ticket = user_pick_numbers()
    else:
        user_ticket = get_random_numbers()

    total_won += get_total_winnings(winning_ticket, user_ticket)

    print('total spent, total won, net loss')

    play_again = ask_to_play_again()
