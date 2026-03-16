class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        cou = 0

        for i in range(1,n):
            l, r = nums[0:i], nums[i:n]
            if abs(sum(l) - sum(r)) % 2 == 0:
                cou+=1

        return cou
