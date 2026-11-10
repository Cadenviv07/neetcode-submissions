class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            
            leftH = dfs(node.left)
            if leftH == -1:
                return -1
            
            
            rightH = dfs(node.right) 
            if rightH == -1:
                return -1

            
            if abs(leftH - rightH) > 1:
                return -1
            
            
            return max(leftH, rightH) + 1
        
        return dfs(root) != -1