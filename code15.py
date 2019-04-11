#Question: Calculate the sum of all dictionary values.
d = {"a": 1, "b": 2, "c": 3}
#Expected output: 
 #6
sum=0
for i in d.values():
    sum+=i
d['sum']=sum
print(d)
