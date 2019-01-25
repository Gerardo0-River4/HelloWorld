'''
Kata
Gerardo Rivera
11-20-18
'''

num = int(input("Enter a 3 digit number: "))

hundredsDigit = num // 100
tensDigit = num % 100 // 10
onesDigit = num % 10

print("The digits are: (", hundredsDigit, ",", tensDigit,",", onesDigit,")")