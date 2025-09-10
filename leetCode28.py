from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x = 0

        for i,c in enumerate(haystack):
            if x == len(needle):
                return i - x
            
            if c == needle[x]:
                x +=1
            else:
                x = 0


        return -1

d = Solution()
print(d.strStr("butsad","sad"))