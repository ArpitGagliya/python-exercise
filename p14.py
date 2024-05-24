''') Print the following pattern
Write a program to print the following start pattern using the for loop
'''



a=int(input("enter a number : "))

for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ")
for i in range(a-1,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print(" ")
   
 '''output
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''