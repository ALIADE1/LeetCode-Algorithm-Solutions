class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        nums_r = nums[::-1]

        return nums + nums_r
