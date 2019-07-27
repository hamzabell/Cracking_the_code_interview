class Node: 
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree: 
    def __init__(self, root):
        self.root = root


    def insert(self, node, nodeToBeInserted):
        if (node.value > nodeToBeInserted.value):
            if (node.left == None):
                nodeToBeInserted.parent = node
                node.left = nodeToBeInserted
                return True
            return self.insert(node.left, nodeToBeInserted)
        else:
            if (node.right == None):
                nodeToBeInserted.parent = node
                node.right = nodeToBeInserted
                return True
            return self.insert(node.right, nodeToBeInserted)
        
            

root = Node(12)
newNode = Node(3)
gtaNode = Node(15)
gtestNode = Node(20)
nextNode = Node(90)
nextestNode = Node(25)
bst = BinarySearchTree(root)
bst.insert(root, newNode)
bst.insert(root, gtaNode)
bst.insert(root, gtestNode)
bst.insert(root, nextNode)
bst.insert(root, nextestNode)



print(root.left.value)
print(root.right.value)
print(gtaNode.right.value)
print(gtestNode.right.value)
print(nextNode.left.value)

        


