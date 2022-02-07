from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        num_count = 0
        for x in nums:
            num_size = 1
            while True:
                if x < 10:
                    break
                else:
                    x = x/10
                    num_size = num_size + 1
            if num_size % 2 == 0:
                num_count = num_count + 1
        return num_count

solution = Solution ()
print(solution.findNumbers([12, 345, 6, 78, 55, 667555, 654321]))