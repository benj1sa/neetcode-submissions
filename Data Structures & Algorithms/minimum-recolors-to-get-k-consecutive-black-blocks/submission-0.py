class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_ops = float('inf')
        for start_idx in range(len(blocks) - k + 1):
            ops = 0
            for i in range(start_idx, start_idx + k):
                if blocks[i] == "W":
                    ops += 1
            min_ops = min(min_ops, ops)
        return min_ops