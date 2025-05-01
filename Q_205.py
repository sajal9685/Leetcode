# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.

s = "egg"
t = "add"
li=[]
for i in s:
    print(i,"s")
    if (i):
        li.append((i,s.index(i)))
print(li)        
for j in t:
    pass    