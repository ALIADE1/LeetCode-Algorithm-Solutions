class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_stnd = heights[:]
        heights.sort()
        ans_cou = 0

        for x in range(len(heights)):
            if heights_stnd[x] != heights[x]:
                ans_cou+=1

        return ans_cou
