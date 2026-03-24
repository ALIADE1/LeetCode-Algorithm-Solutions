class Solution:
    def mergeArrays(self, num1: List[List[int]], num2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        n1, n2 = len(num1), len(num2)
        ans = []

        while i < n1 and j < n2:
            if num1[i][0] == num2[j][0]:
                ans.append([num1[i][0], num1[i][1] + num2[j][1]])
                i+=1
                j+=1
            elif num1[i][0] < num2[j][0]:
                ans.append(num1[i])
                i+=1
            else:
                ans.append(num2[j])
                j+=1

        ans.extend(num1[i:])
        ans.extend(num2[j:])

        return ans
