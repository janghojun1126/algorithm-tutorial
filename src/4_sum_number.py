def mysum(my_list):
    total = 0
    for i in my_list:
        total = total + i

    return(total)


my_list = [1,2,3,4,5]
result =mysum(my_list)

my_list2 = [11,22,33,44,55]
result2 = mysum(my_list2)
print(result2)
