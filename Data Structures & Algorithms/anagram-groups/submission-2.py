class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for word in strs:
            freq_val = [0]*26
            for i in range(len(word)):
                freq_val[ord(word[i]) - ord('a')] += 1 
            t = tuple(freq_val)
            if t in freq:
                freq[t].append(word)
            else:
                freq[t] = [word] 

        result = []
        for key in freq:
            result.append(freq[key])
        
        return result


