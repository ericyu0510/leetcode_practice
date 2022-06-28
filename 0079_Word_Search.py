class Solution:
    '''
    Time: O(m*n*3^k), where k is length of word and m and n are sizes of our board
    Space: O(k)
    '''
    def exist(self, board, word: str) -> bool:
        self.board = board
        self.word = word
        self.found = False
        start = []
        self.m, self.n = len(self.board), len(self.board[0])
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == word[0]:
                    start.append((i, j))
        
        for row, col in start:
            if self.found:
                return True
            self.search(0, row, col)
        return self.found
    
    def search(self, index, row, col):
        if self.found:
            return
        if self.board[row][col] == self.word[index]:
            if index == len(self.word)-1:
                self.found = True
                return
            tmp = self.board[row][col]
            self.board[row][col] = '#'
            if row > 0:
                self.search(index+1, row-1, col)
            if row < self.m -1:
                self.search(index+1, row+1, col)
            if col > 0:
                self.search(index+1, row, col-1)
            if col < self.n-1:
                self.search(index+1, row, col+1)
            
            self.board[row][col] = tmp
            
        return
        