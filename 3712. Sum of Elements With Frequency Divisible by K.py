class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        cou = Counter(nums)
        summ = 0

        for x, y in cou.items():
            if y % k == 0:
                summ+=(x*y)

        return summ
