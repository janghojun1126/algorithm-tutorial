import random

input_values = []
for i in range(6):
 input_value = input("유저 로또번호 입력: ")
 input_values.append(input_value)

print(input_values)
random_values = []
while(True):
 random_value = random.randrange(1, 45)
 
 if random_value in random_values:
  continue


 random_values.append(random_value) 
 if len(random_values) == 6:
  break

print(f"당첨 번호: {random_values}")

# if input_values in random_values:
#  print(f"{}")

 
