class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = str(x)
        summ = 0

        for c in s:
            summ+=int(c)

        return summ if x % summ == 0 else -1
