import art
import game_data
import random
# import clear

GAME_DATA = game_data.data
PLAY_GAME = True

# a = random.randint(0,50)
# b = random.randint(0,50)

points = 0

# comp_a = GAME_DATA[a]
# comp_b = GAME_DATA[b]

# comp_a_follower = int(GAME_DATA[a]["follower_count"])
# comp_b_follower = int(GAME_DATA[b]["follower_count"])

# print(comp_a_follower)
# print(comp_b_follower)

print(art.logo)
while PLAY_GAME:
  a = random.randint(0,50)
  b = random.randint(0,50)

  comp_a = GAME_DATA[a]
  comp_b = GAME_DATA[b]
  
  comp_a_follower = int(GAME_DATA[a]["follower_count"])
  comp_b_follower = int(GAME_DATA[b]["follower_count"])
  
  print(comp_a_follower)
  print(comp_b_follower)
  
  print(f'Compare A: {comp_a["name"]},a {comp_a["description"]}, from {comp_a["country"]}')
  print(art.vs)
  print(f'Compare B: {comp_b["name"]},a {comp_b["description"]}, from {comp_b["country"]}')
  ans = input("who has more follower A or B: ").upper()
  
  if ans=="A" and comp_a_follower>comp_b_follower:
      points+=1
      print(f"you guessed it correct, your point is {points} ")
      
  elif ans=="B" and comp_b_follower>comp_a_follower:
      points+=1
      print(f"you guessed it correct, your point is {points} ")
      
  else:
    print(f"you guessed it wrong, your score is {points}")
    PLAY_GAME = False
    

