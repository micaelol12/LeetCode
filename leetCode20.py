class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        fila = []
        dict = {'(':')','[':']','{':'}'}

        for c in s:
            if not c in dict:
                if len(fila) == 0:
                    return False
                
                x = fila.pop(-1)
                
                if dict[x] != c:
                    return False
            else:
                fila.append(c)
                
        return len(fila) == 0


d = Solution()
print(d.isValid(')'))

#print(d.isValid(']'))
#print(d.isValid('['))
#print(d.isValid('()'))
#print(d.isValid('()[]{}'))
#print(d.isValid('(]'))
#print(d.isValid('([])'))
#print(d.isValid('([)]'))