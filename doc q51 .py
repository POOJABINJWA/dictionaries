# Q51.Write a Python program to filter even numbers from a given dictionary values.
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}
# a= {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
#   




# a= {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# b={}
# for i in a:
#     s=[]
#     for j in a[i]:
#         if j%2==0:
#             s.append(j)
#             b.update({i:s})
# print(b)               

   
a= {'V': [1, 4, 6], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
b={}
for i in a:
    c=[]
    sum=0
    for j in a[i]:
        sum=sum+j
    c.append(sum)
    b.update({i:c})
print(b)               

   
