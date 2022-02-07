from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pre_val: int = None
        cur_pos: int = 1
        array_len = len(nums)
        if array_len > 0:
            pre_val = nums[0]
        else:
            return 0
        for i in range(1, len(nums)):
            if nums[i] == pre_val:
                continue
            else:
                pre_val = nums[i]
                nums[cur_pos] = pre_val
                cur_pos = cur_pos + 1
        for i in range(array_len-1,cur_pos-1,-1):
            nums.pop(i)

        #print(nums)
        #print(cur_pos)
        return cur_pos

solution=Solution

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4]
solution.removeDuplicates(solution,nums)

