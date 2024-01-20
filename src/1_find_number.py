import random
random_value = random.randrange(1, 51)
print(f"랜덤숫자: {random_value}")

for i in range(3):
 input_value = input("숫자를 입력해주세요: ")
 if random_value == int(input_value):
  print("정답입니다")
 elif random_value > int(input_value):
  print("사용자의 값이 더 작습니다")
 elif random_value < int(input_value): 
  print("사용자의 값이 더 큽니다")
 else:
  print("정답이 아니다")

 



#random.choice(>)
#print("더 크다")ㄴ
#random.choice(<)
#input("더 작다")
# random.choice([random_value])
# True
# print("정답이다")