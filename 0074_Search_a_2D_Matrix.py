class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix)-1, len(matrix[0])-1
        st, en = 0, m
        while(st <= en):
            mid = (st+en) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                en = mid - 1
            else:
                st = mid + 1
        if st > en:
            return False
        
        st, en = 0, n
        while(st <= en):
            mid = (st+en) // 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                en = mid -1
            else:
                st = mid + 1
        return False
            
            