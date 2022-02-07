from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while n > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[n+m-1] = nums2[n-1]
                n = n - 1
            else:
                nums1[n+m-1] = nums1[m-1]
                m = m - 1
        print(nums1)



nums1 = [1, 2, 3, 4, 0, 0, 0]
m = 4
nums2 = [2, 5, 6]
n = 3

solution = Solution
solution.merge(solution, nums1, m, nums2, n)


nums1 = [0]
m = 0
nums2 = [1]
n = 1
solution = Solution
solution.merge(solution, nums1, m, nums2, n)