class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        val = [['#'] * n for _ in range(m)]

        for i in range(m):
            val[i][0] = '.'
        for j in range(n):
            val[m-1][j] = '.'

        return [''.join(x) for x in val]
