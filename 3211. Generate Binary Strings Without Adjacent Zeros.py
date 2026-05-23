class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = ['0', '1']
        if n == 1:
            return ans

        for i in range(n-1):
            update_ans = []

            for val in ans:
                if val[-1] == '1':
                    update_ans.append(val+'0')
                    update_ans.append(val+'1')
                else:
                    update_ans.append(val+'1')
            ans = update_ans

        return ans
