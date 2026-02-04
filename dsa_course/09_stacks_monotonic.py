"""
DSA Course - Module 8: Stacks & Monotonic Stacks
================================================

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

======================================
MONOTONIC STACK PATTERN
======================================
A monotonic stack maintains elements in sorted order (increasing or decreasing).
When adding a new element, we pop all elements that violate the order.

USE CASES:
- Next Greater Element (decreasing stack)
- Next Smaller Element (increasing stack)
- Stock Span problems
- Daily Temperatures
- Largest Rectangle in Histogram

THE PATTERN:
    for i, num in enumerate(arr):
        while stack and violates_order(stack[-1], num):
            popped = stack.pop()
            # Process popped element - we found its answer!
        stack.append(num)  # or (num, i) if we need indices

WHY IT WORKS:
- Elements stay in stack until we find their "answer"
- When we pop, we've found the first element that beats it
- O(n) because each element is pushed and popped at most once
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
# QUESTION 3: Daily Temperatures (LeetCode 739)
# ============================================

"""
PROBLEM: How many days until warmer temperature?

Given an array of daily temperatures, return an array where answer[i]
is the number of days you have to wait after day i to get a warmer
temperature. If there's no future warmer day, use 0.

Examples:
- [73, 74, 75, 71, 69, 72, 76, 73] -> [1, 1, 4, 2, 1, 1, 0, 0]
  Day 0 (73): next warmer is day 1 (74), wait 1 day
  Day 1 (74): next warmer is day 2 (75), wait 1 day
  Day 2 (75): next warmer is day 6 (76), wait 4 days
  Day 3 (71): next warmer is day 5 (72), wait 2 days
  ...

- [30, 40, 50, 60] -> [1, 1, 1, 0]

- [30, 20, 10] -> [0, 0, 0] (temperatures only decrease)

HINT: This is a monotonic stack problem!
      - Stack stores INDICES (not values) of days waiting for answer
      - Process left to right
      - When current temp > temp at stack top, we found the answer
        for that day: days waited = current index - stored index
      - Pop and record answer, then push current index

      Stack maintains indices of decreasing temperatures.

Implement the function below:
"""


def daily_temperatures(temperatures: list[int]) -> list[int]:
    """Return days until warmer temperature for each day."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 4: Stock Span Problem
# ============================================

"""
PROBLEM: Calculate the stock span for each day.

The span of a stock's price on a given day is the maximum number of
consecutive days (including today) the price has been <= today's price.

In other words: looking backwards, how many consecutive days had
price <= today's price?

Examples:
- [100, 80, 60, 70, 60, 75, 85] -> [1, 1, 1, 2, 1, 4, 6]
  Day 0 (100): no previous days, span = 1
  Day 1 (80): 80 < 100, can't look back, span = 1
  Day 2 (60): 60 < 80, span = 1
  Day 3 (70): 70 > 60, so day 2 counts. 70 < 80, stop. span = 2
  Day 4 (60): 60 < 70, span = 1
  Day 5 (75): 75 > 60, 75 > 70, 75 > 60, 75 < 80. span = 4 (days 2,3,4,5)
  Day 6 (85): 85 > 75, 85 > 80, 85 < 100. span = 6 (days 1-6)

HINT: Use a stack of (price, index) pairs.
      - For each day, pop while stack top price <= current price
      - Span = current_index - index_of_last_higher_price
      - If stack empty, all previous days were lower -> span = i + 1

Implement the function below:
"""


def stock_span(prices: list[int]) -> list[int]:
    """Return the span for each day's stock price."""
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

    # Test Question 3
    print("\n--- Question 3: Daily Temperatures ---")
    try:
        assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
        assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
        assert daily_temperatures([30, 20, 10]) == [0, 0, 0]
        assert daily_temperatures([50]) == [0]
        assert daily_temperatures([50, 50, 50]) == [0, 0, 0]
        print("All Question 3 tests PASSED!")
    except AssertionError as e:
        print(f"Question 3 FAILED: {e}")
    except Exception as e:
        print(f"Question 3 ERROR: {e}")

    # Test Question 4
    print("\n--- Question 4: Stock Span ---")
    try:
        assert stock_span([100, 80, 60, 70, 60, 75, 85]) == [1, 1, 1, 2, 1, 4, 6]
        assert stock_span([10, 20, 30, 40]) == [1, 2, 3, 4]
        assert stock_span([40, 30, 20, 10]) == [1, 1, 1, 1]
        assert stock_span([100]) == [1]
        assert stock_span([10, 10, 10]) == [1, 2, 3]
        print("All Question 4 tests PASSED!")
    except AssertionError as e:
        print(f"Question 4 FAILED: {e}")
    except Exception as e:
        print(f"Question 4 ERROR: {e}")

    # ==========================================
    # REVISION: Module 8 (Prefix Sum)
    # ==========================================
    print("\n--- REVISION: Prefix Sum ---")
    print("Q: How do you get the sum of elements from index i to j using prefix sums?")
    print("A: sum(i to j) = prefix[j+1] - prefix[i]")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Stack = LIFO (Last In, First Out)
2. In Python: list with append() and pop()
3. Use for matching/pairing problems
4. MONOTONIC STACK: maintains sorted order, O(n) for "next greater/smaller"
5. Pattern: pop elements that current element "defeats", then push current
6. Store indices when you need positions, values when you need comparisons
""")
