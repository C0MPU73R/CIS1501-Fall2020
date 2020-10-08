import random


def get_random_numbers():
    return random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)


def get_single_number():
    number = int(input("Enter a number 0-9: "))

    # while number is invalid on either side
    # while 0 < number or number > 9:

    # while not ( valid )
    while not (0 <= number <= 9):
        number = int(input("Try again - Enter a number 0-9: "))
    return number


def user_pick_numbers():
    return get_single_number(), get_single_number(), get_single_number(), get_single_number()


def get_total_winnings(winning_ticket, user_ticket):
    return check_for_straight_win(winning_ticket, user_ticket) \
           + check_for_one_off_win(winning_ticket, user_ticket)


def check_for_straight_win(winning_ticket, user_ticket):
    if winning_ticket == user_ticket:
        return 1000
    # else: - redundant
    return 0


def check_for_one_off_win(winning_ticket, user_ticket):
    if (winning_ticket[0] == user_ticket[0] and
        winning_ticket[1] == user_ticket[1] and
        winning_ticket[2] == user_ticket[2] and
        (winning_ticket[3] == user_ticket[3] - 1 or
        winning_ticket[3] == user_ticket[3] + 1)) or \
        ((winning_ticket[0] == user_ticket[0] - 1 or
         winning_ticket[0] == user_ticket[0] + 1) and
         winning_ticket[1] == user_ticket[1] and
         winning_ticket[2] == user_ticket[2] and
         winning_ticket[3] == user_ticket[3]):
        return 275
    return 0


def ask_to_play_again():
    return input("Do you want to play again? Y/N").upper()


def ask_player_for_easy_pick_or_manual():
    return input("Do you want an easy pick or to pick your own numbers? easy/pick")


total_spent = 0
total_won = 0
play_again = 'Y'

while play_again == 'Y':
    total_spent += 1

    winning_ticket = get_random_numbers()

    if ask_player_for_easy_pick_or_manual() == "easy":
        user_ticket = get_random_numbers()
    else:
        user_ticket = user_pick_numbers()

    total_won += get_total_winnings(winning_ticket, user_ticket)

    print(f'total spent: {total_spent} - total won: {total_won} -  net loss: {total_won-total_spent}')

    play_again = ask_to_play_again()
