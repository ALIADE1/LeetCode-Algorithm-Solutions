class Solution:
    def isBalanced(self, num: str) -> bool:
        sum_evevn, sum_odd = 0, 0
        n = len(num)

        for i in range(n):
            if i % 2 == 0:
                sum_evevn+=int(num[i])
            else:
                sum_odd+=int(num[i])
        
        return sum_evevn == sum_odd
