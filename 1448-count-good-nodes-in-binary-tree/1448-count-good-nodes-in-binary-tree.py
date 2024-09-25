class Solution(object):
    def goodNodes(self, root):
        def helper(root, curMax):
            if not root:
                return 0
            
            amoutLeft = helper(root.left, max(root.val,curMax))
            amountRight = helper(root.right, max(root.val,curMax))
            
            if root.val >= curMax:
                return 1 + amoutLeft + amountRight
            else:
                return amoutLeft + amountRight
        return helper(root, root.val)
           