class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dis_val = []

        for x in arr:
            if arr.count(x) == 1:
                dis_val.append(x)

        return dis_val[k-1] if k <= len(dis_val) else ""
