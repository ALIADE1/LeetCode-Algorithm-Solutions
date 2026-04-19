class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        col_st, col_end = s[0], s[3]
        row_st, row_end = int(s[1]), int(s[4])
        ans = []

        for i in range(ord(col_st), ord(col_end) + 1):
            for j in range(row_st, row_end + 1):
                ans.append(chr(i) + str(j))

        return ans
