# Q18.Write a Python program to get the maximum and minimum value in a dictionary.

a={"a":2,"b":1,"j":4,"k":3}
r=[]
for i in a:
    r.append(a[i])
    min=r[0]
    max=r[0]
    for j in range(len(r)):
        if r[j]>max:
            max=r[j]
        if r[j]<min:
            min=r[j]
print(max)
print(min)

