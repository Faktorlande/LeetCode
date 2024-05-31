"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution(object):
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s = len(str1)
        t = len(str2)
        while t:
            s, t = t, s % t

        gcd_letter = str2[:s]
        multiplier1 = len(str1) // s
        multiplier2 = len(str2) // s

        if str1 == gcd_letter * multiplier1 and str2 == gcd_letter * multiplier2:
            return gcd_letter
        return '""'



print(Solution().gcdOfStrings("ABC", "A"))



# def great_common_divisor(a, b):
#     while b:
#         a, b = b, a % b
#     return a
