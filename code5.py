#Question: Complete the script so that it prints out a list slice containing letters a, c, e, g, and i. 
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
#Expected output: 
#['a', 'c', 'e', 'g', 'i']
keyword =''
for i in letters: 
  if i =='a' or i=='c' or i=='e' or i=='g' or i=='i':
    
       keyword+=i
print(list(keyword))
