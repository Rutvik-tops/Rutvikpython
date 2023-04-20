
#Creat two dictionary

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 2, 'c': 4, 'd': 5}

#create blank Dictnary
result = {}

# Check condition for addintion of two value 
for key in dict1.keys():
    if key in dict2:
        result[key] = dict1[key] + dict2[key]
    else:
        result[key] = dict1[key]

for key in dict2.keys():
    if key not in dict1:
        result[key] = dict2[key]

print(result)  

    
