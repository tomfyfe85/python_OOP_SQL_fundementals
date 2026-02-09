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
# EXAMPLE: Using a Set for Membership
# ============================================

def find_intersection_example(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Find common elements between two arrays.

    Brute force: For each element in nums1, check if in nums2 - O(n*m)
    With set: Convert nums2 to set, then check membership - O(n+m)

    Strategy:
    - Convert one list to a set for O(1) lookups
    - Iterate through the other list, checking membership
    """
    set2 = set(nums2)
    result = []

    for num in nums1:
        if num in set2:
            result.append(num)
            set2.remove(num)  # Avoid duplicates in result

    return result


# Let's trace through: nums1=[1, 2, 2, 1], nums2=[2, 2]
#
# set2 = {2}
# num=1: 1 not in set2, skip
# num=2: 2 in set2, add to result, remove from set2
# num=2: 2 not in set2 (already removed), skip
# num=1: 1 not in set2, skip
# Return [2]


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

Implement the function below:
"""


def contains_duplicate(nums: list[int]) -> bool:
    """Return True if any element appears more than once."""
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

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

Implement the function below:
"""

from collections import Counter
def first_unique_char(s: str) -> int:
    """Return index of first non-repeating character, or -1."""
    cnt = Counter(s)
    for i, char in enumerate(s):
        if cnt[char] == 1:
            return i
    return -1




# ============================================
# QUESTION 3: Two Sum (LeetCode #1)
# ============================================

"""
PROBLEM: Find two numbers that add up to target. Return their indices.

This is THE classic LeetCode problem #1. It demonstrates the power
of using a hash map for O(n) lookups.

Examples:
- nums=[2, 7, 11, 15], target=9 -> [0, 1] (2+7=9)
- nums=[3, 2, 4], target=6 -> [1, 2] (2+4=6)
- nums=[3, 3], target=6 -> [0, 1] (3+3=6)

Implement the function below:
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """Find two numbers that add up to target. Return their indices."""
    from collections import Counter

    int_count = Counter(nums)
    hash_map = {v: k for k, v in enumerate(nums) }
    final = []

    for i, num in enumerate(nums):
        diff = target - num

        if diff in hash_map.keys():
              if diff == target/2 and int_count.get(num) == 1:
                  continue
              
              final.append(i)
              final.append(hash_map[diff])
              return final

# ============================================
# REVISION: Quick Review from Module 1
# ============================================

"""
REVISION: Find the minimum element in an array.s

This is a quick refresher on array iteration from Module 1.
Solve it WITHOUT using Python's built-in min() function.

Example: [3, 1, 4, 1, 5] -> 1
"""


def revision_find_min(nums: list[int]) -> int:
    """Return the minimum element in the array."""
    
    min_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 2: Hash Maps & Sets")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Find Intersection ---")
    assert find_intersection_example([1, 2, 2, 1], [2, 2]) == [2]
    assert find_intersection_example([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9] or \
            find_intersection_example([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4]
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Contains Duplicate ---")
    try:
        assert contains_duplicate([1, 2, 3, 1]) == True, "Has duplicate"
        assert contains_duplicate([1, 2, 3, 4]) == False, "All distinct"
        assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
        assert contains_duplicate([]) == False, "Empty array"
        assert contains_duplicate([1]) == False, "Single element"
        # Edge cases
        assert contains_duplicate([1, 2, 3, 4, 5, 1]) == True, "Duplicate at end"
        assert contains_duplicate([1, 1]) == True, "Two same elements"
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
        # Edge cases
        assert first_unique_char("") == -1, "Empty string"
        assert first_unique_char("cc") == -1, "All duplicates"
        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    # Test Question 3 (LeetCode #1)
    print("\n--- Question 3: Two Sum (LeetCode #1) ---")
    try:
        assert two_sum([2, 7, 11, 15], 9) == [0, 1], "Basic case"
        assert two_sum([3, 2, 4], 6) == [1, 2], "Not first two"
        assert two_sum([3, 3], 6) == [0, 1], "Same numbers"
        # Edge cases
        assert two_sum([1, 2, 3, 4, 5], 9) == [3, 4], "Target at end"
        print("All Question 3 tests PASSED!")
    except AssertionError as e:
        print(f"Question 3 FAILED: {e}")
    except Exception as e:
        print(f"Question 3 ERROR: {e}")

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