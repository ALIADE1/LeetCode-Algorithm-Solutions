class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        cou = Counter(nums)
        sorted_cou = sorted(cou.items(), key=lambda x : x[1])

        return sorted_cou[-1][0]
