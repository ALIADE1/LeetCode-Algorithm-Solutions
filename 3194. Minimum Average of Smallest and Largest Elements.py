class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        i, j = 0, -1
        n = int(len(nums) / 2)
        averages = []
        nums.sort()

        for x in range(n):
            minElement, maxElement = nums[i], nums[j]
            averages.append((minElement + maxElement) / 2)
            i+=1
            j-=1

        return min(averages)
