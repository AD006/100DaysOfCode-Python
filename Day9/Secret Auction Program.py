logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welome to the secret auction program.")

bid = {}
# name=input("What is your name?: ")
# bids=int(input("What's your bid?: $"))

# bidders[name]=bids

# other_bidders=input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

continue_bidding=True
while continue_bidding:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bid[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bid)
  elif should_continue == "yes":
    print("\n"*1000)

# continue_bidding=True
# while continue_bidding:
#   name=input("What is your name?: ")
#   bids=int(input("What's your bid?: $"))
#   bidders[name]=bids
#   other_bidders=input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
#   if other_bidders == "no":
#     continue_bidding=False
#     find_highest_bidder(bids)
#   elif other_bidders == "yes":
#     print("\n"*100)


