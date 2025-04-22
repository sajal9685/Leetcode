n = int(input())
# Output: false
# Explantion: 2 has only two divisors: 1 and 2.
count =1
for i in range(2,50):#10**4
    if n%i==0:
        count+=1
if count==3:
    print(True)
else:
    print(False)    


            
    
