# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        node = root

        output = []

        total = 0

        q = deque()
        q.append(node)

        while q:
            size = len(q)
            sub = []

            for _ in range (size):
                node = q.popleft()
                sub.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            output.append(sub)
        return output



