# Q27.Write a Python program to count the values associated with key in a dictionary.
# student = [{'id': 1, 'success': True, 'name': 'Lary'},
# {'id': 2, 'success': False, 'name': 'Rabi'},
# {'id': 3, 'success': True, 'name': 'Alex'}]
# Sample input if key is id: then 6

a=[{'id': 1, 'success': True, 'name': 'Lary'}
,{'id': 2, 'success': False, 'name': 'Rabi'},
{'id': 3, 'success': True, 'name': 'Alex'}]
name=input("enter the name :")
c=0
for i in a:
        for j in i:
                if j==name:
                 c=c+i[j]   
print(c)                   











