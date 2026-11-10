class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        
        # Helper function to find the K-th smallest element
        # i and j are the starting pointers for nums1 and nums2
        def get_kth(i, j, k):
            
            # BASE CASES
            
            # If nums1 is exhausted, the answer must be in nums2
            if i >= len(nums1):
                return nums2[j + k - 1]
            
            # If nums2 is exhausted, the answer must be in nums1
            if j >= len(nums2):
                return nums1[i + k - 1]
            
            # If we are looking for the 1st smallest (k=1), 
            # we just take the smaller of the two starts
            if k == 1:
                return min(nums1[i], nums2[j])
            
            # RECURSIVE STEP
            
            # Check half of k (use integer division)
            p = k // 2
            
            # Get the value at the "halfway check" index.
            # If the index is out of bounds, use Infinity.
            # This handles the case where one array is shorter than k//2.
            mid_val1 = nums1[i + p - 1] if (i + p - 1) < len(nums1) else float('inf')
            mid_val2 = nums2[j + p - 1] if (j + p - 1) < len(nums2) else float('inf')
            
            # Compare and Discard
            if mid_val1 < mid_val2:
                # nums1's chunk is smaller. Discard it.
                # Move 'i' forward by 'p'. Decrease 'k' by 'p'.
                return get_kth(i + p, j, k - p)
            else:
                # nums2's chunk is smaller. Discard it.
                # Move 'j' forward by 'p'. Decrease 'k' by 'p'.
                return get_kth(i, j + p, k - p)
        
        # MAIN LOGIC
        
        # If odd, find the middle element
        if total_len % 2 == 1:
            return get_kth(0, 0, total_len // 2 + 1)
        # If even, average the two middle elements
        else:
            left_mid = get_kth(0, 0, total_len // 2)
            right_mid = get_kth(0, 0, total_len // 2 + 1)
            return (left_mid + right_mid) / 2