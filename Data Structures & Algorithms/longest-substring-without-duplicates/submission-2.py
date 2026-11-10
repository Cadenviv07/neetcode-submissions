class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        unique = {}
        left = 0 
        right = 0
        length = 0

        for c in s:
            if c in unique:
                left = max(left, unique[c] + 1)
                unique[c] = right
            else:
                unique[c] = right

            length = max(length, right - left)
            right += 1

        return length + 1
    
        