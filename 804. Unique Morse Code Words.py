class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ans = []
        rep = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
        "--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        for x in words:
            stt = ""
            for ch in x:
                stt+=rep[ord(ch) - ord('a')]
            ans.append(stt)

        return len(set(ans))
