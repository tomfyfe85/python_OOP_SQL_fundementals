"""
DSA Course - Module 8: Stack Basics
===================================

CONCEPT: Stack Data Structure
-----------------------------
A stack is LIFO: Last In, First Out.
Think of a stack of plates: you add to top, remove from top.

OPERATIONS (all O(1)):
- push(x): add x to top
- pop(): remove and return top
- peek()/top(): return top without removing
- isEmpty(): check if stack is empty

IN PYTHON:
Use a list! append() = push, pop() = pop

WHEN TO USE STACKS:
- Matching pairs (brackets, tags)
- Undo operations
- Parsing expressions
- Tracking "most recent" item
- Converting recursion to iteration

THE KEY INSIGHT:
When you need to remember something and come back to it later
in REVERSE order, use a stack.
"""


# ============================================
# EXAMPLE: Valid Parentheses
# ============================================

def is_valid_parentheses_example(s: str) -> bool:
    """
    Check if parentheses are valid: properly opened and closed.

    Valid: "()", "()[]{}", "([])"
    Invalid: "(]", "([)]", "((("

    Strategy:
    - When we see opening bracket, push it
    - When we see closing bracket, pop and check it matches
    - At end, stack should be empty (all matched)
    """
    stack = []
    # Map closing brackets to their opening counterpart
    matches = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            # Opening bracket: push to stack
            stack.append(char)
        elif char in ')]}':
            # Closing bracket: check for match
            if not stack:
                # Nothing to match with
                return False
            if stack.pop() != matches[char]:
                # Doesn't match most recent opening
                return False

    # Valid only if all brackets were matched
    return len(stack) == 0


# Let's trace through: "([])"
#
# char='(': opening, push -> stack=['(']
# char='[': opening, push -> stack=['(', '[']
# char=']': closing, pop '[', matches[']']='[' -> match! stack=['(']
# char=')': closing, pop '(', matches[')']='(' -> match! stack=[]
# End: stack empty -> return True
#
# Let's trace through: "([)]"
#
# char='(': push -> stack=['(']
# char='[': push -> stack=['(', '[']
# char=')': pop '[', matches[')']='(' -> '[' != '(' -> return False


# ============================================
# QUESTION 1: Remove Adjacent Duplicates
# ============================================

"""
PROBLEM: Remove all adjacent duplicates in a string.

Repeatedly remove pairs of adjacent equal characters until no more
pairs exist. Return the final string.

Examples:
- "abbaca" -> "ca"
  Remove "bb" -> "aaca"
  Remove "aa" -> "ca"

- "azxxzy" -> "ay"
  Remove "xx" -> "azzy"
  Remove "zz" -> "ay"

HINT: Use a stack!
      - For each character, if it equals stack top, pop (they cancel)
      - Otherwise, push it
      - At end, stack contains remaining characters

Implement the function below:
"""


def remove_duplicates(s: str) -> str:
    """Remove all adjacent duplicate pairs."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2: Next Greater Element
# ============================================

"""
PROBLEM: For each element, find the next greater element to its right.

Given an array, for each element find the next element to its right
that is greater. If none exists, use -1.

Examples:
- [4, 5, 2, 25] -> [5, 25, 25, -1]
  4 -> next greater is 5
  5 -> next greater is 25
  2 -> next greater is 25
  25 -> no greater element, so -1

- [13, 7, 6, 12] -> [-1, 12, 12, -1]
  13 -> no greater element
  7 -> next greater is 12
  6 -> next greater is 12
  12 -> no greater element

HINT: Process from RIGHT to LEFT, maintain stack of "candidates".
      - Stack holds elements that could be "next greater" for future elements
      - For current element, pop stack until we find something greater
      - Whatever remains on top is our answer (or -1 if empty)
      - Push current element for future use

      The stack maintains elements in decreasing order (monotonic stack).

Implement the function below:
"""


def next_greater_element(nums: list[int]) -> list[int]:
    """Return array where result[i] is next greater element after nums[i]."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 8: Stack Basics")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Valid Parentheses ---")
    assert is_valid_parentheses_example("()") == True
    assert is_valid_parentheses_example("()[]{}") == True
    assert is_valid_parentheses_example("(]") == False
    assert is_valid_parentheses_example("([)]") == False
    assert is_valid_parentheses_example("{[]}") == True
    assert is_valid_parentheses_example("((()") == False
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Remove Adjacent Duplicates ---")
    try:
        assert remove_duplicates("abbaca") == "ca", "Basic case"
        assert remove_duplicates("azxxzy") == "ay", "Middle removal"
        assert remove_duplicates("aaa") == "a", "Odd duplicates"
        assert remove_duplicates("aa") == "", "All removed"
        assert remove_duplicates("abc") == "abc", "No duplicates"
        assert remove_duplicates("") == "", "Empty string"
        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: Next Greater Element ---")
    try:
        assert next_greater_element([4, 5, 2, 25]) == [5, 25, 25, -1]
        assert next_greater_element([13, 7, 6, 12]) == [-1, 12, 12, -1]
        assert next_greater_element([1, 2, 3, 4]) == [2, 3, 4, -1]
        assert next_greater_element([4, 3, 2, 1]) == [-1, -1, -1, -1]
        assert next_greater_element([1]) == [-1]
        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Stack = LIFO (Last In, First Out)
2. In Python: list with append() and pop()
3. Use for matching/pairing problems
4. Use for "next greater/smaller" problems (monotonic stack)
5. Key question: "Do I need to remember and return in reverse order?"
""")
