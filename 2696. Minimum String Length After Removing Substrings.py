class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for x in s:
            if not stack:
                stack.append(x)
            elif x == "B" and stack[-1] == "A":
                stack.pop()
            elif x == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(x)

        return len(stack)
