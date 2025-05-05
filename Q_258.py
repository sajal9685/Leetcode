# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.
num = 38
while num>10:
    sum=0
    st=str(num)
    for i in range(0,len(st)):
        sum=sum+int(st[i])
    num=sum    
print(num)