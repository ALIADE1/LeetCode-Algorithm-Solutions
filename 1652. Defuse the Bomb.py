class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n

        if k == 0:
            return ans

        elif k > 0:
            for i in range(n):
                summ = 0

                for j in range(1,k+1):
                    summ+=code[(j+i)%n]
                ans[i] = summ
            return ans

        else:
            for i in range(0,n):
                summ = 0

                for j in range(1,abs(k)+1):
                    summ+=code[(i-j)%n]
                ans[i] = summ
            return ans
