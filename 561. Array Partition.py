class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        summ_ans = 0

        for x in range(0,n,2):
            summ_ans+=nums[x]

        return summ_ans
