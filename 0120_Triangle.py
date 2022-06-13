class Solution:
    '''
    Top down approach
    '''
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     for row in range(1, len(triangle)): # row index
    #         for i in range(len(triangle[row])):
    #             if(i == 0):
    #                 triangle[row][i] = triangle[row-1][i] + triangle[row][i]
    #             elif(i == len(triangle[row])-1):
    #                 triangle[row][i] = triangle[row-1][i-1] + triangle[row][i]
    #             else:
    #                 triangle[row][i] = min(triangle[row-1][i-1], triangle[row-1][i]) + triangle[row][i]
    #     return min(triangle[-1])
    '''
    Button up
    '''
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
		
        for i in range(n-1, 0, -1):
            for j in range(0, len(triangle[i])-1):
                triangle[i-1][j] += min(triangle[i][j], triangle[i][j+1])
        
        return triangle[0][0]