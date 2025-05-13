# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
s =  "Hello World"
st=""
for chr in s[::-1]:
    if chr!=" ":
        st=st+chr 
    elif st:
        break
print(len(st))    
