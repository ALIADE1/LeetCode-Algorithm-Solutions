class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_len = n * n
        cou = {}
        a, b = 0, 0

        for listt in grid:
            for val in listt:
                cou[val] = cou.get(val, 0) + 1

        for i in range(0, total_len + 1):
            if cou.get(i, 0) == 2:
                a = i
            elif cou.get(i, 0) == 0:
                b = i

        return [a,b]
