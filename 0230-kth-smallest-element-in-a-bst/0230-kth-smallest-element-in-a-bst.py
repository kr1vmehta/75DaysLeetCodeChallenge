# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Find the kth smallest element in a BST using iterative in-order traversal.
      
        Args:
            root: Root node of the binary search tree
            k: The position of the smallest element to find (1-indexed)
          
        Returns:
            The value of the kth smallest element
        """
        # Stack to maintain nodes for in-order traversal
        stack = []
        current_node = root
      
        # Iterate until we've processed all nodes or found the kth element
        while current_node or stack:
            # Traverse to the leftmost node, pushing all nodes onto stack
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                # Pop from stack (this gives us nodes in ascending order)
                current_node = stack.pop()
              
                # Decrement k as we've found one more element in sorted order
                k -= 1
              
                # Check if we've found the kth smallest element
                if k == 0:
                    return current_node.val
              
                # Move to the right subtree to continue in-order traversal
                current_node = current_node.right
        