# Q48.Write a Python program to find the length of a given dictionary values.
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}
# Original Dictionary:

a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
c={}
for i in a:
    for j in a:
        if a[i] not in c:
            c.update(a[i][j])
print(c)            
