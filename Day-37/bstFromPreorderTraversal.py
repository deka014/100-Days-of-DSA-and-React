# 1008. Construct Binary Search Tree from Preorder Traversal
# Medium
# 4.9K
# 66
# Companies

# Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

# It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

# A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

# A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

 

# Example 1:

# Input: preorder = [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

# Example 2:

# Input: preorder = [1,3]
# Output: [1,null,3]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder) :
        
        #intuiton - the sorted preorder is inorder of a BST always - use both to generate
        #or use bound method shown below

        self.ind = 0

        def rec(ind,bound):

            if self.ind == len(preorder) or preorder[self.ind] > bound:
                return None

            root = TreeNode(preorder[self.ind])
            self.ind+=1
            root.left = rec(self.ind,root.val)
            root.right = rec(self.ind,bound)

            
            return root
        
        return rec(0,1000)


            

