class Solution:
    def removeZeros(self, n: int) -> int:
        ans = ""

        for x in str(n):
            if x != '0':
                ans+=x

        return int(ans)
