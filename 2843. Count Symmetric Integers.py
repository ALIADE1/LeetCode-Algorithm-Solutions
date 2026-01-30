class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0

        for x in range(low,high+1):
            n = len(str(x))
            s = str(x)

            if n % 2 != 0:
                continue

            c_n = n // 2
            sum1, sum2 = 0, 0

            for i in range(0,c_n):
                sum1+=int(s[i])
                
            for i in range(c_n,n):
                sum2+=int(s[i])
            
            if sum1 == sum2:
                ans+=1

        return ans
