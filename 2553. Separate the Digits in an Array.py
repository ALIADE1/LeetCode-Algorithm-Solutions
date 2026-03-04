class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []

        for x in nums:
            for c in str(x):
                ans.append(int(c))

        return ans
