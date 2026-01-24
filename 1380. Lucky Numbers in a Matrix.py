class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        min_row = []
        max_row = []

        for i in range(n):
            minn = 1e5 + 1
            for j in range(m):
                minn = min(minn,matrix[i][j])
            min_row.append(minn)

        for i in range(m):
            maxx = -1
            for j in range(n):
                maxx = max(maxx,matrix[j][i])
            max_row.append(maxx)

        # print(min_row)
        # print(max_row)
        return list(set(min_row) & set(max_row))
