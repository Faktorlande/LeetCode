class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels_dict = {
            'a': 1,
            'e': 1,
            'i': 1,
            'o': 1,
            'u': 1,
        }
        sum_vowels_current = 0
        sum_vowels_prev = 0
        sum_vowels_max = float('-inf')

        left = 0
        right = k

        while right <= len(s):
            if left == 0:
                current_str = s[left:right]
                for i in range(k):
                    sum_vowels_current += vowels_dict.get(current_str[i], 0)
            else:

                prev_str = s[left-1:right-1]
                current_str = s[left:right]
                sum_vowels_current = sum_vowels_prev - vowels_dict.get(prev_str[0], 0) + vowels_dict.get(current_str[-1], 0)

            if sum_vowels_current > sum_vowels_max:
                sum_vowels_max = sum_vowels_current
            sum_vowels_prev = sum_vowels_current
            sum_vowels_current = 0

            left += 1
            right += 1
        return sum_vowels_max

s = "weallloveyou"
k = 7

print(Solution().maxVowels(s, k))
