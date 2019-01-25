'''
Prime Num
Gerardo Rivera
11-20-18
'''

a = 2

p = 1

ct = 1

while a == 2:

    if ct == 1:

        num = int(input("Enter your number:"))
        ct = ct + 1

    else:
        num = int(input("Enter another number: "))

    for divisor in range(2, num):
        if num % divisor == 0:
            print("The number is not prme, it has a divisor: ", divisor)
            p = p + 1


    if p == 1:
        print("The number is Prime!\n")