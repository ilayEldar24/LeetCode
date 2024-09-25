class Solution(object):
    def kthSmallest(self, root, k):
        self.counter = 0  # Use instance variables instead of class variables
        self.number = -1

        def inOrder(root, k):
            if not root:
                return
            inOrder(root.left, k)
            self.counter += 1
            if self.counter == k:
                self.number = root.val
                return
            inOrder(root.right, k)

        inOrder(root, k)
        return self.number
