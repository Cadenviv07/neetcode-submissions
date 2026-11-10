class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1 
        end = sum(piles)
        result = end
        while start <= end:
            middle = (start + end)//2 

            hours = 0 
            for num in piles:
                hours += math.ceil(num/middle)
        
            if hours <= h:
                result = middle
                end = middle - 1 
            
            if hours > h:
                start = middle + 1

        return result


                
        