"""
---Range Sum of BST---

Given the root node of a binary search tree, return the sum of values of all
nodes with a value in the range [low, high].
"""


class Solution:
    def __init__(self):
        pass

    def range_sum_bst(self, root: TreeNode, low: int, high: int) -> int:
        tree_node_values = self.traverse_tree(root)

        filtered_tree_node_values = filter(lambda x: low <= x <= high,
                                           tree_node_values)

        return sum(filtered_tree_node_values)

    def traverse_tree(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        left_list = self.traverse_tree(root.left)
        right_list = self.traverse_tree(root.right)

        return left_list + [root.val] + right_list
