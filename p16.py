'''Turn every item of a list into its square
Given a list of numbers. write a program to turn every item of a list into its square.
'''

numbers = [1, 2, 3, 4, 5, 6, 7]

a=[]
for i in range(len(numbers)):
    a.append(numbers[i] * numbers[i])
print(a)

#output:--  [1, 4, 9, 16, 25, 36, 49]