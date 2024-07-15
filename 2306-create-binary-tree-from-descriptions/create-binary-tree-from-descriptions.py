# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        from collections import defaultdict

        nodes = {}  # This will map values to TreeNode objects
        has_parent = {}  # This will track which nodes have a parent

        for parent, child, isLeft in descriptions:
            # Create or retrieve the parent node
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            parentNode = nodes[parent]
        
            # Create or retrieve the child node
            if child not in nodes:
                nodes[child] = TreeNode(child)
            childNode = nodes[child]
        
            # Set the child node as left or right child
            if isLeft == 1:
                parentNode.left = childNode
            else:
                parentNode.right = childNode
        
            # Mark the child as having a parent
            has_parent[child] = True
    
        # Find the root node
        for node in nodes:
            if node not in has_parent:
                return nodes[node]
        return None  # In case there is no root (though the problem guarantees a valid tree)
