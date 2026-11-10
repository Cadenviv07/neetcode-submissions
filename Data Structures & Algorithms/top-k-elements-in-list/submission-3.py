class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for key in freq:
            buckets[freq[key]].append(key)
        count = len(nums) - 1
        result = []
        while k > 0:
            if buckets[count] != []:
                for num in buckets[count]:
                    result.append(num)
                    k -= 1 
                    if ( k == 0):
                        break
            count -= 1

        return result

        