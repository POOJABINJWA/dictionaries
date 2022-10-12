# a={'a':3,'c':4, 'g':2,'e':1}
# a={1:'2',4:'3',8:'9',9:'6'}
# c=[]
# for i in a:
#     c.append(a[i])
#     max=c[0]
#     min=c[0]
# for j in range(len(c)):
#     if c[j]>max:
#         max=c[j]    
#     elif c[j]<min:
#         min=c[j] 
        
# print(max)
# print(min)           


# b={"name":["apple"],"modul":["maruti"],"binjwa":["shubham"]}
# c={}
# for i in b:
#     if type(b[i])==list:
#         for j in b[i]:
#             c.update({i:b[i][0]})
# print(c)            


# a=["shubham","pooja","rani","binjwa"]
# b=[2,3,4,5]
# c=["pooja binjwa","nikita sen","pooja shubham verma","binjwa"]
# f=[]
# e={}
# for i in range(4):
#     e.update({a[i]:{b[i]:c[i]}})
# f.append(e)
# print(f)    


# a={'a':[4,3,2,2],'b':[4,2,5],'c':[8]}
# c={}
# for i in a:
#     d=[]
#     for j in a[i]:
#         if j%2==0:
#             d.append(j)
#             c.update({i:d})
# print(c)            

# # dict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# # c=0
# for i in dict:
#     for j in dict[i]:
#         c=c+1
# print(c)

# a=  {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# c=list(a.values())
# for i in range(len(c)):
#     for j in range(len(c)):
# #         print(c[j][i],end=" ")
# #     print()    

# s = {'Aex':{'class':'V','rolld_id':2}, 'Puja':{'class':'V','roll_id':3}}
# for i in s:
#     if type(s[i])==dict:
#         for j in s[i]:
#             print(j,":",s[i][j]

# a={2:3,45:[1,4,5,],"P":1}
# print(a[45][2])

# a={2:3,4:6,5:8,8:9}
# b={'a':'pooja','b':'shubham','c':'abhisek'}
# c={'pooja':56,'shubham':12,'rani':56}
# d={}
# for i in a:
#     for j in b:
#         for k in c:
#             d.update({i:a[i]})
#             d.update({j:b[j]})
#             d.update({k:c[k]})
# print(d)            

a={'a':5,'b':4,'c':7}
b={'d':5,'e':10,'p':2}
c={}
for i in a:
    for j in b:
        c.update({i:a[i]})
        c.update({j:b[j]})
print(c)        
