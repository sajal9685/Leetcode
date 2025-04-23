# Input: columnNumber = 701
# Output: "ZY"
col = 2147483647
li=[]
while col>26:
    if col%26!=0:
        mod=col%26
        li.append(mod)
        if col/26!=0:
            col= int(col/26)
    else:
         li.append(26)
         col = int(col/26) -1            
if col<=26:
        li.append(col)
reverseList=list(reversed(li))   
output = ""
for i in reverseList:
    output += chr(i + 64)
print (output)




