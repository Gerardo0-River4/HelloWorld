'''
Operations with Lists
Keyewords : addition(conactenate), slices, deleting(removing) elements
Gerardo Riverra
12-6-18
'''

from gerardolib import fibon_sequence




alist = ["a", "b", "c", "d", "e"]
blist = ["v", "w" ,"x", "y", "z"]

# Concatenation
print(alist + blist)
print(alist)

# slicing lists
print("\nSLICING LISTS\n")

print(alist[1:3])
print(alist[1:1])
print(alist[0:])

#Squeezing lists
print("\nSQUEEZING LISTS\n")

alist[3:3] = blist[0:]
print(alist)
alist = ["a", "b", "c", "d", "e"]

#Erase
print("\nERASE\n")

alist[3:7] = []
print(alist)
alist = ["a", "b", "c", "d", "e"]

#deleting elements with del list[index]
print("\nDELETING ELEMENTS\n")

del alist[0]
print(alist)
alist = ["a", "b", "c", "d", "e"]


fibon_sequence(5)