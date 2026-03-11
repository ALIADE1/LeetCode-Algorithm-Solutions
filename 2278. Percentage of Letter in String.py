class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cou, n = s.count(letter), len(s)
        return int((cou/n*100))
