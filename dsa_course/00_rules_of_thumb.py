"""
DSA Course - Rules of Thumb & Pattern Recognition
==================================================

This module contains practical heuristics for recognizing which techniques
to use for different problem types. Use this as a quick reference when
approaching new DSA problems.
"""

# ============================================
# SECTION 1: DATA STRUCTURE SELECTION
# ============================================

"""
RULE 1: Use SET to eliminate duplicates or track "seen" elements
----------------------------------------------------------------
Example: Check if array contains duplicate
    BAD:  if num in list_of_seen:  # O(n) lookup
    GOOD: if num in set_of_seen:   # O(1) lookup
"""

def example_use_set_for_duplicates(nums: list[int]) -> bool:
    """Return True if array has duplicates."""
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


"""
RULE 2: Build DICT as you go (one-pass) instead of two-pass
------------------------------------------------------------
Example: Two Sum - find indices of two numbers that sum to target
    BAD:  Build full dict, then search separately (two passes)
    GOOD: Build dict while searching (one pass)
"""

def example_build_dict_as_you_go(nums: list[int], target: int) -> list[int]:
    """Find two numbers that sum to target."""
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i  # Build as we go
    return []


"""
RULE 3: Use COUNTER for frequency problems
-------------------------------------------
Example: Find first non-repeating character
    BAD:  Manually count with dict
    GOOD: Use Counter from collections
"""

def example_use_counter(s: str) -> int:
    """Return index of first non-repeating character."""
    from collections import Counter
    counts = Counter(s)
    for i, char in enumerate(s):
        if counts[char] == 1:
            return i
    return -1


# ============================================
# SECTION 2: PATTERN RECOGNITION
# ============================================

"""
RULE 4: "if x in list" inside loop → convert to SET first
-----------------------------------------------------------
Example: Find intersection of two arrays
    BAD:  for num in arr1:
              if num in arr2:  # O(n*m) - arr2 is a list
    GOOD: set2 = set(arr2)
          for num in arr1:
              if num in set2:  # O(n+m) - set2 is a set
"""

def example_list_to_set_for_lookups(arr1: list[int], arr2: list[int]) -> list[int]:
    """Find common elements between two arrays."""
    set2 = set(arr2)  # Convert once
    result = []
    for num in arr1:
        if num in set2:  # O(1) lookup
            result.append(num)
            set2.remove(num)  # Avoid duplicates
    return result


"""
RULE 5: Sorted array + need two elements → Two pointers from ends
------------------------------------------------------------------
Example: Find two numbers that sum to target in SORTED array
    BAD:  Nested loops - O(n²)
    GOOD: Left/right pointers - O(n)
"""

def example_two_pointers_sorted(nums: list[int], target: int) -> list[int]:
    """Find two numbers that sum to target in sorted array."""
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []


"""
RULE 6: In-place array manipulation → Slow/fast pointers
---------------------------------------------------------
Example: Move all zeros to end of array
    BAD:  Create new array - O(n) space
    GOOD: Use write pointer and read pointer - O(1) space
"""

def example_slow_fast_pointers(nums: list[int]) -> None:
    """Move all zeros to end, maintain order of non-zeros."""
    write = 0  # Slow pointer - where to write next non-zero
    for read in range(len(nums)):  # Fast pointer - scanning array
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
    # Fill remaining with zeros
    for i in range(write, len(nums)):
        nums[i] = 0


"""
RULE 7: "Consecutive elements" / "substring" / "subarray" → Sliding Window
---------------------------------------------------------------------------
Example: Maximum sum of k consecutive elements
    BAD:  Recalculate sum for each window - O(n*k)
    GOOD: Slide window, update incrementally - O(n)
"""

def example_sliding_window(nums: list[int], k: int) -> int:
    """Find maximum sum of k consecutive elements."""
    # Calculate first window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide window
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]  # Remove left, add right
        max_sum = max(max_sum, window_sum)

    return max_sum


"""
RULE 8: Look for COMPLEMENT pattern
------------------------------------
Example: Two Sum, finding pairs
    Instead of: "Does element Y exist?"
    Think:      "Does complement (target - X) exist?"
"""

def example_complement_pattern(nums: list[int], target: int) -> bool:
    """Check if any two numbers sum to target."""
    seen = set()
    for num in nums:
        complement = target - num  # What we NEED to find
        if complement in seen:
            return True
        seen.add(num)
    return False


# ============================================
# SECTION 3: OPTIMIZATION STRATEGIES
# ============================================

"""
RULE 9: Trade space for time (most common optimization)
--------------------------------------------------------
Example: Checking for duplicates
    O(n²) time, O(1) space: Nested loops
    O(n) time, O(n) space:  Use set

    Usually worth it! Going from O(n²) to O(n) is huge.
"""


"""
RULE 10: Nested loops (O(n²)) → Often optimizable to O(n)
-----------------------------------------------------------
How? Usually with:
    - Hash map (store what you need to find)
    - Two pointers (if sorted)
    - Sliding window (if consecutive)

Example: Find pair with sum = target
    BAD:  for i in range(n):
              for j in range(i+1, n):  # O(n²)
    GOOD: Use hash map or two pointers  # O(n)
"""


"""
RULE 11: Multiple range queries → Precompute (Prefix Sum)
----------------------------------------------------------
Example: Sum of elements from index i to j (multiple queries)
    BAD:  Calculate sum each time - O(n) per query
    GOOD: Build prefix sum once - O(1) per query
"""

def example_prefix_sum(nums: list[int]):
    """Build prefix sum for O(1) range queries."""
    prefix = [0]
    for num in nums:
        prefix.append(prefix[-1] + num)

    # Now query sum from index i to j in O(1):
    def range_sum(i: int, j: int) -> int:
        return prefix[j+1] - prefix[i]

    return range_sum


"""
RULE 12: Can you sort the input? Sometimes O(n log n) sort enables O(n) solution
---------------------------------------------------------------------------------
Example: Find if there are two numbers that sum to target
    Unsorted: Need hash map
    Sorted:   Two pointers from ends - cleaner code, same O(n) after sort
"""


# ============================================
# SECTION 4: PROBLEM-SOLVING APPROACH
# ============================================

"""
RULE 13: Start with brute force (mentally)
-------------------------------------------
1. What's the obvious, naive solution?
2. What's its time complexity?
3. Can you eliminate the bottleneck?

Example: Two Sum
    Brute force:  Try all pairs - O(n²)
    Bottleneck:   Looking for complement
    Optimization: Use hash map for O(1) lookup - O(n)
"""


"""
RULE 14: Ask yourself: "What needs to be tracked?"
---------------------------------------------------
Before coding, identify:
    - What variables do I need?
    - What's being counted/accumulated/compared?
    - What state changes as I iterate?

Example: Finding minimum
    Track: min_so_far
    Update: if current < min_so_far

Example: Two pointers
    Track: left pointer, right pointer
    Update: based on comparison with target
"""


"""
RULE 15: Edge cases to always consider
---------------------------------------
    - Empty input: [], "", None
    - Single element: [1], "a"
    - All same elements: [5, 5, 5]
    - Duplicates vs all unique
    - Already in desired state (e.g., already sorted)
    - Extreme values (very large, very small, negative)
"""


# ============================================
# SECTION 5: KEYWORD TRIGGERS
# ============================================

"""
PROBLEM KEYWORDS → TECHNIQUE
----------------------------

"find pair/two elements" → Hash map (unsorted) or Two pointers (sorted)
"consecutive/substring/subarray" → Sliding window
"in-place with O(1) space" → Two pointers (slow/fast)
"find duplicate/unique" → Set or Counter
"frequency/count/anagram" → Counter or dict
"multiple queries on array" → Prefix sum
"sorted array" → Binary search or Two pointers
"linked list cycle" → Fast/slow pointers
"middle of linked list" → Fast/slow pointers
"contains/exists/seen before" → Set or hash map
"""


# ============================================
# SECTION 6: COMMON MISTAKES TO AVOID
# ============================================

"""
MISTAKE 1: Using list when you need set
----------------------------------------
    BAD:  if x in my_list:  # O(n) lookup
    GOOD: if x in my_set:   # O(1) lookup
"""


"""
MISTAKE 2: Not considering one-pass solutions
----------------------------------------------
    BAD:  First loop to build dict, second loop to search
    GOOD: Build and search in same loop (when possible)
"""


"""
MISTAKE 3: Forgetting that sort modifies original array
--------------------------------------------------------
    If you need original order, make a copy first:
        sorted_nums = sorted(nums)  # Creates copy
    vs
        nums.sort()  # Modifies in place
"""


"""
MISTAKE 4: Off-by-one errors with pointers
-------------------------------------------
    Two pointers: while left < right (not <=, usually)
    Sliding window: Remember window size is right - left + 1
    Array indices: range(len(arr)) goes from 0 to len-1
"""


"""
MISTAKE 5: Not checking for empty input
----------------------------------------
    Always handle: empty array, empty string, None
        if not nums:
            return default_value
"""


# ============================================
# QUICK REFERENCE CARD
# ============================================

"""
QUICK PATTERN MATCHING GUIDE
=============================

SEE THIS                           → THINK THIS
-----------------------------------------------------------------
"if x in list" in loop             → Convert list to set first
Need to find pairs                 → Hash map (store complement)
Sorted array + find elements       → Two pointers from ends
Consecutive elements               → Sliding window
In-place, O(1) extra space         → Two pointers (slow/fast)
Frequency counting                 → Counter or dict
Duplicates/unique elements         → Set
Range sum queries                  → Prefix sum
Nested loops (O(n²))               → Try to optimize to O(n)


TIME COMPLEXITY GOALS
=====================
O(1)       : Hash map lookup, set lookup, array index access
O(log n)   : Binary search (sorted array)
O(n)       : Single pass through array (use hash map, not nested loops)
O(n log n) : Sorting
O(n²)      : Usually avoidable! Look for optimization.


SPACE-TIME TRADEOFFS
====================
Most optimizations: Trade O(n) space for better time
Worth it when: Going from O(n²) to O(n) or O(n log n) to O(n)
Not worth it when: Already O(n) time, trying to save space

Remember: In interviews and most real-world code, time > space
"""


# ============================================
# PRACTICE: Pattern Recognition
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("DSA RULES OF THUMB - Pattern Recognition Guide")
    print("=" * 60)
    print("\nKey Insight: Most problems fall into a few patterns.")
    print("Learning to recognize these patterns is the key to mastery.")
    print("\nWhen stuck, ask yourself:")
    print("  1. What's the brute force solution?")
    print("  2. What's the bottleneck?")
    print("  3. Is there a data structure that makes lookups faster?")
    print("  4. Can I solve it in one pass?")
    print("  5. Does the input have special properties (sorted, etc)?")
    print("\n" + "=" * 60)
