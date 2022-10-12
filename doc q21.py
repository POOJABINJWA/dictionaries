# Q21.Write a Python program to print all unique values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
# {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}


s= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
l=[]
for j in s:
    for i in j:
        if j[i] not in l:
            l.append(j[i])

print(set(l))











# a={'1':['a', 'b'], '2':['c', 'd']}
# b= list(a.values())
# for i in b[0]:
#     for j in b[1]:
#         print(i+j)


