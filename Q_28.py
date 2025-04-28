# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
haystack = "hello"
needle = "ll"
li=[]
for chr in range(1,len(haystack)-2):
    for i in range(0,len(haystack)):
        pair=haystack[i:i+chr]
        li.append(pair)
for el in li:
    if el==needle:
        print (0)
        break
else:
    print(-1)   
