class Solution:
    def isValidSudoku(self, board):
        
        # Check rows
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])

        # Check columns
        for j in range(9):
            s = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])

        # Check 3x3 boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                s = set()
                for i in range(3):
                    for j in range(3):
                        value = board[row + i][col + j]
                        if value == ".":
                            continue
                        if value in s:
                            return False
                        s.add(value)

        return True