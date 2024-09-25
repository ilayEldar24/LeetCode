class Solution(object):
    def rightSideView(self, root):
        
        res = []
        q = deque()
        q.append(root)
        res = []

        while q:
            level = []
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if level:
                res.append(level.pop())

        return res

    