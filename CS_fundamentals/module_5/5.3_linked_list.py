"""
Exercise 5.3: Linked List Implementation

LINKED LISTS
=============

A linked list stores elements in nodes, where each node points to the next.

Unlike arrays/lists, elements are NOT stored contiguously in memory.
Each node only knows about the NEXT node (singly linked) or
the NEXT and PREVIOUS nodes (doubly linked).

===================================
ARRAY vs LINKED LIST
===================================

    Operation       Array (list)    Linked List
    -------------------------------------------
    Access by index    O(1)           O(n)
    Insert at start    O(n)           O(1)
    Insert at end      O(1)*          O(n)**
    Insert in middle   O(n)           O(1)***
    Delete at start    O(n)           O(1)
    Search             O(n)           O(n)

    *  Amortised (dynamic array resizing)
    ** O(1) if you keep a tail pointer
    *** O(1) once you have a reference to the node

KEY INSIGHT: Linked lists are better when you need frequent
insertions/deletions at the beginning or middle.

===================================
STRUCTURE
===================================

    Node: [value | next] -> [value | next] -> [value | next] -> None
           ^head

    Each node holds:
    - val: the data
    - next: pointer to the next node (or None)

===================================
EXAMPLE: Building a linked list
===================================

    # Create nodes manually
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    # Result: 1 -> 2 -> 3 -> None

    # Traversal:
    current = head
    while current:
        print(current.val)  # 1, 2, 3
        current = current.next

===================================
EXERCISE
===================================

PART 1: Node class

Class: Node
- __init__(self, val, next=None)
- val: the value stored
- next: reference to next Node (default None)
- __repr__() -> str: Return "Node({val})"

---

PART 2: LinkedList class

Class: LinkedList

Attributes:
- head: Node or None (first node)

Methods:
- __init__(): Initialize with head = None

- append(val) -> None:
    Add a new node with val at the END of the list.
    If list is empty, new node becomes head.

- prepend(val) -> None:
    Add a new node with val at the START of the list.
    New node becomes the new head.

- delete(val) -> bool:
    Remove the FIRST node with the given value.
    Return True if found and deleted, False if not found.
    Handle: deleting head, deleting middle, deleting tail, value not found.

- find(val) -> Node | None:
    Return the first Node with the given value, or None if not found.

- to_list() -> list:
    Return a Python list of all values in order.
    Example: 1 -> 2 -> 3 -> [1, 2, 3]

- __str__() -> str:
    Return string like "1 -> 2 -> 3 -> None"
    Empty list returns "None"

- __len__() -> int:
    Return the number of nodes. Allows len(my_list).

---

PART 3 (HARD): Additional Methods

- insert_at(index: int, val) -> bool:
    Insert a new node at the given index (0-based).
    Return True if successful, False if index is out of range.
    index 0 = prepend, index == length = append.

- reverse() -> None:
    Reverse the linked list IN PLACE (don't create new nodes).
    1 -> 2 -> 3 becomes 3 -> 2 -> 1

    Hint: Use three pointers: prev, current, next_node
    Walk through the list, flipping each node's pointer.

- get_middle() -> Node | None:
    Return the middle node using the fast/slow pointer technique
    from DSA Module 4! (If even length, return second middle.)

ESTIMATED TIME: 45-60 minutes
"""


# ============================================
# PART 1: Node Class
# ============================================

# YOUR CODE HERE


# ============================================
# PART 2: LinkedList Class
# ============================================

# YOUR CODE HERE


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    # ==========================================
    # PART 1 TESTS: Node
    # ==========================================
    print("\n=== Test 1: Node ===")
    try:
        n1 = Node(1)
        n2 = Node(2)
        n1.next = n2

        assert n1.val == 1
        assert n1.next == n2
        assert n2.next is None
        assert repr(n1) == "Node(1)"

        print("  Node works correctly")
        print("Test 1 PASSED!")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")
    except Exception as e:
        print(f"Test 1 ERROR: {e}")

    # ==========================================
    # PART 2 TESTS: LinkedList
    # ==========================================
    print("\n=== Test 2: Append ===")
    try:
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        assert ll.to_list() == [1, 2, 3]
        assert str(ll) == "1 -> 2 -> 3 -> None"

        print("  Append works")
        print("Test 2 PASSED!")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 ERROR: {e}")

    print("\n=== Test 3: Prepend ===")
    try:
        ll = LinkedList()
        ll.prepend(3)
        ll.prepend(2)
        ll.prepend(1)

        assert ll.to_list() == [1, 2, 3]

        print("  Prepend works")
        print("Test 3 PASSED!")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 ERROR: {e}")

    print("\n=== Test 4: Delete ===")
    try:
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)

        # Delete middle
        assert ll.delete(2) == True
        assert ll.to_list() == [1, 3, 4]

        # Delete head
        assert ll.delete(1) == True
        assert ll.to_list() == [3, 4]

        # Delete tail
        assert ll.delete(4) == True
        assert ll.to_list() == [3]

        # Delete not found
        assert ll.delete(99) == False

        # Delete last remaining
        assert ll.delete(3) == True
        assert ll.to_list() == []

        # Delete from empty
        assert ll.delete(1) == False

        print("  Delete handles all cases")
        print("Test 4 PASSED!")
    except AssertionError as e:
        print(f"Test 4 FAILED: {e}")
    except Exception as e:
        print(f"Test 4 ERROR: {e}")

    print("\n=== Test 5: Find ===")
    try:
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)

        node = ll.find(20)
        assert node is not None
        assert node.val == 20

        assert ll.find(99) is None

        print("  Find works")
        print("Test 5 PASSED!")
    except AssertionError as e:
        print(f"Test 5 FAILED: {e}")
    except Exception as e:
        print(f"Test 5 ERROR: {e}")

    print("\n=== Test 6: Length ===")
    try:
        ll = LinkedList()
        assert len(ll) == 0

        ll.append(1)
        ll.append(2)
        assert len(ll) == 2

        ll.delete(1)
        assert len(ll) == 1

        print("  Length works")
        print("Test 6 PASSED!")
    except AssertionError as e:
        print(f"Test 6 FAILED: {e}")
    except Exception as e:
        print(f"Test 6 ERROR: {e}")

    print("\n=== Test 7: Empty List ===")
    try:
        ll = LinkedList()
        assert str(ll) == "None"
        assert ll.to_list() == []
        assert len(ll) == 0
        assert ll.find(1) is None

        print("  Empty list handled correctly")
        print("Test 7 PASSED!")
    except AssertionError as e:
        print(f"Test 7 FAILED: {e}")
    except Exception as e:
        print(f"Test 7 ERROR: {e}")

    # ==========================================
    # PART 3 TESTS (HARD): Uncomment when ready
    # ==========================================

    # print("\n=== Test 8: Insert At ===")
    # try:
    #     ll = LinkedList()
    #     ll.append(1)
    #     ll.append(3)
    #     ll.append(4)
    #
    #     assert ll.insert_at(1, 2) == True  # Insert 2 at index 1
    #     assert ll.to_list() == [1, 2, 3, 4]
    #
    #     assert ll.insert_at(0, 0) == True  # Insert at start
    #     assert ll.to_list() == [0, 1, 2, 3, 4]
    #
    #     assert ll.insert_at(5, 5) == True  # Insert at end
    #     assert ll.to_list() == [0, 1, 2, 3, 4, 5]
    #
    #     assert ll.insert_at(99, 10) == False  # Out of range
    #     assert ll.insert_at(-1, 10) == False  # Negative
    #
    #     print("  Insert at index works")
    #     print("Test 8 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 8 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 8 ERROR: {e}")

    # print("\n=== Test 9: Reverse ===")
    # try:
    #     ll = LinkedList()
    #     ll.append(1)
    #     ll.append(2)
    #     ll.append(3)
    #     ll.append(4)
    #
    #     ll.reverse()
    #     assert ll.to_list() == [4, 3, 2, 1]
    #
    #     # Single element
    #     ll2 = LinkedList()
    #     ll2.append(1)
    #     ll2.reverse()
    #     assert ll2.to_list() == [1]
    #
    #     # Empty
    #     ll3 = LinkedList()
    #     ll3.reverse()
    #     assert ll3.to_list() == []
    #
    #     print("  Reverse works in-place")
    #     print("Test 9 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 9 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 9 ERROR: {e}")

    # print("\n=== Test 10: Get Middle (Fast/Slow Pointers!) ===")
    # try:
    #     ll = LinkedList()
    #     for v in [1, 2, 3, 4, 5]:
    #         ll.append(v)
    #     assert ll.get_middle().val == 3  # Odd length
    #
    #     ll2 = LinkedList()
    #     for v in [1, 2, 3, 4]:
    #         ll2.append(v)
    #     assert ll2.get_middle().val == 3  # Even length, second middle
    #
    #     ll3 = LinkedList()
    #     ll3.append(1)
    #     assert ll3.get_middle().val == 1  # Single element
    #
    #     ll4 = LinkedList()
    #     assert ll4.get_middle() is None  # Empty
    #
    #     print("  Get middle with fast/slow pointers!")
    #     print("Test 10 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 10 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 10 ERROR: {e}")

    print("\n" + "=" * 60)
    print("LINKED LIST KEY LESSONS")
    print("=" * 60)
    print("""
1. Nodes hold data + a pointer to the next node
2. O(1) insert/delete at head (vs O(n) for arrays)
3. O(n) access by index (vs O(1) for arrays)
4. Reverse uses three pointers: prev, current, next_node
5. Fast/slow pointers find the middle in one pass
6. Always handle edge cases: empty list, single node, head/tail
""")
    print("=" * 60)
