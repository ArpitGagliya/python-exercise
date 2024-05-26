'''Initialize hash with default values
In ruby, we can initialize the keys with the same values.
Given:
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
Expected Output:
 {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
'''


employees = ['Kelly', 'Emma','sima','arpit']
defaults = {"designation": 'Developer', "salary": 8000}

a = {}
for employee in employees:
    #a[employee] = {"designation": defaults["designation"],"salary": defaults["salary"]}
    a[employee] = {"designation":defaults["designation"],"salary":defaults["salary"]}

print(a)

'''
Output: {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
'''