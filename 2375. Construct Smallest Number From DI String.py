class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = ""
        stack = []
        i = 1

        for x in pattern:
            stack.append(str(i))
            i+=1
            if x == 'I':
                while stack:
                    val = stack.pop()
                    ans+=str(val)
                    
        stack.append(str(i))            
        while stack:
            val = stack.pop()
            ans+=str(val)
        return ans
