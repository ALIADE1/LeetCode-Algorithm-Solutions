class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans = []

        for x in tasks:
            ans.append(x[0] + x[1])

        return min(ans)
