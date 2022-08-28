class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        l = [[] for _ in range(m+n-1)]
        for i in range(m):
            for j in range(n):
                l[i-j+(n-1)].append(mat[i][j])
        for li in l:
            li.sort()
        for i in range(m):
            for j in range(n):
                mat[i][j] = l[i-j+(n-1)].pop(0)
        return mat