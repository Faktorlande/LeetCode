class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l_s = len(s)
        l_t = len(t)
        check_res = 0
        i = j = 0
        while i < l_s:
            while j < l_t:
                if s[i] == t[j]:
                    check_res += 1
                    j += 1
                    break
                j += 1
            i += 1
        return check_res == l_s


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l_s = len(s)
        l_t = len(t)
        i = j = 0
        while i < l_s and j < l_t:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == l_s

s = "axdc"
t = "ahbgdc"
print(Solution().isSubsequence(s, t))