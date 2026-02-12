class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxx, summ = max(nums), 0

        for x in nums:
            summ += (maxx - x)

        return summ
