class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        for i in range(32):
            ones += (n >> i) & 1
        return ones