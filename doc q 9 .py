c={}
a=int(input("enter the number :"))
i=0
while i<(a):
    key=input("enter the key")
    s=[]
    d=int(input("enter the number"))
    j=0
    while j< d:
        h=input("enter the number")
        s.append(h)
        j=j+1   
    i=i+1
    c.update({key:s}) 
print(c)    


