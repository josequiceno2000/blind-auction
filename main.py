from intro import intro
from bidders import bid

def main():
    bidders = {}
    new_bidder = True
    intro()
    bidder, bid_amount = bid()
    bidders[bidder] = bid_amount
    new_bidder = input("Are there any other bidders? Type 'yes' or 'no'\n> ") == "yes"

    while new_bidder:
        print("\n" * 100)
        bidder, bid_amount = bid()
        bidders[bidder] = bid_amount
        new_bidder = input("Are there any other bidders? Type 'yes' or 'no'\n> ") == "yes"
    
    print(bidders)
    


if __name__ == "__main__":
    main()