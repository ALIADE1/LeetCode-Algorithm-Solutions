class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cou = Counter(nums)
        ans = []

        sort_items = sorted(cou.items(), key = lambda x:(x[1],-x[0]))

        for x, y in sort_items:
            for _ in range(y):
                ans.append(x)

        return ans
