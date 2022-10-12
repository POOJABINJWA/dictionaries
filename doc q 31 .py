# Q31.. Write a Python program to get the top three items in a shop. Go to
# the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55,
# 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3


dict1= {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
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


