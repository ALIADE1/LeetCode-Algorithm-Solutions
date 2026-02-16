class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)

        for x in range(n):
            dig = str(nums[x])[::-1]
            nums.append(int(dig))

        return len(set(nums))
