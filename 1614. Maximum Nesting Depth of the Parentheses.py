class Solution:
    def maxDepth(self, s: str) -> int:
        c, maxx = 0, 0

        for i in s:
            if i == "(":
                c+=1
                if maxx < c:
                    maxx = c
            elif i == ")":
                c-=1
        
        return maxx
