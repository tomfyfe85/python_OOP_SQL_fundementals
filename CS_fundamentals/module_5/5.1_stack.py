"""
Exercise 5.1: Stack Implementation

STACKS
======

A stack is a Last-In, First-Out (LIFO) data structure.

Think of a stack of plates:
- You ADD plates to the TOP (push)
- You REMOVE plates from the TOP (pop)
- You can only see the TOP plate (peek)

===================================
KEY OPERATIONS
===================================

    push(item)   - Add item to top         O(1)
    pop()        - Remove & return top     O(1)
    peek()       - Return top without removing  O(1)
    is_empty()   - Check if stack is empty O(1)
    size()       - Return number of items  O(1)

All O(1) - this is what makes stacks efficient!

===================================
REAL-WORLD USE CASES
===================================

1. Undo/Redo in text editors
2. Browser back button (history stack)
3. Function call stack (recursion!)
4. Balancing brackets in code: ({[]})
5. Reversing sequences

===================================
EXAMPLE: How push/pop works
===================================

    stack = []

    push(1)  -> [1]
    push(2)  -> [1, 2]
    push(3)  -> [1, 2, 3]
    peek()   -> 3 (stack unchanged)
    pop()    -> 3, stack is now [1, 2]
    pop()    -> 2, stack is now [1]
    push(4)  -> [1, 4]
    pop()    -> 4, stack is now [1]

===================================
EXERCISE
===================================

PART 1: Implement a Stack class

Class: Stack

Attributes:
- _items: list (internal storage, private)

Methods:
- __init__(): Initialize empty stack
- push(item) -> None: Add item to top of stack
- pop() -> any: Remove and return top item. Raise IndexError("Stack is empty") if empty.
- peek() -> any: Return top item without removing. Raise IndexError("Stack is empty") if empty.
- is_empty() -> bool: Return True if stack has no items
- size() -> int: Return number of items in stack
- __str__() -> str: Return string like "Stack([1, 2, 3])" (bottom to top)

---

PART 2: Bracket Validator (using your Stack)

Use your Stack class to solve a classic problem:

Given a string containing brackets, determine if the brackets are valid.

Rules:
- Open brackets must be closed by the same type: (), {}, []
- Open brackets must be closed in the correct order
- Every close bracket must have a matching open bracket

Function: is_valid_brackets(s: str) -> bool

Examples:
    is_valid_brackets("()")       -> True
    is_valid_brackets("()[]{}")   -> True
    is_valid_brackets("(]")       -> False
    is_valid_brackets("([)]")     -> False
    is_valid_brackets("{[]}")     -> True
    is_valid_brackets("")         -> True

Hint: Push open brackets. When you see a close bracket, pop and check it matches.

---

PART 3 (HARD): MinStack

Design a stack that supports push, pop, peek, AND retrieving the
minimum element - ALL in O(1) time.

Class: MinStack

Methods:
- __init__(): Initialize
- push(val: int) -> None: Push value
- pop() -> int: Remove and return top
- peek() -> int: Return top without removing
- get_min() -> int: Return the minimum element in the stack

The challenge: get_min() must be O(1), not O(n).
Hint: Use TWO stacks - one for values, one to track minimums.

ESTIMATED TIME: 30-45 minutes
"""


# ============================================
# PART 1: Stack Class
# ============================================

# YOUR CODE HERE


# ============================================
# PART 2: Bracket Validator
# ============================================

def is_valid_brackets(s: str) -> bool:
    """Return True if all brackets in s are properly matched and nested."""
    # YOUR CODE HERE
    pass


# ============================================
# PART 3 (HARD): MinStack
# ============================================

# YOUR CODE HERE


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    # ==========================================
    # PART 1 TESTS: Stack
    # ==========================================
    print("\n=== Test 1: Stack - Basic Operations ===")
    try:
        s = Stack()
        assert s.is_empty() == True
        assert s.size() == 0

        s.push(1)
        s.push(2)
        s.push(3)

        assert s.is_empty() == False
        assert s.size() == 3
        assert s.peek() == 3
        assert s.size() == 3  # peek doesn't remove

        print("  Basic operations work")
        print("Test 1 PASSED!")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")
    except Exception as e:
        print(f"Test 1 ERROR: {e}")

    print("\n=== Test 2: Stack - Push and Pop ===")
    try:
        s = Stack()
        s.push("a")
        s.push("b")
        s.push("c")

        assert s.pop() == "c"
        assert s.pop() == "b"
        assert s.pop() == "a"
        assert s.is_empty() == True

        print("  LIFO order confirmed")
        print("Test 2 PASSED!")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 ERROR: {e}")

    print("\n=== Test 3: Stack - Error Handling ===")
    try:
        s = Stack()

        try:
            s.pop()
            assert False, "Should raise IndexError"
        except IndexError as e:
            assert "empty" in str(e).lower()

        try:
            s.peek()
            assert False, "Should raise IndexError"
        except IndexError as e:
            assert "empty" in str(e).lower()

        print("  Empty stack errors handled correctly")
        print("Test 3 PASSED!")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 ERROR: {e}")

    print("\n=== Test 4: Stack - __str__ ===")
    try:
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        assert str(s) == "Stack([1, 2, 3])"

        empty = Stack()
        assert str(empty) == "Stack([])"

        print("  String representation correct")
        print("Test 4 PASSED!")
    except AssertionError as e:
        print(f"Test 4 FAILED: {e}")
    except Exception as e:
        print(f"Test 4 ERROR: {e}")

    # ==========================================
    # PART 2 TESTS: Bracket Validator
    # ==========================================
    print("\n=== Test 5: Bracket Validator ===")
    try:
        assert is_valid_brackets("()") == True
        assert is_valid_brackets("()[]{}") == True
        assert is_valid_brackets("(]") == False
        assert is_valid_brackets("([)]") == False
        assert is_valid_brackets("{[]}") == True
        assert is_valid_brackets("") == True
        assert is_valid_brackets("(") == False
        assert is_valid_brackets(")") == False
        assert is_valid_brackets("((()))") == True
        assert is_valid_brackets("{[()]}") == True
        assert is_valid_brackets("hello(world)") == True  # non-bracket chars ignored

        print("  All bracket validation tests passed")
        print("Test 5 PASSED!")
    except AssertionError as e:
        print(f"Test 5 FAILED: {e}")
    except Exception as e:
        print(f"Test 5 ERROR: {e}")

    # ==========================================
    # PART 3 TESTS (HARD): MinStack
    # ==========================================

    # Uncomment when ready:

    # print("\n=== Test 6: MinStack ===")
    # try:
    #     ms = MinStack()
    #     ms.push(5)
    #     ms.push(3)
    #     ms.push(7)
    #     ms.push(1)
    #
    #     assert ms.get_min() == 1
    #     assert ms.peek() == 1
    #
    #     ms.pop()  # Remove 1
    #     assert ms.get_min() == 3  # Min updates!
    #
    #     ms.pop()  # Remove 7
    #     assert ms.get_min() == 3
    #
    #     ms.pop()  # Remove 3
    #     assert ms.get_min() == 5
    #
    #     print("  MinStack tracks minimum correctly")
    #     print("Test 6 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 6 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 6 ERROR: {e}")

    # print("\n=== Test 7: MinStack - Duplicates ===")
    # try:
    #     ms = MinStack()
    #     ms.push(2)
    #     ms.push(2)
    #     ms.push(1)
    #     ms.push(1)
    #
    #     assert ms.get_min() == 1
    #     ms.pop()
    #     assert ms.get_min() == 1  # Still 1 (duplicate)
    #     ms.pop()
    #     assert ms.get_min() == 2
    #     ms.pop()
    #     assert ms.get_min() == 2  # Still 2 (duplicate)
    #
    #     print("  MinStack handles duplicates correctly")
    #     print("Test 7 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 7 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 7 ERROR: {e}")

    print("\n" + "=" * 60)
    print("STACK KEY LESSONS")
    print("=" * 60)
    print("""
1. LIFO: Last In, First Out
2. All core operations are O(1)
3. Use a list internally - append() is push, pop() is pop
4. Stacks are everywhere: undo, browser history, recursion
5. Bracket matching is the classic stack problem
""")
    print("=" * 60)
