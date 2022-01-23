from typing import List


class Solution:
    def findMaxConsecutiveOnes2(self, nums: List[int]) -> int:
        i = 0
        maxi = 0
        for x in range(len(nums)):
            if nums[x] == 1:
                i = i + 1
            else:
                maxi = max(maxi, i)
                i = 0
        return max(maxi, i)

ss=Solution()
#print(ss.findMaxConsecutiveOnes2([1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1,1,1,1,0,0,0]))
# print(ss.findMaxConsecutiveOnes2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1,1,1,1,0,0,0]))
# print(ss.findMaxConsecutiveOnes2([0,0,0,1,1,0,1,1,1,1,1,0]))  #5
print(ss.findMaxConsecutiveOnes2([1,1,0,1,1,1]))  #3
print(ss.findMaxConsecutiveOnes2([1,0,1,1,0,1]))  #2
