class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        summ_ans = 0
        i, j = 0, 0

        for com in commands :
            if com == "RIGHT":
                j+=1
                summ_ans=((i * n) + j)
            elif com == "LEFT":
                j-=1
                summ_ans=((i * n) + j)
            elif com == "UP":
                i-=1
                summ_ans=((i * n) + j)
            else:
                i+=1
                summ_ans=((i * n) + j)
            # print(summ_ans)

        return summ_ans
