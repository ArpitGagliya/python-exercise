'''Replace list’s item with new value if found
You have given a ruby list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
'''


list1 = [5, 10, 15, 20, 25, 50, 20]

a = 0
for i in range(len(list1)):
    if list1[i] == 20:
        a = i
        break

if a != 0:
    list1[a] = 200

print(list1)

'''output
[5, 10, 15, 200, 25, 50, 20]
'''