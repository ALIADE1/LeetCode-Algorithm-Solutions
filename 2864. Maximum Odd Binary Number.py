class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c_1 = s.count('1')
        c_0 = s.count('0')

        return '1' * (c_1-1) + '0' *(c_0) + '1'
