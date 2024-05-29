from typing import List


class Solution(object):
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_number_candies = max(candies)
        result = [False if (max_number_candies - candy > extraCandies) else True
                  for candy in candies]

        return result


print(Solution().kidsWithCandies([12,1,12], 10))
