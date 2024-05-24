'''Find the sum of the series upto n terms
Write a program to calculate the sum of series up to n term. For example, 
if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
'''

number=int(input("enter a number : "))
a=0
b=2
for i in range(1,number+1):
    a += b
    b = b * 10 + 2
print(a)

'''output
enter a number : 5
24690
'''