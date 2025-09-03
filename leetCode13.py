class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        v = 0
        last = (0, 0)
        values = { 'I': (1,1), 'V':(5,2),'X':(10,3),'L':(50,4),'C':(100,5),'D':(500,6),'M':(1000,7)}
        
        for c in s:
            x,i = values[c]
            l,z = last
            pos = i-z
            
            if  pos > 0 and pos <= 2:
                v -= 2 * l
            
            last = (x,i)
            v += x

        return v


d = Solution()
print(d.romanToInt('III'))
print(d.romanToInt('LVIII'))
print(d.romanToInt('MCMXCIV'))

