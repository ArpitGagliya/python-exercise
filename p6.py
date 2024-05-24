'''Print the following pattern
Write a program to use for loop to print the following reverse number pattern
'''


a=int(input("enter a number : "))

for i in range(a,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print(" ")

'''output
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''