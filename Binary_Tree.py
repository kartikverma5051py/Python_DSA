class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild =None

def height(node):
    if node is None:
        return 0
    return 1+max(height(node.lchild),height(node.rchild))
def diameter(root):
    if root is None:
        return 0
    lheight = height((root.lchild))
    rheight = height(root.rchild)


    ldiameter = diameter(root.lchild)
    rdiameter = diameter(root.rchild)

    return  max(lheight+rheight+1,max(ldiameter,rdiameter))
if __name__ == '__main__':
    root = BST(1)
    root.lchild = BST(2)
    root.rchild=BST(3)
    root.lchild.lchild = BST(4)
    root.lchild.rchild = BST(5)
    print(diameter(root))
a = 100
b = 5
print(a//b*a/b)