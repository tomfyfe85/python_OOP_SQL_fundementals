"""
DSA Course - Module 2: Hash Maps & Sets
=======================================

CONCEPT: Hash-Based Data Structures
-----------------------------------
Hash maps (dict) and sets provide O(1) average lookup time.
This is THE most important optimization in DSA.

LISTS vs SETS vs DICTS:
- list: O(n) to check "is x in list?"
- set: O(1) to check "is x in set?"
- dict: O(1) to check "is key in dict?" AND store associated value

WHEN TO USE SETS:
- Need to check membership: "Have I seen this before?"
- Need unique elements only
- Need to find duplicates

WHEN TO USE DICTS:
- Need to count occurrences
- Need to map values to other values
- Need to store extra info about elements

THE BIG INSIGHT:
If you're checking "if x in list" inside a loop, you probably
want a set instead. This turns O(n^2) into O(n).
"""


# ============================================
# EXAMPLE: Two Sum (Classic LeetCode #1)
# ============================================

def two_sum_example(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers that add up to target. Return their indices.

    Brute force: Check every pair - O(n^2)
    Hash map: For each num, check if (target - num) exists - O(n)

    Strategy:
    - For each number, we need to find if its "complement" exists
    - complement = target - current_number
    - Store numbers we've seen in a dict: {value: index}
    """
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            # Found it! Return both indices
            return [seen[complement], i]

        # Haven't found pair yet, store this number
        seen[num] = i

    return []  # No solution found


# Let's trace through: nums=[2, 7, 11, 15], target=9
#
# i=0, num=2: complement=7, seen={}, 7 not in seen, seen={2:0}
# i=1, num=7: complement=2, seen={2:0}, 2 IS in seen! Return [0, 1]
#
# Why this works:
# - We need two numbers that sum to 9
# - When we see 7, we ask "is there a number that adds to 9?"
# - That number is 9-7=2
# - We check if 2 was seen before -> YES at index 0


# ============================================
# QUESTION 1: Contains Duplicate
# ============================================

"""
PROBLEM: Check if array contains any duplicate.

Given an array of integers, return True if any value appears
at least twice, return False if every element is distinct.

Examples:
- [1, 2, 3, 1] -> True (1 appears twice)
- [1, 2, 3, 4] -> False (all distinct)
- [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] -> True (many duplicates)

HINT: Use a set to track what you've seen.
      If you try to add something already in the set, it's a duplicate.

      OR: Compare len(nums) with len(set(nums))

Implement the function below:
"""


def contains_duplicate(nums: list[int]) -> bool:
    """Return True if any element appears more than once."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2: First Unique Character
# ============================================

"""
PROBLEM: Find the first non-repeating character in a string.

Given a string, return the INDEX of the first character that
doesn't repeat. If no such character exists, return -1.

Examples:
- "leetcode" -> 0 (l appears only once, it's at index 0)
- "loveleetcode" -> 2 (v appears only once, it's at index 2)
- "aabb" -> -1 (all characters repeat)

HINT: Two-pass approach:
      1. First pass: count frequency of each character (use dict)
      2. Second pass: find first char with count == 1

Implement the function below:
"""


def first_unique_char(s: str) -> int:
    """Return index of first non-repeating character, or -1."""
    # YOUR CODE HERE
    pass


# ============================================
# REVISION: Quick Review from Module 1
# ============================================

"""
REVISION: Find the minimum element in an array.

This is a quick refresher on array iteration from Module 1.
Solve it WITHOUT using Python's built-in min() function.

Example: [3, 1, 4, 1, 5] -> 1
"""


def revision_find_min(nums: list[int]) -> int:
    """Return the minimum element in the array."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 2: Hash Maps & Sets")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Two Sum ---")
    assert two_sum_example([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum_example([3, 2, 4], 6) == [1, 2]
    assert two_sum_example([3, 3], 6) == [0, 1]
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Contains Duplicate ---")
    try:
        assert contains_duplicate([1, 2, 3, 1]) == True, "Has duplicate"
        assert contains_duplicate([1, 2, 3, 4]) == False, "All distinct"
        assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
        assert contains_duplicate([]) == False, "Empty array"
        assert contains_duplicate([1]) == False, "Single element"
        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: First Unique Character ---")
    try:
        assert first_unique_char("leetcode") == 0, "l is first unique"
        assert first_unique_char("loveleetcode") == 2, "v is first unique"
        assert first_unique_char("aabb") == -1, "No unique char"
        assert first_unique_char("a") == 0, "Single char"
        assert first_unique_char("aadadaad") == -1, "No unique"
        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    # ==========================================
    # REVISION: Module 1 (Arrays & Iteration)
    # ==========================================
    print("\n--- REVISION: Arrays & Iteration ---")
    try:
        assert revision_find_min([3, 1, 4, 1, 5]) == 1, "Find minimum"
        assert revision_find_min([-5, -2, -10]) == -10, "Negative numbers"
        print("Revision PASSED!")
    except AssertionError as e:
        print(f"Revision FAILED: {e}")
    except Exception as e:
        print(f"Revision ERROR: {e}")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Sets give O(1) membership testing - use for "have I seen this?"
2. Dicts give O(1) lookup AND can store associated values
3. If checking "if x in list" in a loop, convert to set first
4. Two-pass with dict: first count, then use the counts
5. Two Sum pattern: look for complement in hash map
""")
