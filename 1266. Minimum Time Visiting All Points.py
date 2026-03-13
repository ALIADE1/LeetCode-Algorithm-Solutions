class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0

        for x in range(n-1):
            x1, y1 = points[x][0], points[x][1]
            x2, y2 = points[x+1][0], points[x+1][1]
            ans+= max(abs(x1-x2), abs(y1-y2))

        return ans
