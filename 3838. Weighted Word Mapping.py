class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ""
        for i in words:
            summ = 0
            for j in i:
                summ += weights[ord(j) - 97]
            summod = summ % 26
            ans+=chr(ord('z') - summod)
        return ans
