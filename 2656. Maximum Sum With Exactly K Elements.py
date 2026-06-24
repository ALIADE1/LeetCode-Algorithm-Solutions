class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxx = max(nums)
        ans = 0

        for i in range(k):
            ans+=(maxx + i)

        return ans
