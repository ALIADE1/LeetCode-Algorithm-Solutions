class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        ss = ""
        for w in words:
            ss+=w[0]
        return ss == s 
