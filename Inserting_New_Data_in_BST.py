class BST:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key>data:
            if self.left:
                self.left.insert(data)
            else:
                self.left =BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right= BST(data)
if __name__ == '__main__':
    root = BST(10)
    lst = [10,20,30,5,6,2]
    for i in lst:
        root.insert(i)