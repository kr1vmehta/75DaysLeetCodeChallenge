# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the diameter of a binary tree.
        The diameter is the length of the longest path between any two nodes.
        This path may or may not pass through the root.
      
        Args:
            root: The root node of the binary tree
          
        Returns:
            The diameter (number of edges) of the binary tree
        """
        # Initialize the maximum diameter found so far
        self.max_diameter = 0
      
        def calculate_height(node: Optional[TreeNode]) -> int:
            """
            Calculate the height of the tree rooted at the given node.
            Also update the maximum diameter during traversal.
          
            Args:
                node: Current node being processed
              
            Returns:
                The height of the subtree rooted at this node
            """
            # Base case: empty node has height 0
            if node is None:
                return 0
          
            # Recursively calculate heights of left and right subtrees
            left_height = calculate_height(node.left)
            right_height = calculate_height(node.right)
          
            # The diameter passing through this node is the sum of 
            # left and right subtree heights
            current_diameter = left_height + right_height
          
            # Update the maximum diameter if current is larger
            self.max_diameter = max(self.max_diameter, current_diameter)
          
            # Return the height of this subtree (1 + max height of children)
            return 1 + max(left_height, right_height)
      
        # Start the DFS traversal from root
        calculate_height(root)
      
        # Return the maximum diameter found
        return self.max_diameter
        