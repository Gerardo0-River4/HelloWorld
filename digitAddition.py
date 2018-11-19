'''
Addition of 5 digits
11-19-28
Gerardo Rivera
'''

print("Eter a 5 digit number!")

number = int(input())

tenThousands = number // 10000
thousands = number // 1000 % 10
hundreds =  number // 100 % 10
tens = number // 10 % 10
ones = number // 1 % 10

print(tenThousands, " + " ,thousands, " + " ,hundreds, " + " ,tens, " + " ,ones, " = " ,tenThousands + thousands + hundreds + tens + ones)