
start = 2
end = int(input("informe o número desejado"))

print ("1")
  
for i in range(start, end+1): 
  if i>1: 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i) 