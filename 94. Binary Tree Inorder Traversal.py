# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ans = root
        #  push and to the st
        #  move ans use left
        #  if curr  = None
        # if cur ; pusj curr
        # curr = curr.left
        #  else:
        #     cirr = st[-1]
        #     print
        #     curr = curr.right
        ans = []
        st = []
        cur = root
        
        while cur or st:
            while cur:
                st.append(cur)
                cur = cur.left

            cur = st.pop()
            ans.append(cur.val)
            cur = cur.right
        
        return ans
