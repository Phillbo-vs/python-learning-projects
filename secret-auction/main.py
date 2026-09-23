from art import logo
print(logo)

keep_running = True
bid_board = {}

while keep_running:
    name = input("What is your name?")
    bid = int(input("What is your bid?"))
    bid_board[name] = bid
    if input('Are there any other bidders? Type "yes" or "no"\n').lower() == "no":
        keep_running = False
    else:
        print("\n" * 1000)

highest_bid = 0
winner = ""

for bidder in bid_board:
    if bid_board[bidder] > highest_bid:
        highest_bid = bid_board[bidder]
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}")
