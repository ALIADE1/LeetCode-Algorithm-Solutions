class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        char_val, num_val = coordinates[0], coordinates[1]
        indx = ord(char_val) - ord('a')

        if int(num_val) % 2 == 0:
            return indx % 2 == 0
        else:
            return indx % 2 != 0
