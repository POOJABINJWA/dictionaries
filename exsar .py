# a={"name":10,"brand": "maruti","modul" :45}
# b=[]
# c=[]
# for i in a:
#     b.append(i)
#     c.append(a[i])
# print(b)
# print(c)    


# a={"name":["apple"],"rand": ["maruti"],"modul" :[45]}
# b={}
# for i in a:
#     if type(a[i])==list:
#         for j in a[i]:
#           b.update({i:a[i][0]})
# print(b)        
# print(type(a))


# a={'z':50,'y':10,'u':89}
# b={'z':20,'y':12,'c':90}
# c={}
# for i in a:
#     if i in b:
#         b[i]=b[i]+a[i]
#     else:
#         b[i]=a[i]
# print(b)            
    
# a={'o':50,'t':10,'u':89}
# b={'z':20,'y':12,'c':90}
# c={}
# for i in a:
#     for j in b:
#         c.update({i:a[i]})
#         c.update({j:b[j]})
# print(c)         



# a={}
# i=0
# while i <4:
#     name= input("enter the name ")
#     Values=input("enter the values")
#     a.update({name :Values})
#     i=i+1
# print(a)   
# 
a={}
b=int(input("enter the size first"))
for i in range(b):
    key=input("enter the key")
    size=int(input("enter the size of nested dict seconda"))
    c={}
    for j in range(size):
        n=input("enter the keys")
        values=input("enter the number")
        c[n]=values
    a[key]=c
print(a)        




