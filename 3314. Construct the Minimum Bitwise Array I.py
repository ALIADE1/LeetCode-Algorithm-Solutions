class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for x in nums:
            b = 1
            for i in range(x):
                if i | (i+1) == x:
                    ans.append(i)
                    b = 0
                    break
            if b:
                ans.append(-1)

        return ans
