class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.val = data

class Solution:
    def inorderTraversal(self, root):
        nodes = []
        def TraversalUtil(root):
            if not root:
                return
            
            # for child in root.children:
            #     TraversalUtil(child)
            
            if root.left:
                TraversalUtil(root.left)
                
            nodes.append(root.val)
                
            if root.right:
                TraversalUtil(root.right)
                
        TraversalUtil(root)
        return nodes

'''   Let us create below tree
*              5
*           //    \\
*          3        7
*        // \\    // \\
*        1   4    6   8
*           //
*          2
'''
arr = Node(5)
arr.left = Node(3)
arr.left.right = Node(4)
arr.left.left = Node(1)
arr.right = Node(7)
arr.right.right = Node(8)
arr.right.left = Node(6)
arr.left.right.left = Node(2)
obj = Solution()
ans = obj.inorderTraversal(arr)
print(ans)
'''
Output:
[1, 3, 2, 4, 5, 6, 7, 8]
'''
