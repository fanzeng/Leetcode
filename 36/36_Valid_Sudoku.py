class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.verifyRow(board) and self.verifyCol(board) and self.verifyBox(board)
        
    def verify(self, arr):
        print arr
        count = [0]*9
        for a in arr:
            if a == ".":
                continue
            n = int(a)
            if count[n-1] > 0:
                return False
            else:
                count[n-1] = 1
        return True

    def verifyRow(self, board):
        for row in board:
            if not self.verify(row):
                return False
        return True
    
    def verifyCol(self, board):
        for i in range(9):
            if not self.verify([row[i] for row in board]):
                return False
        return True

    def verifyBox(self, board):
        for i in range(3):
            for j in range(3):
                x = 3*i + 1
                y = 3*j + 1
                if not self.verify([board[k][l] for (k, l) in self.getBox(x, y)]):
                    return False
        return True
    
    def getBox(self, x, y):
        return [
            (x-1, y-1), (x-1, y), (x-1, y+1),
            (x, y-1), (x, y), (x, y+1),
            (x+1, y-1), (x+1, y), (x+1, y+1)
        ]
