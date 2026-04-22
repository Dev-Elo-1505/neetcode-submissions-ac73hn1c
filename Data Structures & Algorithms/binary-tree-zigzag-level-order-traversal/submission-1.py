# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            curr_level = deque()

            for _ in range(level_size):
                curr = queue.popleft()

                if left_to_right:
                    curr_level.append(curr.val)
                else:
                    curr_level.appendleft(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
            result.append(list(curr_level))
            left_to_right = not left_to_right

        return result
                
    
        