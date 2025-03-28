class BinaryTree:

    def __init__(self, rootID):

        self.rootID = rootID
        self.left = None
        self.right = None

    def insertLeft(self, newNode):

        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):

        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

def printTreePre(tree):

    if tree != None:
        print(tree.rootID)
        printTreePre(tree.left)
        printTreePre(tree.right)


bTree: BinaryTree = BinaryTree("A")
bTree.insertRight(BinaryTree("B"))
bTree.insertLeft(BinaryTree("C"))
bTree.insertRight(BinaryTree("D"))

printTreePre(bTree)


