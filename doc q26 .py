# Q26.
# Write a Python program to print a dictionary in table format.
# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# Sample Output:
# C1 C2 C3
# 1 5 9
# 2 6 10
# 3 7 11
a=  {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
b=list(a.values())
for j in range(len(b)):
    for k in range(len(b)):
        print(b[k][j],end=" ")
    print()

