class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s = str(num)
        n = len(s)

        return False if s[-1] == '0' and n > 1 else True
