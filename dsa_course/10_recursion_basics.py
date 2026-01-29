"""
DSA Course - Module 10: Recursion Basics
========================================

CONCEPT: Recursion
------------------
A function that calls itself to solve smaller versions of the same problem.

THE TWO ESSENTIAL PARTS:
1. BASE CASE: When to stop (prevents infinite recursion)
2. RECURSIVE CASE: How to break down the problem

HOW TO THINK RECURSIVELY:
1. What's the simplest case? (base case)
2. How can I reduce the problem by one step?
3. Assume the recursive call works - how do I use its result?

COMMON MISTAKES:
- Forgetting the base case (infinite recursion!)
- Base case doesn't cover all stopping conditions
- Not making progress toward base case

WHEN TO USE RECURSION:
- Problem has smaller subproblems of same type
- Tree/graph traversal
- Divide and conquer algorithms
- When the recursive solution is cleaner than iterative
"""


# ============================================
# EXAMPLE: Sum of Array (Recursively)
# ============================================

def sum_array_example(nums: list[int]) -> int:
    """
    Calculate sum of all elements using recursion.

    Thinking process:
    - Base case: empty array has sum 0
    - Recursive case: sum = first element + sum of rest

    sum([1,2,3,4]) = 1 + sum([2,3,4])
                   = 1 + 2 + sum([3,4])
                   = 1 + 2 + 3 + sum([4])
                   = 1 + 2 + 3 + 4 + sum([])
                   = 1 + 2 + 3 + 4 + 0
                   = 10
    """
    # Base case: empty array
    if not nums:
        return 0

    # Recursive case: first element + sum of rest
    return nums[0] + sum_array_example(nums[1:])


def sum_array_with_index(nums: list[int], index: int = 0) -> int:
    """
    Same thing, but using an index instead of slicing.
    More efficient - doesn't create new lists.
    """
    # Base case: index past end of array
    if index >= len(nums):
        return 0

    # Recursive case: current element + sum of rest
    return nums[index] + sum_array_with_index(nums, index + 1)


# Let's trace sum_array_example([1, 2, 3]):
#
# sum_array_example([1, 2, 3])
#   -> 1 + sum_array_example([2, 3])
#        -> 2 + sum_array_example([3])
#             -> 3 + sum_array_example([])
#                  -> return 0  (base case)
#             -> return 3 + 0 = 3
#        -> return 2 + 3 = 5
#   -> return 1 + 5 = 6


# ============================================
# QUESTION 1: Reverse String Recursively
# ============================================

"""
PROBLEM: Reverse a string using recursion.

Examples:
- "hello" -> "olleh"
- "a" -> "a"
- "" -> ""

HINT: Think about it this way:
      reverse("hello") = reverse("ello") + "h"
                       = reverse("llo") + "e" + "h"
                       = reverse("lo") + "l" + "e" + "h"
                       = reverse("o") + "l" + "l" + "e" + "h"
                       = "o" + "l" + "l" + "e" + "h"
                       = "olleh"

      Base case: empty string or single character
      Recursive case: reverse the rest, then add first character at end

Implement the function below:
"""


def reverse_string_recursive(s: str) -> str:
    """Reverse the string using recursion."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2: Power Function
# ============================================

"""
PROBLEM: Calculate x raised to power n (x^n) using recursion.

Handle these cases:
- Positive n: x^n = x * x^(n-1)
- n = 0: x^0 = 1
- Negative n: x^(-n) = 1 / x^n

Examples:
- power(2, 3) -> 8 (2*2*2)
- power(2, 0) -> 1
- power(2, -2) -> 0.25 (1/4)
- power(5, 1) -> 5

HINT:
      Base case: n == 0 -> return 1
      Recursive case: x * power(x, n-1)
      Handle negative: if n < 0, return 1 / power(x, -n)

BONUS (optional): Can you make it faster?
      x^8 = (x^4)^2 = ((x^2)^2)^2
      Instead of 8 multiplications, only 3!
      If n is even: power(x, n) = power(x*x, n//2)
      If n is odd: power(x, n) = x * power(x, n-1)

Implement the function below:
"""


def power(x: float, n: int) -> float:
    """Calculate x raised to power n."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 10: Recursion Basics")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Sum Array ---")
    assert sum_array_example([1, 2, 3, 4]) == 10
    assert sum_array_example([]) == 0
    assert sum_array_example([5]) == 5
    assert sum_array_with_index([1, 2, 3, 4]) == 10
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Reverse String ---")
    try:
        assert reverse_string_recursive("hello") == "olleh", "Basic case"
        assert reverse_string_recursive("a") == "a", "Single char"
        assert reverse_string_recursive("") == "", "Empty string"
        assert reverse_string_recursive("ab") == "ba", "Two chars"
        assert reverse_string_recursive("racecar") == "racecar", "Palindrome"
        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: Power Function ---")
    try:
        assert power(2, 3) == 8, "2^3"
        assert power(2, 0) == 1, "x^0 = 1"
        assert power(5, 1) == 5, "x^1 = x"
        assert abs(power(2, -2) - 0.25) < 0.0001, "2^-2 = 0.25"
        assert power(3, 4) == 81, "3^4"
        assert abs(power(2.5, 2) - 6.25) < 0.0001, "Float base"
        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Every recursion needs: BASE CASE + RECURSIVE CASE
2. Base case: simplest version (empty, single element, n=0)
3. Recursive case: reduce problem, assume recursion works
4. Trust the recursion - don't try to trace every call mentally
5. Watch for: missing base case, not making progress toward base
""")


# ============================================
# BONUS: Visualizing Recursion
# ============================================

def factorial_traced(n: int, depth: int = 0) -> int:
    """Factorial with tracing to see recursion in action."""
    indent = "  " * depth
    print(f"{indent}factorial({n})")

    if n <= 1:
        print(f"{indent}-> returns 1 (base case)")
        return 1

    result = n * factorial_traced(n - 1, depth + 1)
    print(f"{indent}-> returns {n} * ... = {result}")
    return result


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("BONUS: Tracing Recursion")
    print("=" * 60)
    print("\nfactorial(5) traced:")
    print("-" * 40)
    factorial_traced(5)
