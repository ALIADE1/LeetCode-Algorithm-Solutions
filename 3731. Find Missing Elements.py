class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maxx, minn = max(nums), min(nums)
        ans = []

        for x in range(minn, maxx):
            if x not in nums:
                ans.append(x)
        
        return ans
