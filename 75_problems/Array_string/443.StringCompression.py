class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        res = ''
        length = len(chars)
        groups = ''
        i = j = 0

        while i < length:
            i = j
            if i < length and chars[i] != groups:
                groups = chars[i]
                count_char = 1
                while j < length and chars[j] == groups:
                    j += 1
                    count_char += 1
                if count_char > 2:
                    res += chars[j - 1] + str(count_char - 1)
                else:
                    res += chars[j - 1]
        length = len(res)
        for i in range(len(res)):
            chars[i] = res[i]

        return length



chars = ["a","a","b","c","c","c"]
print(Solution().compress(chars))
