class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = j = 0
        while i < l:
            if nums[i] == 0:
                j = i
                while j < l - 1 and nums[j] == 0:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
        return nums


class Solution(object):
    def moveZeroes(self, nums):
        insert_pos = 0

        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1