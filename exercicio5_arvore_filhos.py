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

    def printChildren(self,value):
        q = deque()
        q.append(self.root)

        while q:
            temp = q.popleft()
            if temp.data == value:
                print(temp.left.data)
                print(temp.right.data)
                break
            else:
               q.append(temp.left)
               q.append(temp.right)

                
        

      
root = BinaryTree(50)
root.addToTree(30)
root.addToTree(70)
root.addToTree(20)
root.addToTree(40)
root.addToTree(60)
root.addToTree(80)
root.printChildren(70)

print("In Order Traversal \n")
root.inOrderTraversal(root.root)
print("\n")
print("Pre Order Traversal \n")
root.preOrderTraversal(root.root)
print("\n")
print("Post Order Traversal \n")
root.postOrderTraversal(root.root)
print("\n")