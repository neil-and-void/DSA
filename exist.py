from typing import *

def exist(board: List[List[str]], word: str) -> bool:
    # base cases
    def rec_exists(board, word, w_idx, i, j):
        if i < 0 or len(board) <= i or j < 0 or len(board[0]) <= j:
            return False
        elif board[i][j] == '!':
            return False
        elif w_idx == len(word) - 1 and word[w_idx] == board[i][j]:
            return True

        # recursive case
        elif board[i][j] == word[w_idx]:
            prev = board[i][j]
            board[i][j] = '!'
            u = rec_exists(board, word, w_idx + 1, i + 1, j)
            d = rec_exists(board, word, w_idx + 1, i - 1, j)
            l = rec_exists(board, word, w_idx + 1, i, j - 1)
            r = rec_exists(board, word, w_idx + 1, i, j + 1)
            board[i][j] = prev
            return u or d or l or r

    for i in range(len(board)):
        for j in range(len(board[0])):
            exists = rec_exists(board, word, 0, i, j)
            if exists:
                return True
    return False

b = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
w = "SEE"
ans = exist(b, w)
print(ans)
