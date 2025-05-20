# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
s = "Let's take LeetCode contest"
st=""
ans=""
for chr in s:
    st=st+chr
    if chr==" ":
        for i in st[::-1]:
            ans=ans+i
        st=""
else:
    ans=ans+" "
    for i in st[::-1]:
        ans=ans+i

print(ans)            

            

    