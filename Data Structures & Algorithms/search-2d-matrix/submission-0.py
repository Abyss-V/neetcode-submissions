class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_m = 0
        right_m = len(matrix) - 1
        while left_m <= right_m:
            middle_m = (left_m + right_m) // 2
            if matrix[middle_m][0] > target:
                right_m = middle_m - 1
            elif matrix[middle_m][-1] < target:
                left_m = middle_m + 1
            elif matrix[middle_m][0] <= target and matrix[middle_m][-1] >= target:
                m = matrix[middle_m]
                left = 0
                right = len(m) - 1
                while left <= right:
                    middle = (left + right) // 2
                    if m[middle] == target:
                        return True
                    elif m[middle] < target:
                        left = middle + 1
                    elif m[middle] > target:
                        right = middle - 1
                return False
        return False
    
# time: O(m log n) , space :O(1)