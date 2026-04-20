class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []

        for x in image:
            x = x[::-1]
            vals = []
            for v in x:
                vals.append(v^1)
            ans.append(vals)

        return ans
