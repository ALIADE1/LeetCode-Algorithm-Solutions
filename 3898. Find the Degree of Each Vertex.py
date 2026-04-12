class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = []

        for x in matrix:
            ans.append(sum(x))

        return ans
