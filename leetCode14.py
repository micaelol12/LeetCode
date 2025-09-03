class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = strs.pop(0)

        for str in strs:
            for i,c in enumerate(str):
                if i > len(prefix) -1 or c != prefix[i]:
                    str = prefix[0:i]
                    break
            prefix = str
            
        return prefix
        
d = Solution()
print(d.longestCommonPrefix(["flower","flow","flight"]))
print(d.longestCommonPrefix(["dog","racecar","car"]))
print(d.longestCommonPrefix(["aaa","aa","aaa"]))