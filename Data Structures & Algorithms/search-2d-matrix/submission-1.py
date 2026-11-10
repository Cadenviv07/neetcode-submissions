class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        
        start = 0
        end = (rows * cols) - 1
        
        while start <= end:
            mid_index = (start + end) // 2
            
            mid_element = matrix[mid_index // cols][mid_index % cols]
            
            if mid_element == target:
                return True
            elif target < mid_element:
                end = mid_index - 1
            else:
                start = mid_index + 1
                
        return False