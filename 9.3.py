dict1 = {'a': 100, 'b': 200, 'c': 300} 
dict2 = {'a': 300, 'b': 200, 'd': 400} 
dict3 = {}

print("dict1 =", dict1) 
print("dict2 =", dict2) 


dict3.update(dict1) 
dict3.update(dict2) 


for key in dict1: 
    if key in dict2: 
        dict3[key] = dict2[key] + dict1[key] 

print("New dict =", dict3)
