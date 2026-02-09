"""
DSA Course - Module 17: Binary Trees
====================================

CONCEPT: Binary Trees
---------------------
A tree where each node has at most 2 children (left and right).

TERMINOLOGY:
- Root: top node (no parent)
- Leaf: node with no children
- Height: longest path from root to leaf
- Depth: distance from root to node
- Level: set of nodes at same depth

TYPES:
- Full binary tree: every node has 0 or 2 children
- Complete: all levels filled except last (filled left to right)
- Perfect: all leaves at same level, all internal nodes have 2 children
- BST (Binary Search Tree): left < node < right

TRAVERSAL ORDERS:
1. Pre-order: node -> left -> right (root first)
2. In-order: left -> node -> right (sorted for BST)
3. Post-order: left -> right -> node (root last)
4. Level-order: BFS, level by level

COMMON PATTERNS:
- Recursive: base case (null), then recurse on children
- Return value: compute result based on children's results
- Pass value down: send info to children via parameters
- BFS for level-order operations
"""


# ============================================
# Node Definition
# ============================================

class TreeNode:
    """Binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Helper to build tree from list (level order with None for missing)
def build_tree(values: list) -> TreeNode:
    """Build tree from level-order list. None represents missing node."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


# ============================================
# EXAMPLE: Tree Traversals
# ============================================

def preorder_example(root: TreeNode) -> list[int]:
    """
    Pre-order traversal: node -> left -> right

         1
        / \
       2   3
      / \
     4   5

    Pre-order: [1, 2, 4, 5, 3]
    """
    result = []

    def traverse(node):
        if not node:
            return
        result.append(node.val)  # Process node
        traverse(node.left)       # Left subtree
        traverse(node.right)      # Right subtree

    traverse(root)
    return result


def inorder_example(root: TreeNode) -> list[int]:
    """
    In-order traversal: left -> node -> right

    In-order: [4, 2, 5, 1, 3]

    For BST, in-order gives sorted sequence!
    """
    result = []

    def traverse(node):
        if not node:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)

    traverse(root)
    return result


def postorder_example(root: TreeNode) -> list[int]:
    """
    Post-order traversal: left -> right -> node

    Post-order: [4, 5, 2, 3, 1]

    Useful for deletion, computing subtree values.
    """
    result = []

    def traverse(node):
        if not node:
            return
        traverse(node.left)
        traverse(node.right)
        result.append(node.val)

    traverse(root)
    return result


def levelorder_example(root: TreeNode) -> list[list[int]]:
    """
    Level-order traversal using BFS.

    Level-order: [[1], [2, 3], [4, 5]]
    """
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


# ============================================
# QUESTION 1: Maximum Depth of Binary Tree
# ============================================

"""
PROBLEM: Find the maximum depth (height) of a binary tree.

The depth is the number of nodes along the longest path from
root to the farthest leaf.

Examples:
- [3,9,20,null,null,15,7] -> 3
      3
     / \
    9  20
      /  \
     15   7

- [1,null,2] -> 2
- [] -> 0

Implement the function below:
"""


def max_depth(root: TreeNode) -> int:
    """Return the maximum depth of the binary tree."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2: Invert Binary Tree
# ============================================

"""
PROBLEM: Mirror a binary tree (swap left and right children).

     4               4
   /   \           /   \
  2     7    ->   7     2
 / \   / \       / \   / \
1   3 6   9     9   6 3   1

Examples:
- [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
- [2,1,3] -> [2,3,1]
- [] -> []

Implement the function below:
"""


def invert_tree(root: TreeNode) -> TreeNode:
    """Invert the binary tree and return the root."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 3: Path Sum (Root to Leaf)
# ============================================

"""
PROBLEM: Check if there's a root-to-leaf path with given sum.

Given a binary tree and target sum, return True if there exists a
root-to-leaf path where all node values sum to target.

Examples:
-       5
       / \
      4   8
     /   / \
    11  13  4
   /  \      \
  7    2      1

  target=22 -> True (5->4->11->2)

- [1,2,3], target=5 -> False

Implement the function below:
"""


def has_path_sum(root: TreeNode, target_sum: int) -> bool:
    """Return True if root-to-leaf path sums to target."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 4: Lowest Common Ancestor (LCA)
# ============================================

"""
PROBLEM: Find the lowest common ancestor of two nodes.

The LCA of nodes p and q is the deepest node that has both p and q
as descendants (a node can be its own descendant).

Examples:
-       3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4

  LCA(5, 1) = 3
  LCA(5, 4) = 5 (5 is ancestor of 4, and ancestor of itself)

Implement the function below:
"""


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """Return the lowest common ancestor of nodes p and q."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 5: Validate Binary Search Tree
# ============================================

"""
PROBLEM: Check if a binary tree is a valid BST.

A valid BST:
- Left subtree contains only nodes with values < node's value
- Right subtree contains only nodes with values > node's value
- Both subtrees must also be valid BSTs

Examples:
-   2
   / \
  1   3   -> True

-   5
   / \
  1   4
     / \
    3   6   -> False (3 is in right subtree of 5 but 3 < 5)

Implement the function below:
"""


def is_valid_bst(root: TreeNode) -> bool:
    """Return True if tree is a valid BST."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 17: Binary Trees")
    print("=" * 60)

    # Build test tree:  1
    #                  / \
    #                 2   3
    #                / \
    #               4   5
    test_tree = build_tree([1, 2, 3, 4, 5])

    # Test Example
    print("\n--- Example: Tree Traversals ---")
    assert preorder_example(test_tree) == [1, 2, 4, 5, 3]
    assert inorder_example(test_tree) == [4, 2, 5, 1, 3]
    assert postorder_example(test_tree) == [4, 5, 2, 3, 1]
    assert levelorder_example(test_tree) == [[1], [2, 3], [4, 5]]
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Maximum Depth ---")
    try:
        assert max_depth(build_tree([3, 9, 20, None, None, 15, 7])) == 3
        assert max_depth(build_tree([1, None, 2])) == 2
        assert max_depth(None) == 0
        assert max_depth(build_tree([1])) == 1
        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: Invert Binary Tree ---")
    try:
        tree = build_tree([4, 2, 7, 1, 3, 6, 9])
        inverted = invert_tree(tree)
        assert levelorder_example(inverted) == [[4], [7, 2], [9, 6, 3, 1]]

        assert invert_tree(None) is None
        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    # Test Question 3
    print("\n--- Question 3: Path Sum ---")
    try:
        tree = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
        assert has_path_sum(tree, 22) == True
        assert has_path_sum(build_tree([1, 2, 3]), 5) == False
        assert has_path_sum(None, 0) == False
        assert has_path_sum(build_tree([1, 2]), 1) == False  # Must be leaf
        print("All Question 3 tests PASSED!")
    except AssertionError as e:
        print(f"Question 3 FAILED: {e}")
    except Exception as e:
        print(f"Question 3 ERROR: {e}")

    # Test Question 4
    print("\n--- Question 4: Lowest Common Ancestor ---")
    try:
        # Build tree and get references to nodes
        tree = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        # Navigate to find p=5 and q=1
        p = tree.left  # node 5
        q = tree.right  # node 1
        assert lowest_common_ancestor(tree, p, q).val == 3

        # p=5, q=4
        q4 = tree.left.right.right  # node 4
        assert lowest_common_ancestor(tree, p, q4).val == 5

        print("All Question 4 tests PASSED!")
    except AssertionError as e:
        print(f"Question 4 FAILED: {e}")
    except Exception as e:
        print(f"Question 4 ERROR: {e}")

    # Test Question 5
    print("\n--- Question 5: Validate BST ---")
    try:
        assert is_valid_bst(build_tree([2, 1, 3])) == True
        assert is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6])) == False
        assert is_valid_bst(None) == True
        assert is_valid_bst(build_tree([1])) == True
        # Edge case: [5, 4, 6, None, None, 3, 7] - 3 is in right subtree but < 5
        assert is_valid_bst(build_tree([5, 4, 6, None, None, 3, 7])) == False
        # More edge cases
        assert is_valid_bst(build_tree([1, 1])) == False, "Duplicate values"
        print("All Question 5 tests PASSED!")
    except AssertionError as e:
        print(f"Question 5 FAILED: {e}")
    except Exception as e:
        print(f"Question 5 ERROR: {e}")

    # ==========================================
    # REVISION: Module 16 (Dynamic Programming)
    # ==========================================
    print("\n--- REVISION: Dynamic Programming ---")
    print("Q: What's the difference between top-down and bottom-up DP?")
    print("A: Top-down: recursive + memoization. Bottom-up: iterative, fill table in order.")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Tree problems are naturally recursive: base case (null), recurse on children
2. Traversals: pre-order (node first), in-order (sorted for BST), post-order, level-order
3. Common pattern: return value from children, combine at parent
4. Pass info down via parameters (e.g., valid range for BST)
5. BFS (queue) for level-order, DFS (recursion/stack) for others
""")