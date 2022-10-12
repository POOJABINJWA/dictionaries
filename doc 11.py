# Q11.Write a Python script to merge two Python dictionaries


# dict1={"a":200,"b":100,"c":300}
# dict2={"a":100,"b":200,"c":100}
# dict3={}
# # for i,j in dict1.item():
# #     for x,y in dict2.item() :
# #         if i==x:
# #             dict3[i]=(j+y)
# # print(dict3)                       

# dict3=dict1
# dict3.update(dict2)
# print(dict3)
a={"a":100,"v":20}
b={"x":456,"y":22}
x=a
x.update(b)
print(x)