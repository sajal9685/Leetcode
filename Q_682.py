# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.
ops =["-60","D","-36","30","13","C","C","-33","53","79"]
li=[]
ans=0
for i in range(0,len(ops)):
    print(li)
    if ops[i]=="C":
        li.remove((li[len(li)-1]))
    elif ops[i]=="D":
        lent=len(li)-1
        li.append((int(li[lent])*2))
    elif ops[i]=="+":
        lent=len(li)-1
        sum=int(li[lent])+int(li[lent-1])
        li.append(sum)
    else:     
        li.append(int(ops[i]))
for num in li:
    ans=ans+num
print(ans)    