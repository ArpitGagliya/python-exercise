#print 1 to user given number in pattern


a=int(input("enter the number : "))

for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end = " ")
    print(" ")
    
 '''
 1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''