# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import List, Optional

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
     
        result = []
      
        # Handle empty tree case
        if root is None:
            return result
      
        # Initialize queue with root node for BFS
        queue = deque([root])
      
        # Process tree level by level
        while queue:
            current_level = []
            level_size = len(queue)
          
            # Process all nodes at the current level
            for _ in range(level_size):
                # Remove node from front of queue
                node = queue.popleft()
              
                # Add node value to current level list
                current_level.append(node.val)
              
                # Add children to queue for next level processing
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
          
            # Add current level to result
            result.append(current_level)
      
        return result
        