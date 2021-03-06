from __future__ import print_function
import math


class Surround(object):
    def __init__(self):
        pass

    def printboard(self, board):
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                print(board[i][j], end='')
            print('')
        print('')

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if len(board) == 0 or len(board[0]) == 0:
            return None

        # Replace all 'O' at boundary to 'A'
        # Note the board might not be square
        for i in [0, len(board) - 1]:
            for j in range(0, len(board[0])):
                if board[i][j] == 'O':
                    board = self.replace(board, i, j, 'A')
        for i in [0, len(board[0]) - 1]:
            for j in range(0, len(board)):
                if board[j][i] == 'O':
                    board = self.replace(board, j, i, 'A')

        self.printboard(board)
        changed = True
        while changed:
            changed = False
            for depth in range(1, int(math.floor((len(board) + 1) / 2))):  # propagate toward the center
                for i in [0 + depth, len(board) - 1 - depth]:  # two horizontal edges
                    for j in range(0 + depth, len(board[0]) - depth):
                        print(depth, i, j)
                        if board[i][j] == 'O' and self.isalive(board, i, j):
                            board = self.replace(board, i, j, 'A')
                            changed = True
                            self.printboard(board)
                for i in [0 + depth, len(board[0]) - 1 - depth]:  # two vertical edges
                    for j in range(0 + depth, len(board) - depth):
                        if board[j][i] == 'O' and self.isalive(board, j, i):
                            board = self.replace(board, j, i, 'A')
                            changed = True
                            self.printboard(board)
        self.printboard(board)
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == 'O':
                    board = self.replace(board, i, j, 'X')
                elif board[i][j] == 'A':
                    board = self.replace(board, i, j, 'O')
        return board

    def isalive(self, board, i, j):
        if board[i+1][j] == 'A' or board[i-1][j] == 'A' or board[i][j+1] == 'A' or board[i][j-1] == 'A':
            return True
        else:
            return False

    def replace(self, board, i, j, newchar):
        list1 = list(board[i])
        list1[j] = newchar
        board[i] = ''.join(list1)
        return board


def main():
    board = ['XXXOXX', 'XOXXOO', 'OOXOXX', 'XOXOXX', 'XXOXXX', 'OXOXOX']
    # board = ['OOXXXXO', 'OXOOXXX', 'OXXOOOO', 'XOXOOXX', 'OXOXOXO', 'XOOXXOX', 'XXXOXOX']
    # board = ['OOXXXXO', 'OXOOXXX', 'OXXOOOO', 'XOXOOXX', 'OXOXOXO', 'XOOXXOX', 'XXXOXOX', 'XXXOXOX']
    test = Surround()
    test.printboard(board)
    board = test.solve(board)
    test.printboard(board)

main()