'''Display numbers from a list using loop
input: numbers = [12, 75, 150, 180, 145, 525, 50]

- The number must be divisible by five
- If the number is greater than 150, then skip it and move to the next number
- If the number is greater than 500, then stop the loop
'''

number = [12, 75, 150, 180, 145, 525, 50]

for a in number:
    if a % 5 == 0:
        if a > 500:
            break
        elif a > 150:
            continue
        else:
            print(a)
            
 '''output
 : 
75
150
145
'''