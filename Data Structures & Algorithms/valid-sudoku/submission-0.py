class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rset = defaultdict(set)
        cset = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                n = board[r][c]
                if n == '.':
                    continue
                if n in rset[r] or n in cset[c]:
                    return False
                rset[r].add(n)
                cset[c].add(n)

        for top in range(0, 6, 3):
            for left in range(0, 6, 3):
                boxset = set()
                for r in range(top, top+3):
                    for c in range(left, left+3):
                        if board[r][c] == '.':
                            continue
                        if board[r][c] in boxset:
                            return False
                        boxset.add(board[r][c])

        return True