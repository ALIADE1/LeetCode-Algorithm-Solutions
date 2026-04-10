class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        s1 = str(num1).zfill(4)
        s2 = str(num2).zfill(4)
        s3 = str(num3).zfill(4)

        ans = ''
        for x in range(4):
            ans+=min(s1[x],s2[x],s3[x])

        return int(ans)
