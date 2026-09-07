class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rset = defaultdict(set)
        cset = defaultdict(set)
        bset = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                n = board[r][c]
                if n == '.':
                    continue
                if n in rset[r] or n in cset[c] or n in bset[(r//3,c//3)]:
                    return False
                rset[r].add(n)
                cset[c].add(n)
                bset[(r//3,c//3)].add(n)

        return True