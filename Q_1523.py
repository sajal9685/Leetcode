low=int(input("low =" ))
high=int(input("high =" ))
n=0

for i in range(low,high+1):
    if i%2!=0:
        n=n+1
print(n)        