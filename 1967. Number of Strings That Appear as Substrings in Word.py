class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cou_ans = 0

        for c in patterns:
            if c in word:
                cou_ans+=1

        return cou_ans
