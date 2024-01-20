import random
random_value = random.randrange(1, 51)
print(f"랜덤숫자: {random_value}")
count = 0
player = input("난이도를 설정하시오(상 중 하): ")
if player == "하":
  game_count = 10
elif player == "중":
  game_count = 5
elif player == "상":
  game_count = 3

count2 = game_count

for i in range(game_count):
  count = count + 1
  count2 = count2 - 1
  input_value = input("숫자를 입력해주세요: ")
  if random_value == int(input_value):
    print(f"{count}번만에 정답입니다")
    break
    
  elif random_value > int(input_value):
    print(f"{count2}번 남았고 사용자의 값이 더 작습니다")
  elif random_value < int(input_value): 
    print(f"{count2}번 남았고사용자의 값이 더 큽니다")
  else:
    print("정답이 아니다")
