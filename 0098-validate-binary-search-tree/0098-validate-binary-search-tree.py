class Solution(object):
    def isValidBST(self, root):
        def helper(node, left, right):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            # Recursively check the left and right subtree
            return (helper(node.left, left, node.val) and helper(node.right, node.val, right))
        
        # Initial call with root and infinity bounds
        return helper(root, float('-inf'), float('inf'))
