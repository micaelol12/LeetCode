from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i,n in enumerate(nums):
            if n != val:
                nums[k] = nums[i]
                k+=1

        return k

d = Solution()
print(d.removeElement([0,2,3,4,5,3,1,0],3))