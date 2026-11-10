class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sC = [0]*26
        tC = [0]*26

        for i in range(len(s)):
            sC[ord(s[i]) - ord('a')] += 1
            tC[ord(t[i]) - ord('a')] += 1
        
        for i in range(26):
            if sC[i] != tC[i]:
                return False
        return True
     