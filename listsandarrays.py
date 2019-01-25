'''
Lists and thier methods (9operations and about lists)

'''

mylist = ["apples", "pears", "grapes", "oranges"]

print(mylist)

print(len(mylist))

# Position of each element in the list
'''
print(mylist[0])

print(mylist[1])

print(mylist[3])

print(mylist[-1])
print(mylist[-2])
'''

#adding an element to the list

mylist.append("banana")
print(mylist)

mylist.append("watermelon")
print(mylist)

'''
mylist.append(9)
mylist.append(1)
print((mylist[6]) + (mylist[7]))
'''

'''
mylist.reverse()
print(mylist)
'''

'''
mylist.pop(0)
print(mylist)
'''

new_list = mylist.copy()
print(new_list)
new_list.clear()
print(new_list)
