class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        maxx = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
                else:
                    if i == 0 or j == 0:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                maxx = max(maxx,matrix[i][j])

        return maxx * maxx
