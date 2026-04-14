class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0

        for i, val in enumerate(nums):
            if bin(i).count('1') == k:
                ans+=val

        return ans
