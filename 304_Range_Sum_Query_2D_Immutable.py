class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            for c in range(1, n):
                matrix[r][c] = matrix[r][c-1] + matrix[r][c]
        for c in range(n):
            for r in range(1, m):
                matrix[r][c] = matrix[r-1][c] + matrix[r][c]
        self.ps_matrix = matrix
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = self.ps_matrix[row2][col2]
        if(row1 > 0):
            sum -= self.ps_matrix[row1-1][col2]
        if(col1 > 0):
            sum -= self.ps_matrix[row2][col1-1]
        if(row1 > 0 and col1 > 0):
            sum += self.ps_matrix[row1-1][col1-1]
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)