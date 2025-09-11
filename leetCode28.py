class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_l = len(needle) 
        
        for i in range(len(haystack) - needle_l + 1):
            x  = 0
            
            while x < needle_l and haystack[i + x] == needle[x]:
                x += 1
            
            if x == needle_l:
                return i

        return -1
    
d = Solution()
print(d.strStr("mississippi","issipi"))
print(d.strStr("aa","aaa"))
print(d.strStr("sadbutsad","sad"))