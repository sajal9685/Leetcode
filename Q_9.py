
#palindrome number = reverse of which number is same as before reversing
x=int(input())
xStr= str(x)
xRev=xStr[:: -1]
if xStr ==xRev:
    print (True)
else:
    print (False)


