accounts = [[1,2,3],[3,2,1]]
ans=0
for i in accounts:
    ans=max(ans,sum(i))
print (ans)    