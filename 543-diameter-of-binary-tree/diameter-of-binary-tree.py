# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # res=[0]

        # def dfs(root):
        #     if not root:
        #         return -1
            
        #     left = dfs(root.left)
        #     right = dfs(root.right)
            
        #     res[0] = max(res[0],2 + left + right)
        #     return 1 + max(left,right)
    
        # dfs(root)
        # return res[0]

        largest_diameter=[0] #global variable to be updated

        def height(root):
            if root is None:
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)

            diameter = left_height + right_height

            largest_diameter[0] = max(largest_diameter[0],diameter)

            return 1 + max(left_height, right_height)

        height(root)

        return largest_diameter[0]

        