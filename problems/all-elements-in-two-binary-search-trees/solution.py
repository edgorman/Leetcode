# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        values = []
        nodes = [root1, root2]
        
        # Extract values from roots
        while len(nodes) > 0:
            # Take first node from list
            node = nodes[0]
            nodes.remove(node)
            
            # If node is not none, add to values list
            if node != None:
                values.append(node.val)
            
                # If children are not none, add to nodes list
                if node.left != None:
                    nodes.append(node.left)
                if node.right != None:
                    nodes.append(node.right)
        
        # Sort numbers in ascending order
        values.sort()
        return values
