# Q38.. Write a Python program to drop empty Items from a given Dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

b={'c1': 'Red', 'c2': 'Green', 'c3': None}
c={}
for x,y in b .items():
    if b[x]!=None:
        c.update({x:b[x]})
print(c)        



