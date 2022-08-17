class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(bool)
        col_dict = defaultdict(bool)
        box_dict = defaultdict(bool)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if row_dict[(i, board[i][j])] == True:
                    return False
                else:
                    row_dict[(i, board[i][j])] = True
                if col_dict[(j, board[i][j])] == True:
                    return False
                else:
                    col_dict[(j, board[i][j])] = True
                if box_dict[(i//3, j//3, board[i][j])] == True:
                    return False
                else:
                    box_dict[(i//3, j//3, board[i][j])] = True
        return True