# Input: x = 123
# Output: 321
x = 120
xStr = str(x)
new = ""
ch = 'F'
for char in xStr:
    if char == "-":
        new = xStr.replace("-","",1)
        break
    elif char == "0":
        new = xStr[::-1].lstrip("0")
        ch = 'T'
        break
    else:
        new = xStr
if ch=='F':        
    xRev = new[::-1]          
    if x < 0:
        xRev = "-" + xRev
    if xRev == "":
        xRev = "0"
    print(xRev)
else:
    if x < 0:
        new = "-" + new
    print(new)

  
