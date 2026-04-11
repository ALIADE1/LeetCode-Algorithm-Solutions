class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans, cou = [], 0

        for x in s:
            if x == '(' and cou > 0:
                ans.append(x)
            if x == ')' and cou > 1:
                ans.append(x)

            if x == '(': 
                cou+=1 
            else: 
                cou-=1
                
        return "".join(ans)
