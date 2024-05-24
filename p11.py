'''Use a loop to display elements from a given list present at odd index positions
Input: my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
'''


a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(a)):
    if i % 2 != 0:
        print(a[i])

#Output: 20 40 60 80 100
