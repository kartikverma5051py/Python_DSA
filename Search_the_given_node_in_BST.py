class BST:
    def __init__(self,key):
        self.left = None
        self.right =None
        self.key = key
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key==data:
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

    def search(self,data):
        if self.key==data:
            print("Node is found")
            return
        if self.key>data:
            if self.left:
                self.left.search(data)
            else:
                print("Node is not present")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("Node is not present")

    def preorder(self):
        # lst = []
        # lst.append(self.key)
        print(self.key,end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
        # return lst
if __name__ == '__main__':
    root = BST(100)
    lst = [1,2,3,4,1000,2,312,3243,54]
    for i in lst:
        root.insert(i)
    root.search(2)
    print(root.preorder())
lst = [1,2]
print(lst.pop(0))