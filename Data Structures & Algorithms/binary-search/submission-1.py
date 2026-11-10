class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        return self.bsa(start,end,target, nums)

    def bsa(self,start,end, target, nums):
        if start > end:
                return -1
            
        middle = (start + end)//2

        if nums[middle] == target:
            return middle
        elif target < nums[middle]:
            end = middle - 1
            return self.bsa(start, end, target,nums)
        else:
            start = middle + 1 
            return self.bsa(start, end, target,nums)
            