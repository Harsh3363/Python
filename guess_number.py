import random
import clear

def play_again(run_again):
  if run_again=="y":
              clear()
              guess_game()

def guess_game():
  print("Welcome to the number guessing game! \nI'm       thinking of a number in between 1 to 100")
  level= input("choose a difficulty level either easy     or hard: ")
  
  if level=="easy":
    num_attempt = 10
  else:
    num_attempt = 5
    
  def guess():
    return random.randint(1,100)
     
  continue_game = True
  ans = guess()
  
  while continue_game  : 
    print(f"you have {num_attempt} number of attempts") 
    num = int(input("guess a number: "))
    print(num_attempt)
    if num>ans: 
      print("guessed number is too high")
      num_attempt-=1
    elif num<ans:
      print("guessed number is too low")
      num_attempt-=1
    elif num_attempt==0:
      print("you lost")
      run_again = input("wanna play again?\n y or n: ")
      play_again(run_again)
    elif num==ans:
      print("You guessed it correct\n Congrats won!!") 
      continue_game = False
      run_again = input("wanna play again?\ny or n: ")
      play_again(run_again)
    
guess_game()
