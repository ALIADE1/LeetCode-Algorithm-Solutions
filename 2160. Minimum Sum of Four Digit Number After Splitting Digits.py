class Solution:
    def minimumSum(self, num: int) -> int:
        s = sorted(str(num))
        new1 = int(s[0] + s[2]) 
        new2 = int(s[1] + s[3]) 

        return new1 + new2
