class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        end = len(height) - 1
        left = 0
        right = end
        max_area = 0

        while left != right:
            if height[left] < height[right]:
                max_area = max(max_area, height[left] * (right - left))
                left += 1
            else:
                max_area = max(max_area, height[right] * (right - left))
                right -= 1

        return max_area

height = [1,2]


print(Solution().maxArea(height))