# thisdict={"brand" : "Ford" , "model": "Mustang" ,"year" : 1964}
# print(thisdict)

# city_population = {
# "NewYorkCity":8550405,
# "LosAngeles":3971883,
# "Toronto":2731571, 
# "Chicago":2720546, 
# "Houston":2296224, 
# "Montreal":1704694, 
# "Calgary":1239220, 
# "Vancouver":631486, 
# "Boston":667137
# }

# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population))


# Dict = {   'ball' : 'green',   'Ball': 'red', }
# print(Dict['ball'])
# print(Dict['Ball'])
# print(Dict['bat'])


# student=dict(name= "Ravina",age= 20)
# print(student)

# person={
# 'name':'jack',
# 'age':20,
# 'gender':'male',
# 4:'organization'
# }

# result = person['age'] 
# x = person.get('gender')
# # print(person[4])
# print(x)
# print(result)

# dic= {
# 'Name': 'RAM', 
# 'Age': 17,
# }
# dic['ORGANIZATION'] = "NAV GURUKUL"

# dic['place'] = 'dharamsala'

# print(dic)

# car ={"brand":  "ford","model":  "mustang","year":  1964
# }
# if "model" in car:
#     print("Yes, 'model' is one of the keys in the car dictionary.")

# else:
#     print("No, 'model' key dictionary mai nahi hai.")


# d1={"abc":5,"def":6,"ghi":7}
# print(d1[0])

# person= {'1': 'RAM', '2': 17,}
# person[3] = 'male'
# print(person)



# classes ={
# "room1":  "6th",
# "room2":  "7th",
# "room3":  "8th"
# }
# mydict=classes.copy()
# print(mydict)


# Using the pop( ) method we can remove a specified element from the dictionary.

# CAR_DETAILS={
# "brand": "Ford",
# "model": "jason",
# "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS)

# The popitem() method removes the last inserted item:
# person={
# 'name':'jack',
# 'id':22,
# 'place':'dharamsala'
# }
# person.popitem()
# print(person)

# Using the del keyword we can remove a specified element from the dictionar
# person={
# 'name':'jack',
# 'id':22,
# 'place':'dharamsala'
# }

# del person['place']
# print(person)


# states_capitals = {
# 'Gujarat' : 'Gandhinagar',
# 'Maharashtra' : 'Mumbai',
# 'Rajasthan' : 'Jaipur',
# 'Bihar' : 'Patna'
# }

# for state in states_capitals:
#   print(states_capitals[state])

# details ={
# "name":  "Bijender",
# "age":  17,
# "class":  "10th"
# }
# for x in details.values():
#   print(x)


# movie ={
# "name":  "Puli",
# "hero":  "Vijay",
# "rating":  7.5
# }
# for x,y in movie.items():
#   print(x,y)



# meal ={
# "monday":  "Chole chawal",
# "sunday":  "Fried rice",
# "wednesday":  "dosa"
# }
# print(len(meal))


# A = {1 : "One", 2 : "Two", 3 : "Three"}
# B = {'A' : "Apple", 'B' : "Bat", 'C' : "Cat", 'D' : "Doll"}
# A.update(B)
# print(A)

# a={1:"A",2:"B",3:"C"}
# b={4:"D",5:"E"}
# a.update(b)
# print(a)


    
# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic4={}
# for i,j in dic1.items():
#     for x,y in dic2.items():
#         for a,b in dic3.items():
#             if i==x or x==a:
#                 dic4[i]=(j+y)
#             else:
#                 dic4[i]=j
#                 dic4[x]=y 
#                 dic4[a]=b
# print(dic4)                   



# # d = {"john":40, "peter":45}
# # print(list(d.keys()))

# a={1:"A",2:"B",3:"C"}
# for i,j in a.items():
#    print(i,j,end=" ")

# a={1:"A",2:"B",3:"C"}
# print(a.setdefault(3))

# a={1:"A",2:"B",3:"C"}
# b=a.copy()
# b[2]="D"

# print(a)

# dict1={"name":"raju", "marks":56}
# a= input(" ")   
# if a in dict1:
#     print("eixst")
# else:
#     print("not eixst")        


# dict1={"data1":100,"data2":-54,"data3":247}
# s=0
# for i in dict1:
#     s=s+dict1[i]
# print(s)    
    
# a={1:"A",2:"B",3:"C"}
# for i in a:
#   print(i,end=" ")


# a={1:"A",2:"B",3:"C"}
# a.items()



# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# i=0
# b={}
# while i<len(list1):
#     b.update({list1[i]:list2[i]})
#     i=i+1
# print(b)  
# 
 
# dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
# print(dic)    



# a={'sonu':85,'Kartik':90,'Deepak':96,'Aman':76,'Somesh':60,'Umesh':85,'Amarpal':70,'Roshan':57,'Riyaz':98,'Shabid':56}
# c={}
# for  i in range (1,5):
#     name= (input("enter the name"))
#     marks=int(input("enter the marks"))
#     c[name]=marks
# print(c)

# d1="MISSISSIPPI"
# d2={}
# for i in (d1):
#     d2[i]=d1.count(i)
# print(d2)    

# Dic= {1: 'NAVGURUKUL',2: 'IN',    3:{ 'A' : 'WELCOME', 'B' : 'To', 'C' : 'DHARAMSALA'}}
# del Dic[3]["A"]
# print(Dic)


# a=[{"first":"1"},  {"second": "2"},  {"third": "1"},  {"four": "5"},  {"five":"5"},  {"six":"9"}, {"seven":"7"}]
# b=[]
# for i in a:
#     for j in i:
#         if i[j]not in b:
#             b.append(i[j])
# print(b)


# Output :-

# ['2', '7', '9', '5', '1']


# dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# c=0
# for i in dict1:
#     for j in dict1[i] :
#         c=c+1  
# print("count total",c)        
        

# dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# b=[]
# max=0
# for i in dict:
#     if dict[i]>max :
#         max=dict[i]

# b.append(max)
# print(b)        
# dict1 = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# b=[]
# max=0
# max1=0
# max2=0
# for i in dict1:
#     for j  in dict1:
#         if dict1[j]>max :
#           max=dict1[j]
#         if dict1[j]>max1 and dict1[j]!=max:
#             max1=dict1[j]   
#         if dict1[j]>max2 and dict1[j]!=max and dict1[j]!=max1:
#             max2=dict1[j]    
# b.append(max)
# b.append(max1)
# b.append(max2)
# print(b)        

# a = {(1,2):1,(2,3):2}
# print(a[1,2])
# ouputa=1
# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])
# output keyError

# c={}
# for i in range(1,5):
#     c[i]=i**2
# print(c)       


# from audioop import reverse


# dict1={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# a=[]
# for i in dict1:
#     a.append(dict1[i])
# k=sorted(a)
# dic={}
# for i in k:
#     for j in dict1:
#         if i==dict1[j]:
#             dic.update({j:dict1[j]})
# print(dic)
# k.reverse()
# dic={}
# for i in k:
#     for j in dict1:
#         if i==dict1[j]:
#             dic.update({j:dict1[j]})
# print(dic)

  
# for i in dict1:
#     a.append(dict1[i])
# for i in range(len(a)): = {1 : "One", 2 : "Two", 3 : "Three"}
# B = {'A' : "Apple", 'B' : "Bat", 'C' : "Cat", 'D' : "Doll"}
# A.update(B)
# print(B)
# #     for  j in range(len(a)-1):
# #         if a[j]<a[j+1]:
# #             tem=a[j]
#             a[j]=a[j+1]
#             a[j+1]=tem
# print(a)



# d={}
# for i in range(3):
#     name = input("enter the name")
    

# a="pooja"
# b="binjwa"
# c=" "
# print(a+c+b)




# a={'a':5,'b':4,'c':7}
# b={'d':5,'e':10,'p':2}
# c={}
# for i in a:
#     for j in b:
#         c.update({i:a[i]})
#         c.update({j:b[j]})
# print(c)        


# a={1:2,3:7,7:6,4:8,3:9}
# b=int(input("enter the number"))
# for i in a:
#     if a[i]==b:
#         c="it is present"
#     else:
#         c="it is not present" 
# print(c)           

# a={'b':7,'c':{'s':2,'f':{'e':6}},'o':6}
# print(a['c']['f']['e'])
# print(a["c"]["f"]["e"])

# a={'a':1,'b':2,'c':2,'d':1,'c':3}
# c=[]
# for i in a:
#     if a[i] not in c:
#         c.append(a[i])
# print(c)        

# d={}
# a=int(input("enter the number :"))
# for i in range(a):
#     keys=input("enter the keys :")
#     size=int(input("enter the size dict nested :"))
#     c={}
#     for j in range(size):
#         n=input("enter the number n :")
#         values=input("enter the values :")
#         c[n]=values
#     d[keys]=c
# print(d)     
# 
# c={}
# i=0
# while i<3:
#     name=input("enter the  name :")
#     age=int(input("enter the age :"))
#     c.update({name:age})
#     i=i+1
# print(c)       


# a=['pooja','nikita','rani','shubham']
# b=[12,34,56,78,]
# h={}
# c=[]
# for i in range(4):
#         h.update({a[i]:b[i]})
# # c.append(h)
# print(h)