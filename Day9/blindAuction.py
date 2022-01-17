from art import logo

print(f"{logo}\nWelcome to the secret auction program.")

auction_start = True
auction = {}


def add_person(person_name, bid_amount):
    new_person = {person_name: bid_amount}
    auction.update(new_person)


def who_won():
    bidder = list(auction.keys())
    values = list(auction.values())
    winning_bid = max(values)
    position = values.index(winning_bid)
    winner = bidder[position]
    print(f"The winner is {winner} with a bid of {winning_bid}")


while auction_start:

    name = input("what is your name?: ")
    bid = int(input("What's your bid?: "))
    add_person(name, bid)

    more_people = input("Are there any other bidders? Type 'yes' or 'no. \n").lower()
    if more_people == "no":
        who_won()
        auction_start = False
    elif more_people == "yes":
        auction_start = True
    else :
        print("INVALID ENTRY!!!\n\n")
        who_won()
