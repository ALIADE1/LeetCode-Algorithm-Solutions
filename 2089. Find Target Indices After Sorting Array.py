class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        n = len(nums)
        ans = []

        for x in range(n):
            if nums[x] == target:
                ans.append(x)

        return ans
