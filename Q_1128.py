# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
dom = [[1,2],[1,2],[1,1],[1,2],[2,2]]
count=0
for i in range(0,len(dom)-1):
    j=i+1
    for j in range(j,len(dom)):
        if dom[i] == dom[j]:
            count=count+1
        else:
            rev=dom[j][:]
            rev.reverse()
            if dom[i]== rev:
                count=count+1
print(count)
