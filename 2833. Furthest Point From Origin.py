class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l, r = moves.count('L'), moves.count('R')
        c_ = moves.count('_')

        if r >= l:
            return c_ + r - l
        else:
            return c_ + l - r
