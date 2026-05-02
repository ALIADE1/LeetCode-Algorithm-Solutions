class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans_sum = 0

        for i in range(1, n):
            if nums[i-1] < nums[i]:
                continue
            else:
                ans_sum += abs(nums[i] - nums[i-1]) + 1
                nums[i] = max(nums[i], 1 + nums[i-1])
            
        return ans_sum
