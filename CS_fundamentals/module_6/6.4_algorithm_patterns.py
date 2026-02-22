"""
Exercise 6.4: Algorithm Patterns

ALGORITHM PATTERNS
==================

Many problems share common solution patterns. Once you recognise the
pattern, you can apply a known approach instead of starting from scratch.

This module covers three foundational patterns:
1. Two Pointers
2. Sliding Window
3. Divide and Conquer

===================================
PATTERN 1: TWO POINTERS
===================================

Use two pointers that move through the data, typically:
- One from each end (converging)
- One slow, one fast (same direction)

When to use: sorted arrays, finding pairs, palindromes

Example: Find a pair in sorted array that sums to target
    left = 0, right = len-1
    If sum too small: move left right
    If sum too big: move right left

===================================
PATTERN 2: SLIDING WINDOW
===================================

Maintain a "window" (subarray/substring) that slides through the data.
Efficient for finding subarrays/substrings with certain properties.

When to use: contiguous subarray problems, "find maximum/minimum of size k"

Example: Maximum sum of k consecutive elements
    Start with sum of first k elements
    Slide: add next element, remove first element of previous window

===================================
PATTERN 3: DIVIDE AND CONQUER
===================================

Break problem into smaller subproblems, solve them, combine results.

When to use: problem can be split into independent subproblems

You already used this in merge sort!
    Split -> Solve halves -> Merge results

===================================
EXERCISE
===================================

PART 1: Two Pointer Problems

    def two_sum_sorted(arr: list[int], target: int) -> tuple[int, int] | None:
        Given a SORTED array and target, return indices of two numbers
        that add up to target. Return None if no pair exists.
        Use two pointers (not a hash map).
        Example: [1, 3, 5, 7, 11], target=10 -> (1, 3) because 3+7=10

    def remove_duplicates(arr: list[int]) -> list[int]:
        Given a SORTED array, return a new list with duplicates removed.
        Use two pointers: one for reading, one for writing position.
        Example: [1, 1, 2, 2, 3, 4, 4] -> [1, 2, 3, 4]

---

PART 2: Sliding Window Problems

    def max_sum_subarray(arr: list[int], k: int) -> int | None:
        Return the maximum sum of any k consecutive elements.
        Return None if array has fewer than k elements.
        Example: [2, 1, 5, 1, 3, 2], k=3 -> 9 (5+1+3)

    def longest_unique_substring(s: str) -> int:
        Return the LENGTH of the longest substring without repeating characters.
        Example: "abcabcbb" -> 3 ("abc")
        Example: "bbbbb" -> 1 ("b")
        Example: "pwwkew" -> 3 ("wke")
        Hint: Use a sliding window with a set to track characters in the window.

---

PART 3 (HARD): Divide and Conquer

    def max_subarray(arr: list[int]) -> int:
        Find the contiguous subarray with the largest sum (Kadane's Algorithm).
        Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6 (subarray [4, -1, 2, 1])

        This can be solved with divide and conquer OR Kadane's algorithm.
        Kadane's is simpler:
        - Track current_sum and max_sum
        - At each element: current_sum = max(element, current_sum + element)
        - Update max_sum if current_sum is larger

ESTIMATED TIME: 45-60 minutes
"""


# ============================================
# PART 1: Two Pointer Problems
# ============================================

def two_sum_sorted(arr: list[int], target: int) -> tuple[int, int] | None:
    """Return indices of two numbers in sorted arr that sum to target."""
    # YOUR CODE HERE
    pass


def remove_duplicates(arr: list[int]) -> list[int]:
    """Return new list with duplicates removed from sorted array."""
    # YOUR CODE HERE
    pass


# ============================================
# PART 2: Sliding Window Problems
# ============================================

def max_sum_subarray(arr: list[int], k: int) -> int | None:
    """Return max sum of k consecutive elements."""
    # YOUR CODE HERE
    pass


def longest_unique_substring(s: str) -> int:
    """Return length of longest substring without repeating characters."""
    # YOUR CODE HERE
    pass


# ============================================
# PART 3 (HARD): Kadane's Algorithm
# ============================================

def max_subarray(arr: list[int]) -> int:
    """Return the largest sum of any contiguous subarray."""
    # YOUR CODE HERE
    pass


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    # ==========================================
    # PART 1 TESTS: Two Pointers
    # ==========================================
    print("\n=== Test 1: Two Sum Sorted ===")
    try:
        assert two_sum_sorted([1, 3, 5, 7, 11], 10) == (1, 3)
        assert two_sum_sorted([1, 2, 3, 4, 5], 9) == (3, 4)
        assert two_sum_sorted([1, 2, 3, 4, 5], 3) == (0, 1)
        assert two_sum_sorted([1, 2, 3], 10) is None
        assert two_sum_sorted([], 5) is None
        assert two_sum_sorted([1, 2], 3) == (0, 1)

        print("  Two sum on sorted array works")
        print("Test 1 PASSED!")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")
    except Exception as e:
        print(f"Test 1 ERROR: {e}")

    print("\n=== Test 2: Remove Duplicates ===")
    try:
        assert remove_duplicates([1, 1, 2, 2, 3, 4, 4]) == [1, 2, 3, 4]
        assert remove_duplicates([1, 1, 1, 1]) == [1]
        assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
        assert remove_duplicates([]) == []
        assert remove_duplicates([5]) == [5]

        print("  Remove duplicates works")
        print("Test 2 PASSED!")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 ERROR: {e}")

    # ==========================================
    # PART 2 TESTS: Sliding Window
    # ==========================================
    print("\n=== Test 3: Max Sum Subarray of Size K ===")
    try:
        assert max_sum_subarray([2, 1, 5, 1, 3, 2], 3) == 9
        assert max_sum_subarray([2, 3, 4, 1, 5], 2) == 7
        assert max_sum_subarray([1, 2, 3], 3) == 6
        assert max_sum_subarray([1, 2], 3) is None
        assert max_sum_subarray([], 1) is None
        assert max_sum_subarray([5], 1) == 5

        print("  Max sum subarray works")
        print("Test 3 PASSED!")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 ERROR: {e}")

    print("\n=== Test 4: Longest Unique Substring ===")
    try:
        assert longest_unique_substring("abcabcbb") == 3
        assert longest_unique_substring("bbbbb") == 1
        assert longest_unique_substring("pwwkew") == 3
        assert longest_unique_substring("") == 0
        assert longest_unique_substring("a") == 1
        assert longest_unique_substring("abcdef") == 6
        assert longest_unique_substring("aab") == 2

        print("  Longest unique substring works")
        print("Test 4 PASSED!")
    except AssertionError as e:
        print(f"Test 4 FAILED: {e}")
    except Exception as e:
        print(f"Test 4 ERROR: {e}")

    # ==========================================
    # PART 3 TESTS (HARD): Uncomment when ready
    # ==========================================

    # print("\n=== Test 5: Max Subarray (Kadane's) ===")
    # try:
    #     assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    #     assert max_subarray([1, 2, 3, 4]) == 10
    #     assert max_subarray([-1, -2, -3]) == -1  # Least negative
    #     assert max_subarray([5]) == 5
    #     assert max_subarray([-1, 2, 3, -5, 4]) == 5
    #
    #     print("  Kadane's algorithm works")
    #     print("Test 5 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 5 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 5 ERROR: {e}")

    print("\n" + "=" * 60)
    print("ALGORITHM PATTERNS KEY LESSONS")
    print("=" * 60)
    print("""
1. TWO POINTERS: Converging pointers on sorted data -> O(n)
   - Two sum, palindromes, removing duplicates

2. SLIDING WINDOW: Fixed or variable size window -> O(n)
   - Max sum of k elements, longest substring without repeats

3. DIVIDE AND CONQUER: Split, solve, combine
   - Merge sort, binary search, max subarray

4. KADANE'S ALGORITHM: Track running max -> O(n)
   - Maximum subarray sum

5. Recognising the PATTERN is half the battle!
""")
    print("=" * 60)
