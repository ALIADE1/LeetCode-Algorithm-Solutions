class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        INF = float("inf")
        best = INF
        k = nums[0]

        if all(nums[i] == (k + i) % n for i in range(n)):
            m = (n - k) % n
            best = min(best, m, n - m + 2)

        if all(nums[i] == (k - i) % n for i in range(n)):
            j = nums.index(n - 1)
            best = min(best, 1 + j, 1 + (n - j) % n)

        return -1 if best == INF else best
