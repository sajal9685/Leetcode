# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
haystack = "a"
needle = "a"
li=[]
for chr in range(0,len(haystack)+1):
    for i in range(0,len(haystack)):
        pair=haystack[i:i+chr]
        li.append((pair, i))
print(li)        
for el ,idx in li:
    if el==needle:
        print (idx)
        break
else:
    print(-1)   
