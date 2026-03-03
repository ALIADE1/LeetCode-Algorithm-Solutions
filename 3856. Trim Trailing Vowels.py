class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vow = ['a', 'e', 'i', 'o', 'u']
        x = len(s) - 1

        while x >= 0 and s[x] in vow:
            x-=1

        return s[:x+1]
