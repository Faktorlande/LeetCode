class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left = 0
        right = k
        max_sub_sum = prev_sum = sum(nums[left:right])
        while right <= len(nums) - 1:
            current_sum = prev_sum - nums[left] + nums[right]
            if max_sub_sum < current_sum:
                max_sub_sum = current_sum
            prev_sum = current_sum
            left += 1
            right += 1
            print(f'{nums[left:right]}, current_sum:  {current_sum}, {right}')

        return max_sub_sum / k

print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))
