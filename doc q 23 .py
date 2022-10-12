# Q23.Write a Python program to find the highest 3 values of corresponding keys in a
# dictionary.

dict1 = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
b=[]
max=0
max1=0
max2=0
for i in dict1:
    for j  in dict1:
        if dict1[j]>max :
          max=dict1[j]
        if dict1[j]>max1 and dict1[j]!=max:
            max1=dict1[j]   
        if dict1[j]>max2 and dict1[j]!=max and dict1[j]!=max1:
            max2=dict1[j]    
b.append(max)
b.append(max1)
b.append(max2)
print(b)   
