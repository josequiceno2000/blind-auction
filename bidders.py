
def bid():
    user = input("What is your name?\n> ").capitalize()
    bid = float(input("What is your bid?\n> $"))
    return user, bid

def determine_winner(bidders: dict):
    user_max, max_amount = "", 0
    for name, bid in bidders.items():
        if bid > max_amount:
            user_max, max_amount = name, bid
    return user_max, max_amount
