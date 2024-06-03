class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n

            elif n <= second:
                second = n
            else:
                return True
            print(f"first: {first} second: {second}")
        return False

print(Solution().increasingTriplet([5,2,3,4,1]))