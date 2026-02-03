class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = list(accumulate(height, max))
        right_max = list(accumulate(reversed(height), max))[::-1]

        return sum(min(l,r) - h for l, r, h in zip(left_max, right_max, height))
