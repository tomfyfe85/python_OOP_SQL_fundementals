"""
DSA Course - Module 10: Recursion & Backtracking
================================================

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

======================================
BACKTRACKING PATTERN
======================================
Backtracking = recursion + "undo" step. Build a solution incrementally,
abandon it when it can't lead to a valid solution, and try another path.

THE TEMPLATE:
    def backtrack(current_state, choices):
        if is_solution(current_state):
            save_solution(current_state)
            return

        for choice in choices:
            if is_valid(choice):
                make_choice(choice)        # DO
                backtrack(new_state)       # RECURSE
                undo_choice(choice)        # UNDO (backtrack!)

USE CASES:
- Generating permutations / combinations / subsets
- N-Queens problem
- Sudoku solver
- Path finding with constraints
- Word search in grid

THE KEY INSIGHT:
Backtracking explores a decision tree. Each node is a partial solution.
We go deep (make choices) until we hit a dead end or solution,
then backtrack (undo) to try other branches.
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

Implement the function below:
"""


def power(x: float, n: int) -> float:
    """Calculate x raised to power n."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 3: Generate All Subsets (Backtracking)
# ============================================

"""
PROBLEM: Generate all possible subsets of a list of unique integers.

Given a list of distinct integers, return all possible subsets (power set).
The solution must not contain duplicate subsets.

Examples:
- [1, 2, 3] -> [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
- [0] -> [[], [0]]
- [] -> [[]]

Implement the function below:
"""


def subsets(nums: list[int]) -> list[list[int]]:
    """Return all possible subsets of nums."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 4: Generate Permutations (Backtracking)
# ============================================

"""
PROBLEM: Generate all permutations of a list of unique integers.

Given a list of distinct integers, return all possible orderings.

Examples:
- [1, 2, 3] -> [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
- [0, 1] -> [[0,1], [1,0]]
- [1] -> [[1]]

Implement the function below:
"""


def permutations(nums: list[int]) -> list[list[int]]:
    """Return all permutations of nums."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 5: Combination Sum (Backtracking)
# ============================================

"""
PROBLEM: Find all unique combinations that sum to target.

Given an array of distinct integers and a target, find all unique
combinations where the chosen numbers sum to target.
The same number may be used unlimited times.

Examples:
- candidates=[2,3,6,7], target=7 -> [[2,2,3], [7]]
  2+2+3=7, 7=7
- candidates=[2,3,5], target=8 -> [[2,2,2,2], [2,3,3], [3,5]]
- candidates=[2], target=1 -> [] (no way to make 1)

Implement the function below:
"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """Return all combinations of candidates that sum to target."""
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

    # Test Question 3
    print("\n--- Question 3: Subsets (Backtracking) ---")
    try:
        result = subsets([1, 2, 3])
        expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
        assert sorted([sorted(s) for s in result]) == sorted([sorted(s) for s in expected])
        assert subsets([0]) == [[], [0]] or sorted([sorted(s) for s in subsets([0])]) == [[], [0]]
        assert subsets([]) == [[]]
        print("All Question 3 tests PASSED!")
    except AssertionError as e:
        print(f"Question 3 FAILED: {e}")
    except Exception as e:
        print(f"Question 3 ERROR: {e}")

    # Test Question 4
    print("\n--- Question 4: Permutations (Backtracking) ---")
    try:
        result = permutations([1, 2, 3])
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        assert sorted(result) == sorted(expected), "3 elements"
        assert sorted(permutations([1, 2])) == sorted([[1, 2], [2, 1]]), "2 elements"
        assert permutations([1]) == [[1]], "1 element"
        print("All Question 4 tests PASSED!")
    except AssertionError as e:
        print(f"Question 4 FAILED: {e}")
    except Exception as e:
        print(f"Question 4 ERROR: {e}")

    # Test Question 5
    print("\n--- Question 5: Combination Sum (Backtracking) ---")
    try:
        result = combination_sum([2, 3, 6, 7], 7)
        expected = [[2, 2, 3], [7]]
        assert sorted([sorted(c) for c in result]) == sorted([sorted(c) for c in expected])

        result2 = combination_sum([2, 3, 5], 8)
        expected2 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        assert sorted([sorted(c) for c in result2]) == sorted([sorted(c) for c in expected2])

        assert combination_sum([2], 1) == []

        # Edge cases
        result3 = combination_sum([1], 3)
        assert [1, 1, 1] in result3, "Single coin repeated"

        print("All Question 5 tests PASSED!")
    except AssertionError as e:
        print(f"Question 5 FAILED: {e}")
    except Exception as e:
        print(f"Question 5 ERROR: {e}")

    # ==========================================
    # REVISION: Module 10 (Binary Search)
    # ==========================================
    print("\n--- REVISION: Binary Search ---")
    print("Q: What's the time complexity of binary search and why?")
    print("A: O(log n) - each step eliminates half the remaining elements.")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Every recursion needs: BASE CASE + RECURSIVE CASE
2. Base case: simplest version (empty, single element, n=0)
3. Recursive case: reduce problem, assume recursion works
4. BACKTRACKING: make choice -> recurse -> undo choice
5. Backtracking explores decision trees by trying all paths
6. Common patterns: subsets (include/exclude), permutations (all orderings)
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
