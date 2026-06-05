class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        summ_ans = 0

        for x in str(n):
            summ_ans+=int(x)

        return summ_ans
