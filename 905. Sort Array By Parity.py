class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums_odd = []
        nums_even = []

        for x in nums:
            if x%2==0:
                nums_even.append(x)
            else:
                nums_odd.append(x)

        return nums_even + nums_odd
