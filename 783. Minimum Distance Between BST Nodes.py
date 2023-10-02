# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # prev , res = None , float("inf")
        dictionary  = {
            'prev' : None,
            'res' : float("inf")
        } 

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            # nonlocal prev ,res
            if dictionary['prev']:
                dictionary['res'] =min( dictionary['res'], node.val-dictionary['prev'].val)
            dictionary['prev'] = node
            dfs(node.right)

        dfs(root)
        return dictionary['res']
