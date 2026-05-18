n=int(input("enetr number="))   
new=n 
ans=0
while new>0:
    r= new%10
    if n%r==0:
        ans+=1
print(ans)        

