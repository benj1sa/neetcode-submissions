"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # define p's lineage
        c = p
        ancestors = set()
        while c:
            ancestors.add(c.val)
            c = c.parent
        c = q
        while c:
            if c.val in ancestors:
                return c
            c = c.parent
        return None