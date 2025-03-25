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
