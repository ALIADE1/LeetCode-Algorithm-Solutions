class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        n = len(s)

        for x in range(n):
            if x % 2 == 0:
                ans+=s[x]
            else:
                ans+=chr(ord(s[x-1]) + int(s[x]))

        return ans
