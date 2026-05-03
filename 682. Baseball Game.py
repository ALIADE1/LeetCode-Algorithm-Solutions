class Solution:
    def calPoints(self, operations: List[str]) -> int:
        values = []

        for x in operations:
            if x == 'D':
                values.append(values[-1] * 2)
            elif x == 'C':
                values.pop()
            elif x == '+':
                values.append(values[-1] + values[-2])
            else:
                values.append(int(x))

        return sum(values)
