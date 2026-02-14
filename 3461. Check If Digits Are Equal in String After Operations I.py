class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            n = len(s)
            n_s = ""

            for x in range(n-1):
                n_s+= str((int(s[x]) + int(s[x+1])) % 10)

            s = n_s

        return s[0] == s[1]
