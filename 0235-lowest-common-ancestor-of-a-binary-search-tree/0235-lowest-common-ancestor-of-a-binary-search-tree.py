# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(
        self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'
    ) -> 'TreeNode':
        """
        Find the lowest common ancestor (LCA) of two nodes in a binary search tree.
      
        Args:
            root: The root node of the BST
            p: First target node
            q: Second target node
          
        Returns:
            The lowest common ancestor node of p and q
        """
        # Iterate through the tree starting from root
        while True:
            # If both nodes are smaller than current node, LCA must be in left subtree
            if root.val < min(p.val, q.val):
                root = root.right
            # If both nodes are greater than current node, LCA must be in right subtree
            elif root.val > max(p.val, q.val):
                root = root.left
            # Current node is the LCA when:
            # - One node is on left and other is on right of current node, or
            # - Current node equals one of the target nodes
            else:
                return root
        