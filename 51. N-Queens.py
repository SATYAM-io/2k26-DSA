from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["."*n]*n
        ans = []

        def canPut(r: int, c: int) -> bool:
            for i in range(r):
                if board[i][c] == 'Q':
                    return False

            i, j = r-1, c-1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            i, j = r-1, c+1
            while i >= 0 and j < len(board):
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def nQueen(n: int, r: int) -> bool:
            if r == n:
                print(board)
                ans.append(board[:])
                return False

            for i in range(n):
                cp = canPut(r, i)
                if cp:
                    board[r] = board[r][0:i] + 'Q' + board[r][i+1:n]
                    if nQueen(n, r+1):
                        return True
                    board[r] = board[r][0:i] + '.' + board[r][i+1:]

            return False

        nQueen(n, 0)
        return ans