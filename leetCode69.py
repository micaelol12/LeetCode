class Solution(object):
    def mySqrt(self, x):
        # busca binaria entre 1 e x:
        if x == 0:
            return 0
        
        l,r = 1,x

        while l <= r:
            mid = (l + r) // 2
            y = mid * mid 

            if y == x:
                return mid
            elif y < x:
                l = mid + 1
            else:
                r = mid - 1
                
        return r


d = Solution()
print(d.mySqrt(9))