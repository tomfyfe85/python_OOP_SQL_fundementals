"""
DSA Course - Module 9: Binary Search
====================================

CONCEPT: Binary Search
----------------------
Find an element in a SORTED array by repeatedly halving the search space.
Instead of checking every element O(n), we eliminate half each time O(log n).

THE ALGORITHM:
1. Look at middle element
2. If target found, done!
3. If target < middle, search left half
4. If target > middle, search right half
5. Repeat until found or search space is empty

TIME COMPLEXITY: O(log n)
- Each step eliminates half the remaining elements
- 1000 elements -> ~10 steps
- 1,000,000 elements -> ~20 steps

REQUIREMENTS:
- Array MUST be sorted
- Random access (can jump to any index in O(1))

COMMON VARIATIONS:
- Find exact value
- Find insertion point
- Find first/last occurrence
- Find closest value
"""


# ============================================
# EXAMPLE: Basic Binary Search
# ============================================

def binary_search_example(nums: list[int], target: int) -> int:
    """
    Find index of target in sorted array. Return -1 if not found.

    Strategy:
    - Maintain search space with left and right pointers
    - Calculate middle
    - Narrow search space based on comparison
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2  # Integer division

        if nums[mid] == target:
            return mid  # Found it!
        elif nums[mid] < target:
            left = mid + 1  # Target is in right half
        else:
            right = mid - 1  # Target is in left half

    return -1  # Not found


# Let's trace through: nums=[1, 3, 5, 7, 9, 11, 13], target=7
#
# left=0, right=6
# mid=3, nums[3]=7 -> Found! Return 3
#
# Let's trace through: nums=[1, 3, 5, 7, 9, 11, 13], target=6
#
# left=0, right=6
# mid=3, nums[3]=7, 7 > 6 -> right=2
#
# left=0, right=2
# mid=1, nums[1]=3, 3 < 6 -> left=2
#
# left=2, right=2
# mid=2, nums[2]=5, 5 < 6 -> left=3
#
# left=3, right=2 -> left > right, stop
# Return -1 (not found)


# ============================================
# QUESTION 1: Search Insert Position
# ============================================

"""
PROBLEM: Find the index where target should be inserted.

Given a sorted array and a target, return the index if found.
If not found, return the index where it would be inserted in order.

Examples:
- nums=[1,3,5,6], target=5 -> 2 (found at index 2)
- nums=[1,3,5,6], target=2 -> 1 (would insert at index 1)
- nums=[1,3,5,6], target=7 -> 4 (would insert at end)
- nums=[1,3,5,6], target=0 -> 0 (would insert at beginning)

HINT: This is binary search with a twist.
      - If found, return the index
      - If not found, `left` will be at the insertion point

      Think about it: when we stop, left > right.
      `left` is where the target should go.

Implement the function below:
"""


def search_insert(nums: list[int], target: int) -> int:
    """Return index of target, or where it should be inserted."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2: First Bad Version
# ============================================

"""
PROBLEM: Find the first bad version in a sequence.

You have versions 1 to n. One version is bad, and all versions after
it are also bad. Find the FIRST bad version.

You're given a function is_bad_version(version) that returns True/False.
Minimize the number of calls to is_bad_version.

Examples:
- n=5, bad=4 means versions [1,2,3] are good, [4,5] are bad -> return 4
- n=1, bad=1 means version 1 is bad -> return 1

HINT: Binary search! The versions are "sorted" in a sense:
      [good, good, good, bad, bad, bad]

      We want to find the first "bad" (the boundary).
      - If mid is bad, first bad could be mid or earlier -> right = mid
      - If mid is good, first bad is definitely later -> left = mid + 1

      Note: Use right = mid (not mid-1) because mid could BE the first bad.

Implement the function below:
"""

# This simulates the is_bad_version API - don't modify
_bad_version = 4  # Default for testing


def is_bad_version(version: int) -> bool:
    """Returns True if version is bad. (API provided by problem)"""
    return version >= _bad_version


def first_bad_version(n: int) -> int:
    """Return the first bad version (1-indexed)."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 9: Binary Search")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Basic Binary Search ---")
    assert binary_search_example([1, 3, 5, 7, 9, 11, 13], 7) == 3
    assert binary_search_example([1, 3, 5, 7, 9, 11, 13], 1) == 0
    assert binary_search_example([1, 3, 5, 7, 9, 11, 13], 13) == 6
    assert binary_search_example([1, 3, 5, 7, 9, 11, 13], 6) == -1
    assert binary_search_example([], 5) == -1
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Search Insert Position ---")
    try:
        assert search_insert([1, 3, 5, 6], 5) == 2, "Found"
        assert search_insert([1, 3, 5, 6], 2) == 1, "Insert middle"
        assert search_insert([1, 3, 5, 6], 7) == 4, "Insert end"
        assert search_insert([1, 3, 5, 6], 0) == 0, "Insert beginning"
        assert search_insert([1], 0) == 0, "Single element, insert before"
        assert search_insert([1], 2) == 1, "Single element, insert after"
        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: First Bad Version ---")
    global _bad_version
    try:
        _bad_version = 4
        assert first_bad_version(5) == 4, "Bad at 4"

        _bad_version = 1
        assert first_bad_version(1) == 1, "First is bad"

        _bad_version = 1
        assert first_bad_version(5) == 1, "All bad"

        _bad_version = 5
        assert first_bad_version(5) == 5, "Only last is bad"

        _bad_version = 50
        assert first_bad_version(100) == 50, "Larger n"

        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    # ==========================================
    # REVISION: Module 9 (Stacks)
    # ==========================================
    print("\n--- REVISION: Stacks ---")
    print("Q: What's a monotonic stack and when would you use it?")
    print("A: A stack that maintains sorted order. Use for 'next greater/smaller element' problems.")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Binary search: O(log n) - eliminates half each step
2. REQUIRES sorted data
3. Template: while left <= right, narrow with mid +/- 1
4. Watch for: off-by-one errors, infinite loops
5. Variations: find insertion point, find boundary, find first/last
""")
