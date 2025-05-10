# Input: s = "successes"

# Output: 6

# Explanation:

# The vowels are: 'u' (frequency 1), 'e' (frequency 2). The maximum frequency is 2.
# The consonants are: 's' (frequency 4), 'c' (frequency 2). The maximum frequency is 4.
# The output is 2 + 4 = 6.

# Note: Please do not copy the description during the contest to maintain the integrity of your submissions.©leetcode
s = "successes"
vowel=0
consonant=0
for chr,index in enumerate(s):
    print(chr, index)
