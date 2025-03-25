from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root):
      self.root = Node(root)

    def addToTree(self,value):
        if self.root is None:
          self.root = Node(value)
        else:
          q = deque()
          q.append(self.root)

          while q:
            temp = q.popleft()

            if temp.left is None:
              temp.left = Node(value)
              break
            else:
              q.append(temp.left)

            if temp.right is None:
              temp.right = Node(value)
              break
            else:
              q.append(temp.right)

    def inOrderTraversal(self,root):
      if root:
        self.inOrderTraversal(root.left)
        print(root.data)
        self.inOrderTraversal(root.right)

    def preOrderTraversal(self,root):
      if root:
        print(root.data)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)

    def postOrderTraversal(self,root):
      if root:
        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        print(root.data)