# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curr = root
        last_visited = None
        result = []
        while stack or curr:
            
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack[-1]
                if node.right and last_visited is not node.right:
                    curr = node.right
                else:
                    last_visited = stack.pop()
                    result.append(node.val)
        return result

        