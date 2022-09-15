import art
from replit import clear
#HINT: You can call clear() to clear the output in the console.
print(art.logo)

auction = {}
bidding_finished = False
def max_bid(bidding_record):
  temp = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = auction[bidder]
    if bid_amount>temp:
      temp=bid_amount
      winner=bidder
  print(f"winner is {winner} and winning bid is {temp}")
while not bidding_finished:
  name = input("enter your name ")
  bid = int(input("enter your bid amouint: $"))
  auction[name] = bid 
  should_continue = input("is there any other bidder? ")
  if should_continue=="no":
    bidding_finished = True
    max_bid(auction)
  elif should_continue=="yes":
    clear()
