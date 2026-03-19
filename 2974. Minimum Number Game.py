class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        arr = []

        for x in range(0, n-1, 2):
            arr.append(nums[x+1])
            arr.append(nums[x])

        return arr
