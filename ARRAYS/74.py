class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        isThere=False
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y]==target:
                    isThere=True
                    break
        return isThere