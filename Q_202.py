# Input: n = 19
# Output: true
# Explanation:
# 1**2 + 9**2 = 82
# 8**2 + 2**2 = 68
# 6**2 + 8**2 = 100
# 1**2 + 0**2 + 0**2 = 1
n = int(input("enter: "))
seen = set()
while True:
    sum = 0
    st = str(n)
    li = []
    for chr in st:
        li.append(chr)
    listInt = [int(x) for x in li]
    for i in listInt:
        sum = sum + (i * i)
    if sum == 1:
        print(True)
        break
    elif sum in seen:
        print(False)
        break
    else:
        seen.add(sum)
        n = sum



