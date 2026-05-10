class Solution:
    def totalMoney(self, n: int) -> int:
        q, r = divmod(n, 7)
        summ_ans, i, j = 0, 1, 7
        l, r = q + 1, q + r

        for _ in range(q):
            summ_ans+=((j-i+1)*(j+i))//2
            i+=1
            j+=1

        return summ_ans + ((r-l+1) * (r+l)) // 2
