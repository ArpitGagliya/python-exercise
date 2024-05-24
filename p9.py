'''Write a program to display all prime numbers within a range
Note: A Prime Number is a number that cannot be made by multiplying other whole 
numbers. A prime number is a natural number greater than 1 that is not a product 
of two smaller natural numbers'''



start=int(input("enter a starting point : "))
end=int(input("enter a ending point : "))

for i in range(start,end+1,1):
    for j in range(2,end+1,1):
        if i%j == 0:
            break
        elif i==j+1 :
            print(i)

'''output
enter a starting point : 25
enter a ending point : 50
29
31
37
41
43
47
'''