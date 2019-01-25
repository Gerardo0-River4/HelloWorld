'''
Gerardo Rivera
12-5-18
Traversing lists
For loop, membership, enumerate(list) function
'''

myList = ["apples", "pears", "bananas", "oranges"]

#membebrship of an element

print("\nMembership\n")

if "watermelon" in myList:
    print("yes")
else:
    print("no")

for x in myList:
    print(x)
    # Traverse the list using indexes

for ind in range(len(myList)):
    print(myList[ind])

    # enummerate(list) - function
print("\nEnumeration\n")

for (ind,val) in enumerate(myList):
    print(ind, val)