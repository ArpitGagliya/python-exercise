'''
Iterate both lists simultaneously
Given a two ruby list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

'''

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]


for i in range(len(list1)):
    print(list1[i],list2[~i])
    
    '''out put 
10 400
20 300
30 200
40 100
'''