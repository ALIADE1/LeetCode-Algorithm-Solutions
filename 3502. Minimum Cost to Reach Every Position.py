class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans = []
        v = cost[0]

        for x in cost:
            if x < v:
                v = x
                ans.append(v)
            else:
                ans.append(v)

        return ans
