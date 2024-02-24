import random

rock = 1
scissors = 2
paper = 3
player_value = 0

ROCK = "rock"
SCISSORS = "scissors"
PAPER = "paper"

# 플레이어 값 입력
player = input("rock, scissors, paper: ")
if player == ROCK:
 player_value = rock
elif player == SCISSORS:
 player_Value = scissors
elif player == PAPER:
 player_value = paper

#  AI 값 생성
ai_value = random.randrange(1, 4)
if ai_value == paper:
 print(f"AI: {PAPER}")
elif ai_value == scissors:
 print(f"AI: {SCISSORS}")
elif ai_value == rock:
 print(f"AI: {ROCK}")

# 승리 여부 확인
if player_value == rock:
 if ai_value == rock:
  print("무승부")
 elif ai_value == scissors:
  print("player win")
 elif ai_value == paper:
  print("player lose")

elif player_value == scissors:
 if ai_value == scissors:
  print("무승부")
 elif ai_value == paper:
  print("player win")
 elif ai_value == rock:
  print("player lose")

elif player_value == paper:
 if ai_value == paper:
  print("무승부")
 elif ai_value == rock:
  print("player win")
 elif ai_value == scissors:
  print("player lose")
