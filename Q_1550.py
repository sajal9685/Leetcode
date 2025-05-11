# Input: arr = [1,2,34,3,4,5,7,23,12]
# Output: true
# Explanation: [5,7,23] are three consecutive odds.
 
arr = [2,6,4,1]
found=False
for i in range(0,len(arr)-2):
    if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0:
        print(True)
        found =True
        
if not found:
    print(False)        