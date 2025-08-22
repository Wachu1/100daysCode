import os
auction = {}

def find_highest(bidding_dictionary):
    winner = ""
    highest_bid = 0

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

print("Welcome to the secret auction program")
next_round = True

while next_round:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auction[name] = bid

    next_quest = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if next_quest == 'yes':
        print("\n" * 100)
    else:
        next_round = False
        find_highest(auction)
