class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)

        row_index = -1

        while l <= r:
            m = (l + r) // 2

            if m < 0 or m >= len(matrix):
                break

            row_min = matrix[m][0]
            row_max = matrix[m][-1]

            if row_min == target or row_max == target:
                return True
            if row_min < target < row_max:
                row_index = m
                break
            elif row_min > target:
                r = m-1
            elif row_max < target:
                l = m+1
        
        if row_index == -1:
            return False
        
        row = matrix[row_index]
        l = 0
        r = len(row)

        while l <= r:
            m = (l + r) // 2
            if row[m] == target:
                return True
            elif row[m] < target:
                l = m+1
            elif row[m] > target:
                r = m-1
        
        return False
        