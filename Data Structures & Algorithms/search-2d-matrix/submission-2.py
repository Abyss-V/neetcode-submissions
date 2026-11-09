class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i,row in enumerate(matrix):
            l = 0
            r = len(matrix[i]) - 1
            while l <= r:
                middle = (l+r)//2
                if matrix[i][middle] == target:
                    return True
                elif matrix[i][middle] < target:
                    l += 1
                else:
                    r -= 1
        return False

# solution with complexity: time:o(log(m*n)) , space:o(1)

