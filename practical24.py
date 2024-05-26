'''Convert two lists into a hash
Below are the two lists. Write a ruby program to convert them into a hash in a way that 
item from list1 is the key and item from list2 is the value'''



keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

a = {}
for i in range(len(keys)):
    b = keys[i]
    c = values[i]
    a[b] = c
print(a)


'''output
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
'''