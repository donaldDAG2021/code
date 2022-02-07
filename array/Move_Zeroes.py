from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        j = 0
        while j < len(arr):
            if arr[j] == 0:
                j += 1
            else:
                arr[i] = arr[j]
                i += 1
                j += 1

        while i < len(arr):
            arr[i] = 0
            i += 1
        print(arr)

solution = Solution()

nums = [0, 1, 0, 3, 12]
print(solution.duplicateZeros(nums))