from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        i = 0
        for x in nums:
            if len(str(x)) % 2 == 0:
                i = i + 1
        return i

    def findNumbers2(self, nums: List[int]) -> int:
        i = 0
        for x in nums:
            if len(str(x)) % 2 == 0:
                i = i + 1
        return i


solution = Solution()
print(solution.findNumbers([555, 901256784563, 482, 484, 1771, 177122]))




solution2 = Solution()
print(solution2.findNumbers2([555, 901256784563, 482, 484, 1771, 177122]))



# def findNumbers(self, nums: List[int]) -> int:
#     num = nums[0]
#     if ((num >> 1 & 1) == 1 or (num >> 1 & 1) == 0) and ((num >> 0 & 1) == 0):
#         print(bin(num)[-2:])
#         print('чет')
#     else:
#         print('НЕ чет')
#     return num