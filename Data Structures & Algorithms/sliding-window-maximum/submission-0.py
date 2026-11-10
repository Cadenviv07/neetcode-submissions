from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        results = []

        for i, curr_val in enumerate(nums):
            while q and curr_val > nums[q[-1]]:
                q.pop()
            
            q.append(i)

            if i - k  + 1 > q[0]:
                q.popleft()

            if i >= k - 1:
                results.append(nums[q[0]])
            
        return results
