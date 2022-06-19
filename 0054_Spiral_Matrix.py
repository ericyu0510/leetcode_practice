class Solution:
    '''
    Time: O(mn)
    Space: O(1)
    '''
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        l, r, u, d = 0, len(matrix[0])-1, 0, len(matrix)-1
        row, col = 0, 0
        direction = 0 # 0:right, 1, down, 2, left, 3: up
        count = 0
        while(count < len(matrix[0])*len(matrix)):
            ans.append(matrix[row][col])
            if(direction == 0):
                if col < r:
                    col += 1
                else:
                    row += 1
                    direction = 1
                    u += 1
            elif(direction == 1):
                if row < d:
                    row+=1
                else:
                    col -= 1
                    direction = 2
                    r -= 1
            elif(direction == 2):
                if col > l:
                    col -= 1
                else:
                    row -= 1
                    direction = 3
                    d -= 1
            else:
                if row > u:
                    row -= 1
                else:
                    col += 1
                    direction = 0
                    l += 1
            count += 1
        return ans