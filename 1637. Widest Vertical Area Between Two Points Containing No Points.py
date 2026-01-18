class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        max_wid = 0
        n = len(points)

        for x in range(1,n):
            wid = points[x][0] - points[x-1][0]
            max_wid = max(max_wid, wid)

        return max_wid
