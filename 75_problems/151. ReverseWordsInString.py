class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s_lst = [word.strip() for word in s.split()]
        left = 0
        right = len(s_lst) - 1
        while left < right:
            s_lst[left], s_lst[right] = s_lst[right], s_lst[left]
            left += 1
            right -= 1
        return " ".join(s_lst)


print(Solution().reverseWords("a good   example"))