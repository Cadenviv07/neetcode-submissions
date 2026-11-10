class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False # Added colon

        rows = len(matrix)
        cols = len(matrix[0])

        # --- LOOP 1: Find the correct ROW ---
        start = 0
        end = rows - 1
        target_row_index = -1  # We need to save the row we find here

        while start <= end:
            middle = (start + end) // 2
            
            # Look at the values at the start/end of this row
            row_start_val = matrix[middle][0]
            row_end_val = matrix[middle][-1]

            if target < row_start_val:
                # Target is smaller than this row's start -> Go Up
                end = middle - 1
            elif target > row_end_val:
                # Target is bigger than this row's end -> Go Down
                start = middle + 1
            else:
                # Target is INSIDE this row! Save it and break.
                target_row_index = middle
                break 
        
        # If we didn't find a valid row, stop early
        if target_row_index == -1:
            return False

        # --- LOOP 2: Find the target inside that ROW ---
        start = 0
        end = cols - 1
        
        # Grab the actual row list to make it easier to read
        actual_row = matrix[target_row_index]

        while start <= end:
            middle = (start + end) // 2
            
            # Check the VALUE, not the index
            val = actual_row[middle]

            if val == target: # Added colon
                return True
            
            if target < val:
                end = middle - 1
            else: # Changed from 'if target > middle' to 'else' for efficiency
                start = middle + 1
        
        return False