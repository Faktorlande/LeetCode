"""
https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75
"""

from typing import List

class Solution(object):
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        res = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                empty_left_plot = (i == 0) or flowerbed[i - 1] == 0
                empty_right_plot = (i == len(flowerbed) - 1) or flowerbed[i + 1] == 0
                if empty_left_plot and empty_right_plot:
                    flowerbed[i] = 1
                    res += 1
                    if res >= n:
                        return True
        return res >= n

print(Solution().canPlaceFlowers([1,0,0,0,1,0,0], 2))

            # res = 0
            # length = len(flowerbed)
            # prev = -1
            # next_i = 1
            # i = 0
            # while next_i < length + 1:
            #     if prev == -1 and next_i == length and flowerbed[i] == 0:
            #         res += 1
            #         flowerbed[i] = 1
            #     elif prev == -1 and flowerbed[i] == 0 and flowerbed[next_i] == 0:
            #         res += 1
            #         flowerbed[i] = 1
            #     elif next_i == length and flowerbed[i] == 0 and flowerbed[prev] == 0:
            #         res += 1
            #         flowerbed[i] = 1
            #     elif flowerbed[i] == 0 and flowerbed[prev] == 0 and flowerbed[next_i] == 0:
            #         res += 1
            #         flowerbed[i] = 1
            #     if res >= n:
            #         return True
            #     prev += 1
            #     next_i += 1
            #     i += 1
            # return res >= n