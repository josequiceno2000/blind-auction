
def bid():
    user = input("What is your name?\n> ").capitalize()
    bid = float(input("What is your bid?\n> $"))
    return user, bid

def determine_winner(bidders: dict):
    return max(bidders, key=bidders.get), bidders[max(bidders, key=bidders.get)]
