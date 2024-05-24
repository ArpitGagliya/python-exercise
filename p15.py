''' Concatenate two lists index-wise
Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
Given:
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
'''

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

a=[]
length= max(len(list1),len(list2))

for i in range(length):
    c = ""

    if i < len(list1):
        c += list1[i]

    if i < len(list2):
        c += list2[i]

    a.append(c)
print(a)

'''output
['My', 'name', 'is', 'Kelly']
'''