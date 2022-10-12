# Q19.
# Write a Python program to remove duplicates from Dictionary.
student_data = {'id1':
{'name': ['Sara'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
'id2':
{'name': ['David'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
'id3':
{'name': ['Sara'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
'id4':
{'name': ['Surya'],
'class': ['V'],
},
}
# d=[]
# for i in student_data:
#     d.append(student_data[i])
#     for j in range(len(d)):
#         if j not in d:
#             d.append(j)
# print(d)            

a={}
for i,j in student_data.items():
    if j not in a.values():
        a[i]=j
print(a)        