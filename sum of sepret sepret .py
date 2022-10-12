c={"a":[2,3,4],"b":[5,7,8],"c":[1,2,3]}
d=[]
h={}
for f in c:
    d.append(c[f])
    for i in range(len(d)):
        g=[]
        sum=0
        for j in range(len(d[i])):
            sum=sum+d[i][j]
        g.append(sum)
        h.update({f:g})
print(h)        
