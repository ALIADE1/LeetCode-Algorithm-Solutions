class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans_summ = sum(arr)
        n = len(arr)
        c = 3

        for _ in range(n):
            for i in range(n):
                if i+c > n:
                    continue
                else:
                    ans_summ+=sum(arr[i:i+c])

            c+=2

        return ans_summ
