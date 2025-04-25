# Input: x = 123
# Output: 321
x = 901000
xStr = str(x)
new = ""
for char in xStr:
    if char == "-":
        new = xStr.replace("-","",1)
        break
    elif char == "0":
        new = xStr[::-1].lstrip("0")
        break
    else:
        new = xStr
xRev = new[::-1]          
if x < 0:
    xRev = "-" + xRev
if xRev == "":
         xRev = "0"      
  
print(xRev)
