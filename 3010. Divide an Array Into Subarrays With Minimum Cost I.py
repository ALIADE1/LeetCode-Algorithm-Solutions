class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a, b = 51, 51
        for x in range(1,len(nums)):
            if nums[x] < a:
                b = a
                a = nums[x]
            elif nums[x] < b:
                b = nums[x]

        return nums[0] + a + b
