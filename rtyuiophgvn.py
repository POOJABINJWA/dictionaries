a={"a":2,"b":4,"c":6,"d":4}
max=0
min=0
for i in a:
    if a[i]>max:
        max=a[i]
for i in a:
    if a[i]<min:
        if a[i]>min and  a[i]!=max:
            min=a[i]

print(max)
print(min)                   