# Q25. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

# a='w3resource'
# d={}
# for i in a:
#     d[i]=a.count(i)
# print(d)    
   
# a=int(input('enter the number'))
# b={}
# for a in range(1,a+1):
#     b.update({a:a%2==0})
# print(b)    

a={'a':3,'b':4,'c':2}
b={'r':8,'k':9,'l':5}
c={}
for i in a:
    for j in b:
        c.update({i:a[i]})
        c.update({i:b[i]})
print(c)        







