from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1
    

d = Solution()
print(d.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))