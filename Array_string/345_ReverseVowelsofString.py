# class Solution(object):
#     def reverseVowels(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         length = len(s)
#         vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
#         res = ''
#         reverse_vowels_str = [(s[i] for i in range(length - 1, -1, -1) if s[i] in vowels)]
#
#         for i in range(length):
#             if s[i] in vowels:
#                 res += next(reverse_vowels_str)
#             else:
#                 res += s[i]
#         return res




class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s_lst = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s_lst[left] not in vowels:
                left += 1

            elif s_lst[right] not in vowels:
                right -= 1

            else:
                s_lst[left], s_lst[right] = s_lst[right], s_lst[left]
                left += 1
                right -= 1
        return "".join(s_lst)

s = 'hello'
print(Solution().reverseVowels(s))