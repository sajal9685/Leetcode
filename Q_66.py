digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
print(digits)
joinDigits =''.join(map(str,digits))
print(joinDigits)

newDigits=str(int(joinDigits) + 1)
print(newDigits)
ans=[int(digit) for digit in newDigits]
print(ans)