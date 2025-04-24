# Output: true
# Explanation: 2**4 = 16
n = 12
for i in range(0,32):
    if n == 2**i:
        print(True)
        break
else:
    print(False)    
