class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        operations = 0
        nums_sort = sorted(nums)
        length_nums_sort = len(nums_sort)
        left = 0
        right = length_nums_sort - 1

        while left < right:
            summ = nums_sort[left] + nums_sort[right]
            if summ > k:
                right -= 1
            elif summ < k:
                left += 1
            else:
                operations += 1
                left += 1
                right -= 1
        return operations
