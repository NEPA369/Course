# 3. Implement DFS for value retrieval from tree in python.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 
class DFSTraversal:
    @staticmethod
    def preorder(node):
        if not node:
            return []
        return [node.value] + DFSTraversal.preorder(node.left) + DFSTraversal.preorder(node.right)

    @staticmethod
    def inorder(node):
        if not node:
            return []
        return DFSTraversal.inorder(node.left) + [node.value] + DFSTraversal.inorder(node.right)

    @staticmethod
    def postorder(node):
        if not node:
            return []
        return DFSTraversal.postorder(node.left) + DFSTraversal.postorder(node.right) + [node.value]


if __name__ == "__main__":
    root = TreeNode("A")
    root.left = TreeNode("B")
    root.right = TreeNode("C")
    root.left.left = TreeNode("D")

    print("DFS Preorder:", DFSTraversal.preorder(root))
    print("DFS Inorder:", DFSTraversal.inorder(root))
    print("DFS Postorder:", DFSTraversal.postorder(root))
