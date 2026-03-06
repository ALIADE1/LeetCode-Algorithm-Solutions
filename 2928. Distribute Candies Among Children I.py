class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans_cou = 0

        for i in range(limit+1):
            for j in range(limit+1):
                for k in range(limit+1):
                    if i + j + k == n:
                        ans_cou+=1

        return ans_cou
