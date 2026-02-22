"""
Exercise 5.4: Binary Search Tree (BST)

TREES
=====

A tree is a hierarchical data structure with nodes connected by edges.

    Root: The top node (no parent)
    Children: Nodes below a parent
    Leaf: A node with no children
    Height: Longest path from root to a leaf

BINARY TREE: Each node has at most TWO children (left and right).

BINARY SEARCH TREE (BST): A binary tree with an ordering rule:
    - Left child < Parent
    - Right child > Parent
    - This applies to ALL descendants, not just direct children

===================================
EXAMPLE BST
===================================

            8
          /   \\
         3     10
        / \\      \\
       1   6     14
          / \\   /
         4   7 13

    Search for 6:  8 -> go left -> 3 -> go right -> 6. Found!
    Search for 5:  8 -> 3 -> 6 -> 4 -> None. Not found.

===================================
KEY OPERATIONS & TIME COMPLEXITY
===================================

    Operation    Average    Worst (unbalanced)
    ------------------------------------------
    Search       O(log n)   O(n)
    Insert       O(log n)   O(n)
    Delete       O(log n)   O(n)
    Min/Max      O(log n)   O(n)

    Worst case happens when tree degenerates into a linked list:
    1 -> 2 -> 3 -> 4 (all right children)

===================================
TREE TRAVERSALS
===================================

Three ways to visit every node:

    In-order (Left, Root, Right):   Gives SORTED order for BST!
        1, 3, 4, 6, 7, 8, 10, 13, 14

    Pre-order (Root, Left, Right):  Good for copying/serialising the tree
        8, 3, 1, 6, 4, 7, 10, 14, 13

    Post-order (Left, Right, Root): Good for deleting the tree
        1, 4, 7, 6, 3, 13, 14, 10, 8

===================================
EXERCISE
===================================

PART 1: TreeNode class

Class: TreeNode
- __init__(self, val, left=None, right=None)
- val: the value stored
- left: left child TreeNode (default None)
- right: right child TreeNode (default None)
- __repr__() -> str: Return "TreeNode({val})"

---

PART 2: BinarySearchTree class

Class: BinarySearchTree

Attributes:
- root: TreeNode or None

Methods:
- __init__(): Initialize with root = None

- insert(val) -> None:
    Insert a new value into the BST maintaining the ordering rule.
    If val already exists, do nothing (no duplicates).
    Hint: Walk left if val < current, right if val > current.

- search(val) -> bool:
    Return True if val exists in the tree, False otherwise.

- find_min() -> any:
    Return the minimum value in the tree.
    Raise ValueError("Tree is empty") if empty.
    Hint: Keep going left until you can't.

- find_max() -> any:
    Return the maximum value in the tree.
    Raise ValueError("Tree is empty") if empty.
    Hint: Keep going right until you can't.

- inorder() -> list:
    Return values in sorted order (Left, Root, Right).

- preorder() -> list:
    Return values in pre-order (Root, Left, Right).

- postorder() -> list:
    Return values in post-order (Left, Right, Root).

---

PART 3 (HARD): Delete and Height

- delete(val) -> bool:
    Delete a node with the given value. Return True if found and deleted.

    Three cases:
    1. Leaf node (no children): Just remove it
    2. One child: Replace node with its child
    3. Two children: Replace with in-order successor (smallest in right subtree)
       then delete the successor from its original position

    This is the hardest operation on a BST!

- height() -> int:
    Return the height of the tree (longest path from root to leaf).
    Empty tree has height -1. Single node has height 0.
    Hint: Recursive - height = 1 + max(left_height, right_height)

ESTIMATED TIME: 45-60 minutes
"""


# ============================================
# PART 1: TreeNode Class
# ============================================

# YOUR CODE HERE


# ============================================
# PART 2: BinarySearchTree Class
# ============================================

# YOUR CODE HERE


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    # ==========================================
    # PART 1 TESTS: TreeNode
    # ==========================================
    print("\n=== Test 1: TreeNode ===")
    try:
        n = TreeNode(5)
        assert n.val == 5
        assert n.left is None
        assert n.right is None
        assert repr(n) == "TreeNode(5)"

        n.left = TreeNode(3)
        n.right = TreeNode(7)
        assert n.left.val == 3
        assert n.right.val == 7

        print("  TreeNode works correctly")
        print("Test 1 PASSED!")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")
    except Exception as e:
        print(f"Test 1 ERROR: {e}")

    # ==========================================
    # PART 2 TESTS: BST
    # ==========================================
    print("\n=== Test 2: Insert and Search ===")
    try:
        bst = BinarySearchTree()
        for val in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
            bst.insert(val)

        assert bst.search(6) == True
        assert bst.search(14) == True
        assert bst.search(1) == True
        assert bst.search(5) == False
        assert bst.search(99) == False

        # Duplicate insert should not break anything
        bst.insert(6)
        assert bst.search(6) == True

        print("  Insert and search work")
        print("Test 2 PASSED!")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 ERROR: {e}")

    print("\n=== Test 3: Find Min/Max ===")
    try:
        bst = BinarySearchTree()
        for val in [8, 3, 10, 1, 6, 14]:
            bst.insert(val)

        assert bst.find_min() == 1
        assert bst.find_max() == 14

        # Empty tree
        empty = BinarySearchTree()
        try:
            empty.find_min()
            assert False, "Should raise ValueError"
        except ValueError:
            pass

        print("  Min/Max work")
        print("Test 3 PASSED!")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 ERROR: {e}")

    print("\n=== Test 4: In-order Traversal (sorted!) ===")
    try:
        bst = BinarySearchTree()
        for val in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
            bst.insert(val)

        assert bst.inorder() == [1, 3, 4, 6, 7, 8, 10, 13, 14]

        print("  In-order gives sorted output")
        print("Test 4 PASSED!")
    except AssertionError as e:
        print(f"Test 4 FAILED: {e}")
    except Exception as e:
        print(f"Test 4 ERROR: {e}")

    print("\n=== Test 5: Pre-order Traversal ===")
    try:
        bst = BinarySearchTree()
        for val in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
            bst.insert(val)

        assert bst.preorder() == [8, 3, 1, 6, 4, 7, 10, 14, 13]

        print("  Pre-order traversal correct")
        print("Test 5 PASSED!")
    except AssertionError as e:
        print(f"Test 5 FAILED: {e}")
    except Exception as e:
        print(f"Test 5 ERROR: {e}")

    print("\n=== Test 6: Post-order Traversal ===")
    try:
        bst = BinarySearchTree()
        for val in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
            bst.insert(val)

        assert bst.postorder() == [1, 4, 7, 6, 3, 13, 14, 10, 8]

        print("  Post-order traversal correct")
        print("Test 6 PASSED!")
    except AssertionError as e:
        print(f"Test 6 FAILED: {e}")
    except Exception as e:
        print(f"Test 6 ERROR: {e}")

    print("\n=== Test 7: Empty Tree ===")
    try:
        bst = BinarySearchTree()
        assert bst.search(1) == False
        assert bst.inorder() == []
        assert bst.preorder() == []
        assert bst.postorder() == []

        print("  Empty tree handled correctly")
        print("Test 7 PASSED!")
    except AssertionError as e:
        print(f"Test 7 FAILED: {e}")
    except Exception as e:
        print(f"Test 7 ERROR: {e}")

    print("\n=== Test 8: Single Node ===")
    try:
        bst = BinarySearchTree()
        bst.insert(5)

        assert bst.search(5) == True
        assert bst.find_min() == 5
        assert bst.find_max() == 5
        assert bst.inorder() == [5]

        print("  Single node tree works")
        print("Test 8 PASSED!")
    except AssertionError as e:
        print(f"Test 8 FAILED: {e}")
    except Exception as e:
        print(f"Test 8 ERROR: {e}")

    # ==========================================
    # PART 3 TESTS (HARD): Uncomment when ready
    # ==========================================

    # print("\n=== Test 9: Delete - Leaf ===")
    # try:
    #     bst = BinarySearchTree()
    #     for val in [8, 3, 10, 1, 6]:
    #         bst.insert(val)
    #
    #     assert bst.delete(1) == True  # Leaf
    #     assert bst.inorder() == [3, 6, 8, 10]
    #     assert bst.delete(99) == False  # Not found
    #
    #     print("  Delete leaf works")
    #     print("Test 9 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 9 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 9 ERROR: {e}")

    # print("\n=== Test 10: Delete - One Child ===")
    # try:
    #     bst = BinarySearchTree()
    #     for val in [8, 3, 10, 14]:
    #         bst.insert(val)
    #
    #     assert bst.delete(10) == True  # Has one child (14)
    #     assert bst.inorder() == [3, 8, 14]
    #
    #     print("  Delete node with one child works")
    #     print("Test 10 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 10 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 10 ERROR: {e}")

    # print("\n=== Test 11: Delete - Two Children ===")
    # try:
    #     bst = BinarySearchTree()
    #     for val in [8, 3, 10, 1, 6, 14]:
    #         bst.insert(val)
    #
    #     assert bst.delete(3) == True  # Has two children (1 and 6)
    #     assert bst.inorder() == [1, 6, 8, 10, 14]
    #     assert bst.search(3) == False
    #
    #     # Delete root
    #     assert bst.delete(8) == True
    #     assert 8 not in bst.inorder()
    #     # Remaining values should still be sorted
    #     result = bst.inorder()
    #     assert result == sorted(result)
    #
    #     print("  Delete node with two children works")
    #     print("Test 11 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 11 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 11 ERROR: {e}")

    # print("\n=== Test 12: Height ===")
    # try:
    #     bst = BinarySearchTree()
    #     assert bst.height() == -1  # Empty
    #
    #     bst.insert(8)
    #     assert bst.height() == 0  # Just root
    #
    #     bst.insert(3)
    #     bst.insert(10)
    #     assert bst.height() == 1
    #
    #     bst.insert(1)
    #     bst.insert(6)
    #     bst.insert(14)
    #     assert bst.height() == 2
    #
    #     bst.insert(4)
    #     bst.insert(7)
    #     bst.insert(13)
    #     assert bst.height() == 3
    #
    #     print("  Height calculation correct")
    #     print("Test 12 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 12 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 12 ERROR: {e}")

    print("\n" + "=" * 60)
    print("BST KEY LESSONS")
    print("=" * 60)
    print("""
1. BST rule: left < parent < right (for ALL descendants)
2. In-order traversal gives SORTED output
3. Search/insert/delete are O(log n) average, O(n) worst
4. Worst case: tree degenerates into a linked list
5. Delete with two children: replace with in-order successor
6. Three traversals: in-order, pre-order, post-order
7. Height = 1 + max(left_height, right_height) (recursive!)
""")
    print("=" * 60)
