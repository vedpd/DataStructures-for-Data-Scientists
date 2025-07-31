# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        #solving with BFS: moment we find a leaf node in the level by level check our work is done.

        if not root:
            return 0
        
        queue = deque([(root,1)]) #each item is a tuple (node,current_depth)

        while queue:
            node,depth = queue.popleft()

            if not node.left and not node.right:
                return depth
            
            if node.left:
                queue.append((node.left,depth+1))
            if node.right:
                queue.append((node.right,depth+1))
            
            