class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        perm = []
        l, r = 0, len(s)

        for x in s:
            if x == 'I':
                perm.append(l)
                l+=1
            else:
                perm.append(r)
                r-=1
                
        perm.append(l)
        return perm
