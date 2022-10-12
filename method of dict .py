# d={}
# for i in range(4):
#     name =input("enter the name")
#     number=int(input("enter the number"))
#     d.update({name:number})
# print(d)    

# Adding items
# a={"w":"pooja","c":"rani","d":"arun"}
# a["v"]="poiuytf"
# print(a)

#update dictionary
# a={"brand":"rord","model":"mustang","year":1964}
# a.update({"year":2020})
# print(a)

#removing items
# a={'brand':'roed','model':'mustange','year':2022}
# a.pop('year')
# print(a)

# b={'brand':'maruti','model':'dzire','year':2020}
# c=b.popitem()
# print(c)


# #len function
# b={'brand':'maruti','model':'dzire','year':2020}
# x=len(b)
# print(x)


# b={'brand':'maruti','model':'dzire','year':2020}
# del b['brand']
# print(b)

# b={'brand':'maruti','model':'dzire','year':2020}
# b.clear()
# print(b)

# b={'brand':'maruti','model':'dzire','year':2020}
# x=b.copy()
# print(x)

# b={'brand':'maruti','model':'dzire','year':2020}
# for i in b:
#     print(i)

# b={'brand':'maruti','model':'dzire','year':2020}
# for i in b:
#     print(b[i])

# accessing items
# a={"brand":"ford","model":"mustang","year":2020}
# x=a["model"]
# print(x)


# key print
# a={"brand":"ford","model":"mustang","year":2020}
# for i in a:
#     print(i)

#values print
# a={"brand":"ford","model":"mustang","year":2020}
# for i in a:
#     print(a[i])

# key and values
# a={"brand":"ford","model":"mustang","year":2020}
# for i in a:
#     print(i,':',a[i])

# orderda
# a={"brand":"ford","model":"mustang","year":2020}
# a['w']="monday"
# print(a)

# # a=int(input("enter the number"))
# b={}
# for i in range(0,3):
# i=0
# while i<3:
#     key=input("enter outside key:-:-")
#     k={}
#     # for j in range(0,1):
#     j=0
#     while j<2:
#         keys=input("enter the inside key:-")
#         value=input("enter the inside value :-")
#         k.update({keys:value})
#         j=j+1
#     b.update({key:k})
#     i=i+1
# print(b)

# a={"brand":"ford","model":"mustang","year":2020}
# # # x=a.items()
# # # print(x)
# x=a.get("model")
# print(x)
# # c=a.pop("year")
# # print(a)


# # b={"brand":"ford","model":"mustang","year":2020}
# # x=b.keys()
# print(x)

# 
# # c={"brand":"ford","model":"mustang","year":2020}
# x=c.values()
# print(x)
# print(type(x))

# c={"brand":"ford","model":"mustang","year":2020}
# print(sorted(c))

# d={5:7,9:6,5:9,2:1,1:2}
# print(sorted(d))


# print(max(a))
# print(min(a))

# a={'name','age','rollno'}
# b={'swathi','20','23'}
# c=dict.fromkeys(a,b)
# print(c)

# a={"name":"pooja","age":20,}
# x=a.setdefault('age')
# print(x)

# 
# 


# a={5:9,3:7,6:{5:3},2:5}
# for i in a:
#     if type(a[i])==dict:
#         for j in a[i]:
#             print(a[i][j])
#     # print(i)6

    
# d={}
# for i in range(4):
#     name=input('enter the name')
#     values=input('enter the values')
#     d.update({name:values})
# print(d)    

# i=0
# d={}
# while i<3:
#     name=input("enter the ")
#     valuse=input('enter the number')
#     d.update({name:valuse})
#     i=i+1
# print(d)    


# b={}
# i=0
# while i<2:
#     key=input('enter the no1.')
#     k={}
#     j=0
#     while j<1:
#         keys=input('enter the keys')
#         valuse=input('enter the valuse')
#         k.update({keys:valuse})
#         j=j+1
#     b.update({key:k})
#     i=i+1
# print(b)    

# c={"brand":"ford","model":"mustang","year":2020}
# x=c["year"]
# print(x)


# a={'z':100,'y':20,'x':300}
# b={'z':300,'y':20,'w':400}
# for i in a:
#       if i in b: 
#           b[i]=b[i]+a[i]
#       else:
#         b[i]=a[i]
# print(b)

