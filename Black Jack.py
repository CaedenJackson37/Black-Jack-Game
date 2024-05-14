# This program will allow you to play Black Jack against a computer dealer.
import random
# Game variable are listed here.
deck = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11)
user_cards = []
dealer_cards = []


def draw():
    new_card = random.choice(deck)
    return new_card


def dealer_draw(user_total):
    if user_total < 21:
        while sum(dealer_cards) < 17:
            dealer_cards.append(draw())
            return dealer_cards


def blackjack():
    for i in range(2):
        user_cards.append(draw())
        dealer_cards.append(draw())
    print(f'User has: {user_cards}')
    print(f'Dealer has: {dealer_cards}')


continue_game = True


print('______________________________________________________________________')
print("                  Welcome to Black Jack                 ")
print("In this game of Black Jack you try to get as close to 21 as possible.")
print("However you don't want to go over 21 or you bust.")

play_game = False
while play_game == False:
    play = input("Would you like to play? (y/n) : ").lower()
    if play == "y":
        blackjack()
        play_game = True
    elif play == "n":
        print('____________________________________________________')
        print("Thank you, goodbye.")
    else:
        print("You didn't enter 'y' or 'n' .")
while continue_game == True and sum(user_cards) < 21:
    drawing = input("Would you like another card (y/n) : ").lower()
    if drawing == 'y':
        user_cards.append(draw())
        if 11 in user_cards and sum(user_cards) > 21:
            user_cards.remove(11)
            user_cards.append(1)
        print(f'User has: {user_cards}')
        print(f'Dealer has: {dealer_cards}')
    else:
        continue_game = False

dealer_draw(sum(user_cards))

print("~~~~~~~~~~~~~~~~~~~~Final Results~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"User has {user_cards} for a total of {sum(user_cards)}")
print(f"Dealer has {dealer_cards} for a total of {sum(dealer_cards)}")
if sum(user_cards) > 21:
    print("You bust! Dealer wins!")
elif sum(user_cards) == sum(dealer_cards):
    print("It's a draw!")
elif sum(dealer_cards) >= sum(user_cards) and sum(dealer_cards) <= 21:
    print(f'Dealer Wins with: {dealer_cards}')
else:
    print(f'You win with: {sum(user_cards)}')
