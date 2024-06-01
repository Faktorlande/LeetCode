from typing import List
from functools import reduce


class Solution(object):
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        zeros = [0] * n
        res = [1] * n
        elem_zeros = []

        for i in range(n):
            if nums[i] == 0:
                elem_zeros.append((i, nums[i]))

        if len(elem_zeros) > 1:
            return zeros

        elif len(elem_zeros) == 1:
            nums_copy = nums[:]
            nums_copy.pop(elem_zeros[0][0])
            zeros[elem_zeros[0][0]] = self.prod_array(nums_copy)
            return zeros

        else:
            prod_nums = self.prod_array(nums)
            for i in range(n):
                res[i] = prod_nums // nums[i]

        return res

    def prod_array(self, nums):
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
        return prod

        # print(zeros)
        # def recurs_prod(nums):
        #     if len(nums) == 1:
        #         return nums[0]
        #     else:
        #         return recurs_prod(nums[1::]) * nums[0]
        #
        # n = len(nums)
        # res_lst = [1] * n
        # for i in range(n):
        #     temp, nums[i] = nums[i], res_lst[i]
        #     res_lst[i] = recurs_prod(nums)
        #     nums[i] = temp
        # return res_lst

    # def recurs_prod(self, nums):
    #     if len(nums) == 1:
    #         return nums[0]
    #     else:
    #         return self.recurs_prod(nums[1::]) * nums[0]
    # product_res = 1
    # res_lst = []
    # temp = None
    # current_one = 1
    # for i in range(len(nums)):
    #     temp, nums[i] = nums[i], current_one
    #     for j in range(len(nums)):
    #         product_res *= nums[j]
    #     nums[i] = temp
    #     res_lst.append(product_res)
    #     product_res = 1
    # return res_lst, current_one


num = [-1, 1, 0, -3, 3]
print(Solution().productExceptSelf(num))
