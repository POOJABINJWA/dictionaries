# Q24.
# Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1',
# 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})





a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

d={}
sum=0
sum1=0
for i in a:
    if "item1" in i["item"]:
        sum+=i["amount"]
        d["item1"]=sum
    else:
        sum1+=i["amount"]
        d["item2"]=sum1
print(d)