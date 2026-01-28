class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for x in range(n):
            digit_sum = sum(int(d) for d in str(nums[x]))
            if digit_sum == x:
                return x

        return -1
