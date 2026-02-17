class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        summ_ans = 0
        n = len(nums)

        for i in range(0,n):
            for j in range(i,n+1):
                listt = nums[i:j]
                uniq = len(set(listt))
                summ_ans+=(uniq*uniq)

        return summ_ans
