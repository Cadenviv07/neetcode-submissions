class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        count = 0
        for num in nums:
            numbers[num] = count
            count += 1

        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in numbers and i != numbers[temp]:
                return [i,numbers[temp]]

