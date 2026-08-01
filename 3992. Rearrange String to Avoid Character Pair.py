class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        if x > y:
            return ''.join(sorted(s))
        else:
            return ''.join(sorted(s,reverse=True))
