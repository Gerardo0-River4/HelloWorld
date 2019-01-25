'''
1.) swapping two variables
2.) Fibonacci Sequence
'''

a = 5
b = 10
print(a,b)

temp = 0 #temporary variabale is created

temp = a #temporary variable is used to save value of a
a = b    #value of b is given to a
b = temp #b recieves previous value of a via temp
print(a,b)

print()

    #WHILE LOOPS

x = 1
while x < 10:
    print(x,end='')
    x = x + 1
print()


x = 1
y = 1
z = 1
cont = 1#cont = 'c'
n = int(input("Enter how many numbers you'd like"))
while cont <= n - 1:

    print(x + y)
    z = x
    x = y
    y = y + z

    cont = cont + 1
print("Fibonacci number is ",x + y)
