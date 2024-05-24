'''Calculate the cube of all numbers from 1 to a given number
Write a program to rint the cube of all numbers from 1 to a given number
'''

a=int(input("enter a number :- "))
b=0
for i in range(1,a+1):
    b =i*i*i
    print(i,"cube is ",b)
    
 '''output
 enter a number :- 10
1 cube is  1
2 cube is  8
3 cube is  27
4 cube is  64
5 cube is  125
6 cube is  216
7 cube is  343
8 cube is  512
9 cube is  729
10 cube is  1000
'''