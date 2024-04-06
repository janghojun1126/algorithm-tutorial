my_list = [i for i in range(1,1000)]
even = []
odd = []
for i in my_list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)
