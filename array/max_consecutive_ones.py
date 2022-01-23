from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        maxi = 0
        for x in nums:
            if x == 1:
                i = i + 1
            else:
                maxi = max(maxi, i)
                i = 0
        return max(maxi, i)


ss = Solution()

print(ss.findMaxConsecutiveOnes([1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1,1,1,1,0,0,0]))
print(ss.findMaxConsecutiveOnes([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1,1,1,1,0,0,0]))
print(ss.findMaxConsecutiveOnes([0,0,0,1,1,0,1,1,1,1,1,0]))  #5
print(ss.findMaxConsecutiveOnes([1,1,0,1,1,1]))  #3
print(ss.findMaxConsecutiveOnes([1,0,1,1,0,1]))  #2

