#Question: Filter the dictionary by removing all items with a value of greater than 1.
d = {"a": 1, "b": 2, "c": 3}
#Expected output: 
#{'a': 1}
for i  in d.values(),d.keys():
      if i>1:
        d.pop(i)
print(d)
      
