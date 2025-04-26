class Solution:
    def romanToInt(self, s: str) -> int:
        newS = s
        sum = 0
        sub = 0
        dict = {
        "I": 1,
        "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
        "D": 500,
            "M": 1000,
            "CM": 900,
            "CD": 400,
        "IV": 4,
            "IX": 9,
            "XC": 90,
            "XL": 40,
        }

        for i in range(0, len(s) - 1):
            pair = s[i : i + 2]
            if (
                pair == "IV"
                or pair == "CM"
                or pair == "IX"
                or pair == "XL"
                or pair == "XC"
                or pair == "CD"
            ):
                pairFind = pair
                newS = newS.replace(pairFind, "")
                sub = sub + dict.get(pair)
        s = newS
        sum=sub
        for value in s:
            for key in dict.keys():
                if key == value:
                    sum = sum + dict.get(key)
        print(sum, "ans")
