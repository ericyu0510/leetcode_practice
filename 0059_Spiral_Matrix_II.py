class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [ [0]*n for i in range(n)]
        count = 1
        for i in range(n // 2):
            for c in range(i, n-i):
                mat[i][c] = count
                count += 1
            for r in range(i+1, n-i):
                mat[r][n-i-1] = count
                count += 1
            for c in range(n-i-2, i-1, -1):
                mat[n-1-i][c] = count
                count += 1
            for r in range(n-2-i, i, -1):
                mat[r][i] = count
                count += 1
        if n%2==1:
            mat[n//2][n//2] = count
            
        return mat
        