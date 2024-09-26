class DoublyLinkedListNode(object):
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory(object):

    def __init__(self, homepage):
        self.head = DoublyLinkedListNode(homepage)
        self.curPage = self.head
        
        
    def visit(self, url):
        node = DoublyLinkedListNode(url,self.curPage, None)
        self.curPage.next = node
        self.curPage = node
        

    def back(self, steps):
        node = self.curPage
        i = 0
        while node and i < steps:
            if node.prev == None:
                break
            node = node.prev
            i += 1
            
        
        self.curPage = node
        return node.val
        

    def forward(self, steps):
        node = self.curPage
        
        i = 0
        while node and i < steps:
            if node.next == None or i == steps:
                break
            node = node.next
            i+= 1
           
        
        self.curPage = node
        return node.val
        
