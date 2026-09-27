class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        dsum = 0
        for i in range(len(mat)):
            dsum += mat[i][i] + mat[i][len(mat) - 1 - i]
        if len(mat) % 2 == 1:
            mid = len(mat) // 2
            dsum -= mat[mid][mid]
        return dsum

        # (0,3) + (1,2) + (2, 1)