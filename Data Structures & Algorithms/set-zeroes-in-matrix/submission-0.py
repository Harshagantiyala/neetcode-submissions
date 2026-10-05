class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        indexes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    indexes.append((i, j))
        for i in range(len(indexes)):
            row, col = indexes[i]
            for j in range(len(matrix[row])):
                matrix[row][j] = 0
            for i in range(len(matrix)):
                matrix[i][col] = 0        