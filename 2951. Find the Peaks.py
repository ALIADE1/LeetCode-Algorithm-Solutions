class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        ans = []

        for x in range(1,n-1):
            if mountain[x] > mountain[x-1] and mountain[x] > mountain[x+1]:
                ans.append(x)

        return ans
