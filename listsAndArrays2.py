'''
Assignment
'''

import random
numlist = []
listsum = 0

for i in range(20):
    num = random.randint(-100, 100)
    numlist.append(num)
    listsum = listsum + num

print(numlist)

numlist.sort()
print(numlist)
print("\nThe minimum is ", numlist[0])
print("The maximum is ", numlist[-1])
print("The sum is ", listsum)
print("the sum using the sum function is ", sum(numlist))
