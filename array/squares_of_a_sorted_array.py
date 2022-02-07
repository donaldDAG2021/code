import random
from typing import List


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list = [i * i for i in nums]
        return quicksort(new_list)


nums = [-4, -1, 0, 3, 10]
solution = Solution()

print(solution.sortedSquares(nums))

