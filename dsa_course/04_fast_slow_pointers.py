"""
DSA Course - Module 4: Fast & Slow Pointers (Floyd's Tortoise & Hare)
====================================================================

CONCEPT: Fast and Slow Pointers
-------------------------------
Two pointers moving at different speeds through a sequence.
Typically: slow moves 1 step, fast moves 2 steps.

THE KEY INSIGHT:
If there's a cycle, fast will eventually "lap" slow and they'll meet.
If there's no cycle, fast will reach the end.

MAIN USE CASES:

1. CYCLE DETECTION
   - Fast moves 2x speed of slow
   - If they meet -> cycle exists
   - If fast reaches end -> no cycle

2. FINDING MIDDLE
   - When fast reaches end, slow is at middle
   - Because slow traveled half the distance

3. FINDING CYCLE START
   - After detecting cycle, reset one pointer to start
   - Move both at same speed -> they meet at cycle start

WHY IT WORKS (intuition, no math needed):
- Think of two runners on a circular track
- The faster one will eventually catch up to the slower one
- They must meet if the track loops back
"""


# ============================================
# LINKED LIST NODE (we need this for examples)
# ============================================

class ListNode:
    """Simple linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values: list) -> ListNode:
    """Helper: Create linked list from list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: ListNode) -> list:
    """Helper: Convert linked list back to list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ============================================
# EXAMPLE: Find Middle of Linked List
# ============================================

def find_middle_example(head: ListNode) -> ListNode:
    """
    Find the middle node of a linked list.
    If two middles, return the second one.

    Strategy:
    - slow moves 1 step at a time
    - fast moves 2 steps at a time
    - When fast reaches end, slow is at middle

    Why? Fast travels 2x distance. When fast finishes,
    slow has traveled exactly half = middle.
    """
    if not head:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next        # Move 1 step
        fast = fast.next.next   # Move 2 steps

    return slow


# Let's trace through: 1 -> 2 -> 3 -> 4 -> 5
#
# Start: slow=1, fast=1
# Step 1: slow=2, fast=3
# Step 2: slow=3, fast=5
# Step 3: fast.next is None, stop
# Return slow (node with value 3) - THE MIDDLE!
#
# For even length: 1 -> 2 -> 3 -> 4
# Start: slow=1, fast=1
# Step 1: slow=2, fast=3
# Step 2: slow=3, fast=None (fast.next.next)
# Actually: fast=3, fast.next=4, fast.next.next=None
# So after step 2: slow=3, fast=None? Let's retrace...
#
# Start: slow=1, fast=1
# Check: fast(1) exists, fast.next(2) exists -> continue
# Step 1: slow=2, fast=3
# Check: fast(3) exists, fast.next(4) exists -> continue
# Step 2: slow=3, fast=None (went past end)
# Check: fast is None -> stop
# Return slow (node 3) - second of two middles


# ============================================
# QUESTION 1: Linked List Cycle Detection
# ============================================

"""
PROBLEM: Detect if a linked list has a cycle.

A cycle means some node's next pointer points back to a previous node,
creating an infinite loop.

Examples:
- 1 -> 2 -> 3 -> 4 -> 2 (back to 2) -> Has cycle
- 1 -> 2 -> 3 -> 4 -> None -> No cycle

HINT: Use fast and slow pointers.
      - If fast reaches None -> no cycle
      - If fast equals slow at some point -> cycle exists

      Start both at head. Move slow by 1, fast by 2.
      Keep going until fast is None OR slow == fast.

Implement the function below:
"""


def has_cycle(head: ListNode) -> bool:
    """Return True if linked list has a cycle, False otherwise."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2: Happy Number
# ============================================

"""
PROBLEM: Determine if a number is "happy".

A happy number is defined by this process:
1. Start with any positive integer
2. Replace it with the sum of squares of its digits
3. Repeat until you get 1 (happy!) or enter an endless cycle (not happy)

Examples:
- 19 -> 1^2 + 9^2 = 82 -> 8^2 + 2^2 = 68 -> 6^2 + 8^2 = 100
       -> 1^2 + 0^2 + 0^2 = 1 -> HAPPY!
- 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> CYCLE, not happy

HINT: This is cycle detection in disguise!
      - The "linked list" is the sequence of numbers
      - "next node" is the sum of squares of digits
      - Use fast and slow pointers on this sequence
      - If they meet at 1 -> happy
      - If they meet elsewhere -> cycle, not happy

      First, write a helper function to compute sum of squares of digits.

Implement the function below:
"""


def is_happy(n: int) -> bool:
    """Return True if n is a happy number, False otherwise."""
    # YOUR CODE HERE
    # Hint: You might want a helper function like:
    # def get_next(num): return sum of squares of digits
    pass


# ============================================
# REVISION: Quick Review from Module 3
# ============================================

"""
REVISION: Check if a string is a palindrome using two pointers.

Use left and right pointers converging toward the center.

Example: "racecar" -> True, "hello" -> False
"""


def revision_is_palindrome(s: str) -> bool:
    """Return True if the string is a palindrome."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 4: Fast & Slow Pointers")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Find Middle ---")
    list1 = create_linked_list([1, 2, 3, 4, 5])
    assert find_middle_example(list1).val == 3

    list2 = create_linked_list([1, 2, 3, 4, 5, 6])
    assert find_middle_example(list2).val == 4  # Second middle

    list3 = create_linked_list([1])
    assert find_middle_example(list3).val == 1
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Linked List Cycle ---")
    try:
        # Create list with cycle: 1 -> 2 -> 3 -> 4 -> back to 2
        head1 = ListNode(1)
        head1.next = ListNode(2)
        head1.next.next = ListNode(3)
        head1.next.next.next = ListNode(4)
        head1.next.next.next.next = head1.next  # Cycle to node 2

        assert has_cycle(head1) == True, "Should detect cycle"

        # Create list without cycle
        head2 = create_linked_list([1, 2, 3, 4])
        assert has_cycle(head2) == False, "No cycle"

        # Empty list
        assert has_cycle(None) == False, "Empty list"

        # Single node, no cycle
        head3 = ListNode(1)
        assert has_cycle(head3) == False, "Single node, no cycle"

        # Single node with self-loop
        head4 = ListNode(1)
        head4.next = head4
        assert has_cycle(head4) == True, "Self loop"

        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: Happy Number ---")
    try:
        assert is_happy(19) == True, "19 is happy"
        assert is_happy(2) == False, "2 is not happy"
        assert is_happy(1) == True, "1 is happy"
        assert is_happy(7) == True, "7 is happy"
        assert is_happy(4) == False, "4 is not happy"
        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    # ==========================================
    # REVISION: Module 3 (Two Pointers)
    # ==========================================
    print("\n--- REVISION: Two Pointers ---")
    try:
        assert revision_is_palindrome("racecar") == True
        assert revision_is_palindrome("hello") == False
        print("Revision PASSED!")
    except AssertionError as e:
        print(f"Revision FAILED: {e}")
    except Exception as e:
        print(f"Revision ERROR: {e}")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Fast & slow pointers: slow moves 1 step, fast moves 2 steps
2. Finding middle: when fast ends, slow is at middle
3. Cycle detection: if they meet, there's a cycle
4. Any sequence that might loop can use this pattern!
5. Happy Number shows this pattern isn't just for linked lists
""")
