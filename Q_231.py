# Output: true
# Explanation: 2**4 = 16
"""n = 12
for i in range(0,32):
    if n == 2**i:
        print(True)
        break
else:
    print(False)    
"""

n=int(input("enter number="))
def poweroftwo(n):
    if n<=0:
        return False    
    if n==1:
        return True
    if n%2!=0:
        return False
    return poweroftwo(n//2)

print(poweroftwo(n))