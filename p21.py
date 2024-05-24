#sublist ["h", "i", "j"] print in given nested list after g.



list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)

print(list1)

'''output
["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
'''