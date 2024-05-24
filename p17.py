''') Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
'''


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

a = []
for i in range(len(list1)):
    for j in range(len(list2)):
        c=list1[i] + list2[j]
        a.append(c)
print(a)

#output:--  ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
