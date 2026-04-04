# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def ino(root):
            if root == None: return 
            ino(root.left)
            ino(root.right)
            ans.append(root.val)
        ino(root)
        return ans