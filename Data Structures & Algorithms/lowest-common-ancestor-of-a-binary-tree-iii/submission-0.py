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
        lineage = set()
        tmp = p
        while tmp:
            lineage.add(tmp.val)
            tmp = tmp.parent
        tmp = q
        while tmp:
            if tmp.val in lineage:
                return tmp
            tmp = tmp.parent
        return None