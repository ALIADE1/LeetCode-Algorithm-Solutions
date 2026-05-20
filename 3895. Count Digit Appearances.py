class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        cou_ans = 0

        for x in nums:
            cou_ans+=str(x).count(str(digit))

        return cou_ans
