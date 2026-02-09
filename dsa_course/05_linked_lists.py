"""
DSA Course - Module 11: Linked List Techniques
==============================================

CONCEPT: Linked Lists
---------------------
A linked list is a sequence of nodes where each node contains:
- Data (value)
- Pointer to the next node (and previous, if doubly linked)

Unlike arrays, elements are NOT stored contiguously in memory.

SINGLY LINKED LIST:
    [1] -> [2] -> [3] -> [4] -> None
    head                        tail

DOUBLY LINKED LIST:
    None <- [1] <-> [2] <-> [3] <-> [4] -> None

TRADEOFFS vs Arrays:
    Operation       | Array  | Linked List
    ----------------|--------|-------------
    Access by index | O(1)   | O(n)
    Insert at front | O(n)   | O(1)
    Insert at end   | O(1)*  | O(1) with tail
    Insert middle   | O(n)   | O(1) if have node
    Delete          | O(n)   | O(1) if have node
    Search          | O(n)   | O(n)

KEY TECHNIQUES:
1. Two pointers (fast/slow) - covered in Module 4
2. Dummy head node - simplifies edge cases
3. Reversal - iterative and recursive
4. Merge lists - combining sorted lists

WHEN TO USE LINKED LISTS:
- Frequent insertions/deletions at arbitrary positions
- Don't need random access
- Implementing stacks, queues, LRU cache
"""


# ============================================
# Node Definition
# ============================================

class ListNode:
    """Standard singly linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """For debugging: shows list from this node."""
        vals = []
        curr = self
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        return " -> ".join(vals)


# Helper functions for testing
def list_to_linked(arr: list) -> ListNode:
    """Convert Python list to linked list."""
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linked_to_list(head: ListNode) -> list:
    """Convert linked list to Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ============================================
# EXAMPLE: Reverse Linked List
# ============================================

def reverse_list_example(head: ListNode) -> ListNode:
    """
    Reverse a singly linked list.

    1 -> 2 -> 3 -> 4 -> None
    becomes
    4 -> 3 -> 2 -> 1 -> None

    Strategy (iterative):
    - Use three pointers: prev, curr, next_temp
    - For each node: save next, point curr to prev, advance
    """
    prev = None
    curr = head

    while curr:
        next_temp = curr.next  # Save next node
        curr.next = prev       # Reverse the link
        prev = curr            # Move prev forward
        curr = next_temp       # Move curr forward

    return prev  # prev is now the new head


# Let's trace through: 1 -> 2 -> 3 -> None
#
# Initial: prev=None, curr=1
#
# Step 1: next_temp=2, 1.next=None, prev=1, curr=2
#         None <- 1    2 -> 3 -> None
#
# Step 2: next_temp=3, 2.next=1, prev=2, curr=3
#         None <- 1 <- 2    3 -> None
#
# Step 3: next_temp=None, 3.next=2, prev=3, curr=None
#         None <- 1 <- 2 <- 3
#
# Return prev (3) -> 3 -> 2 -> 1 -> None


def reverse_list_recursive(head: ListNode) -> ListNode:
    """
    Reverse linked list recursively.

    Base case: empty or single node -> return as-is
    Recursive case: reverse the rest, then fix pointers
    """
    # Base case
    if not head or not head.next:
        return head

    # Recursively reverse the rest
    new_head = reverse_list_recursive(head.next)

    # Fix pointers: make next node point back to us
    head.next.next = head
    head.next = None

    return new_head


# ============================================
# QUESTION 1: Remove Nth Node From End
# ============================================

"""
PROBLEM: Remove the nth node from the END of a linked list.

Given the head of a linked list, remove the nth node from the end
and return the modified list's head.

Examples:
- [1,2,3,4,5], n=2 -> [1,2,3,5] (remove 4, which is 2nd from end)
- [1], n=1 -> [] (remove only node)
- [1,2], n=1 -> [1] (remove last node)
- [1,2], n=2 -> [2] (remove first node)

Implement the function below:
"""


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    """Remove nth node from end and return new head."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2: Merge Two Sorted Lists
# ============================================

"""
PROBLEM: Merge two sorted linked lists into one sorted list.

Given heads of two sorted linked lists, merge them into one sorted list.
The new list should be made by splicing together the nodes of the input lists.

Examples:
- [1,2,4], [1,3,4] -> [1,1,2,3,4,4]
- [], [0] -> [0]
- [], [] -> []

Implement the function below:
"""


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    """Merge two sorted linked lists."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 3: Linked List Cycle Detection
# ============================================

"""
PROBLEM: Detect if a linked list has a cycle.

Given head of a linked list, determine if the list has a cycle.
A cycle exists if some node can be reached again by following next pointers.

Examples:
- [3,2,0,-4] with cycle at position 1 -> True
  3 -> 2 -> 0 -> -4
       ^         |
       |_________|

- [1,2] with no cycle -> False
- [1] with no cycle -> False

Implement the function below:
"""


def has_cycle(head: ListNode) -> bool:
    """Return True if linked list has a cycle."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 4: Find Middle of Linked List
# ============================================

"""
PROBLEM: Find the middle node of a linked list.

Given the head of a linked list, return the middle node.
If there are two middle nodes, return the SECOND one.

Examples:
- [1,2,3,4,5] -> node with value 3
- [1,2,3,4,5,6] -> node with value 4 (second middle)
- [1] -> node with value 1

Implement the function below:
"""


def find_middle(head: ListNode) -> ListNode:
    """Return the middle node of the linked list."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 11: Linked List Techniques")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Reverse Linked List ---")
    head = list_to_linked([1, 2, 3, 4, 5])
    reversed_head = reverse_list_example(head)
    assert linked_to_list(reversed_head) == [5, 4, 3, 2, 1]
    head2 = list_to_linked([1, 2])
    assert linked_to_list(reverse_list_recursive(head2)) == [2, 1]
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Remove Nth From End ---")
    try:
        head = list_to_linked([1, 2, 3, 4, 5])
        result = remove_nth_from_end(head, 2)
        assert linked_to_list(result) == [1, 2, 3, 5], "Remove 4"

        head = list_to_linked([1])
        result = remove_nth_from_end(head, 1)
        assert result is None, "Remove only node"

        head = list_to_linked([1, 2])
        result = remove_nth_from_end(head, 1)
        assert linked_to_list(result) == [1], "Remove last"

        head = list_to_linked([1, 2])
        result = remove_nth_from_end(head, 2)
        assert linked_to_list(result) == [2], "Remove first"

        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: Merge Two Sorted Lists ---")
    try:
        l1 = list_to_linked([1, 2, 4])
        l2 = list_to_linked([1, 3, 4])
        merged = merge_two_lists(l1, l2)
        assert linked_to_list(merged) == [1, 1, 2, 3, 4, 4], "Basic merge"

        l1 = None
        l2 = list_to_linked([0])
        merged = merge_two_lists(l1, l2)
        assert linked_to_list(merged) == [0], "One empty"

        l1 = None
        l2 = None
        merged = merge_two_lists(l1, l2)
        assert merged is None, "Both empty"

        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    # Test Question 3
    print("\n--- Question 3: Linked List Cycle ---")
    try:
        # Create cycle: 1 -> 2 -> 3 -> 4 -> 2 (back to 2)
        head = list_to_linked([1, 2, 3, 4])
        head.next.next.next.next = head.next  # 4 points to 2
        assert has_cycle(head) == True, "Has cycle"

        # No cycle
        head = list_to_linked([1, 2, 3])
        assert has_cycle(head) == False, "No cycle"

        # Single node, no cycle
        head = list_to_linked([1])
        assert has_cycle(head) == False, "Single node"

        # Empty
        assert has_cycle(None) == False, "Empty list"

        print("All Question 3 tests PASSED!")
    except AssertionError as e:
        print(f"Question 3 FAILED: {e}")
    except Exception as e:
        print(f"Question 3 ERROR: {e}")

    # Test Question 4
    print("\n--- Question 4: Find Middle ---")
    try:
        head = list_to_linked([1, 2, 3, 4, 5])
        assert find_middle(head).val == 3, "Odd length"

        head = list_to_linked([1, 2, 3, 4, 5, 6])
        assert find_middle(head).val == 4, "Even length (second middle)"

        head = list_to_linked([1])
        assert find_middle(head).val == 1, "Single node"

        head = list_to_linked([1, 2])
        assert find_middle(head).val == 2, "Two nodes"

        # Edge cases
        head = list_to_linked([1, 2, 3])
        assert find_middle(head).val == 2, "Three nodes"

        print("All Question 4 tests PASSED!")
    except AssertionError as e:
        print(f"Question 4 FAILED: {e}")
    except Exception as e:
        print(f"Question 4 ERROR: {e}")

    # ==========================================
    # REVISION: Module 4 (Fast & Slow Pointers)
    # ==========================================
    print("\n--- REVISION: Fast & Slow Pointers ---")
    print("Q: In cycle detection, why does fast move 2 steps and slow 1 step?")
    print("A: If there's a cycle, fast gains 1 step per iteration, guaranteeing they meet.")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Linked lists: good for insert/delete, bad for random access
2. Dummy head node simplifies edge cases (empty list, remove first)
3. Two pointer techniques: fast/slow for cycle detection, middle finding
4. Reversal: iterative (3 pointers) or recursive
5. Always handle edge cases: empty list, single node, removing head
""")