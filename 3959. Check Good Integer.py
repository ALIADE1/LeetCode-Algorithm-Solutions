class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitSum, squareSum = 0, 0

        for x in str(n):
            digitSum += int(x)
            squareSum += int(x)**2

        return squareSum - digitSum >= 50
