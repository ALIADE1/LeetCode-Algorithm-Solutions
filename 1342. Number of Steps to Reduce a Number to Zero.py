class Solution:
    def numberOfSteps(self, num: int) -> int:
        ans_cou = 0

        while num > 0:
            if num % 2 == 0:
                num/=2
                ans_cou+=1
            else:
                num-=1
                ans_cou+=1

        return ans_cou
