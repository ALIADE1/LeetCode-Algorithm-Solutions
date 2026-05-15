class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0

        for x in details:
            age = int(x[11:13])
            if age > 60:
                ans+=1

        return ans
