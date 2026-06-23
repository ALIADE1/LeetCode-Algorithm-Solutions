class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans = 0
        Counter_s = Counter(s)
        Counter_t = Counter(t)

        for x in Counter_s:
            if Counter_t[x] < Counter_s[x]:
                ans+=(Counter_s[x] - Counter_t[x])

        return ans
