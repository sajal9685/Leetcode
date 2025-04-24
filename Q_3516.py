# Input: x = 2, y = 7, z = 4
# Output: 1
# Explanation:
# Person 1 is at position 2 and can reach Person 3 (at position 4) in 2 steps.
# Person 2 is at position 7 and can reach Person 3 in 3 steps.
# Since Person 1 reaches Person 3 first, the output is 1
x = 2
y = 7
z = 4
xz=abs(x-z)
print(xz)
yz=abs(y-z)
print(yz)
if xz>yz:
    print(2)
elif yz>xz:
    print(1)
else:
    print(0)        