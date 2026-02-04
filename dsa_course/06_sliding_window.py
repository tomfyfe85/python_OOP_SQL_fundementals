"""
DSA Course - Module 5: Sliding Window
=====================================

CONCEPT: Sliding Window Technique
---------------------------------
Process subarrays/substrings by maintaining a "window" that slides
through the data. Instead of recalculating everything for each
position, we update by removing left element and adding right element.

TWO TYPES:

1. FIXED SIZE WINDOW
   - Window size k is given
   - Slide one position at a time
   - Add new element, remove old element

2. VARIABLE SIZE WINDOW
   - Find smallest/largest window meeting some condition
   - Expand window to satisfy condition
   - Shrink window to optimize

THE KEY INSIGHT:
Instead of O(n*k) by recalculating each window from scratch,
we get O(n) by updating incrementally.

WHEN TO USE:
- "Find maximum/minimum sum of k consecutive elements"
- "Find longest substring with some property"
- "Find smallest subarray with sum >= target"
"""


# ============================================
# EXAMPLE: Maximum Sum of K Consecutive Elements
# ============================================

def max_sum_k_elements_example(nums: list[int], k: int) -> int:
    """
    Find the maximum sum of any k consecutive elements.

    Brute force: For each starting position, sum k elements -> O(n*k)
    Sliding window: Compute first sum, then slide -> O(n)

    Strategy:
    1. Calculate sum of first k elements
    2. Slide window: subtract element leaving, add element entering
    3. Track maximum sum seen
    """
    if len(nums) < k:
        return 0

    # Calculate sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(nums)):
        # Remove element leaving window (at i-k)
        # Add element entering window (at i)
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


# Let's trace through: nums=[2, 1, 5, 1, 3, 2], k=3
#
# Initial window [2, 1, 5]: sum = 8, max = 8
#
# i=3: Remove nums[0]=2, Add nums[3]=1
#      Window [1, 5, 1]: sum = 8-2+1 = 7, max = 8
#
# i=4: Remove nums[1]=1, Add nums[4]=3
#      Window [5, 1, 3]: sum = 7-1+3 = 9, max = 9
#
# i=5: Remove nums[2]=5, Add nums[5]=2
#      Window [1, 3, 2]: sum = 9-5+2 = 6, max = 9
#
# Return 9


# ============================================
# QUESTION 1: Maximum Average Subarray
# ============================================

"""
PROBLEM: Find the maximum average of any subarray of length k.

Given an array and integer k, find the contiguous subarray of
length k that has the maximum average value. Return the maximum average.

Examples:
- nums=[1,12,-5,-6,50,3], k=4 -> 12.75
  (subarray [12,-5,-6,50] has sum 51, average 51/4 = 12.75)
- nums=[5], k=1 -> 5.0

HINT: This is just "max sum of k elements" divided by k.
      Use sliding window to find max sum, then divide.

Implement the function below:
"""


def find_max_average(nums: list[int], k: int) -> float:
    """Return the maximum average of any subarray of length k."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2: Longest Substring Without Repeating
# ============================================

"""
PROBLEM: Find length of longest substring without repeating characters.

Given a string, find the length of the longest substring that
contains no duplicate characters.

Examples:
- "abcabcbb" -> 3 (substring "abc")
- "bbbbb" -> 1 (substring "b")
- "pwwkew" -> 3 (substring "wke")

HINT: Variable size sliding window.
      - Use a SET to track characters in current window
      - Expand window (move right pointer) to explore
      - When duplicate found, shrink window (move left pointer)
        until the duplicate is removed
      - Track maximum window size seen

      Think of it as:
      - right pointer adds characters
      - left pointer removes characters when there's a duplicate
      - window = s[left:right+1]

Implement the function below:
"""


def length_of_longest_substring(s: str) -> int:
    """Return length of longest substring without repeating characters."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 5: Sliding Window")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Max Sum of K Elements ---")
    assert max_sum_k_elements_example([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_sum_k_elements_example([1, 2, 3, 4, 5], 2) == 9
    assert max_sum_k_elements_example([5], 1) == 5
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Maximum Average Subarray ---")
    try:
        result1 = find_max_average([1, 12, -5, -6, 50, 3], 4)
        assert abs(result1 - 12.75) < 0.001, f"Expected 12.75, got {result1}"

        result2 = find_max_average([5], 1)
        assert abs(result2 - 5.0) < 0.001, f"Expected 5.0, got {result2}"

        result3 = find_max_average([0, 4, 0, 3, 2], 1)
        assert abs(result3 - 4.0) < 0.001, f"Expected 4.0, got {result3}"

        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: Longest Substring Without Repeating ---")
    try:
        assert length_of_longest_substring("abcabcbb") == 3, "abc"
        assert length_of_longest_substring("bbbbb") == 1, "b"
        assert length_of_longest_substring("pwwkew") == 3, "wke"
        assert length_of_longest_substring("") == 0, "empty"
        assert length_of_longest_substring("a") == 1, "single"
        assert length_of_longest_substring("abcdef") == 6, "all unique"
        # Edge cases
        assert length_of_longest_substring("dvdf") == 3, "dvdf -> vdf"
        assert length_of_longest_substring("aab") == 2, "aab -> ab"
        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    # ==========================================
    # REVISION: Module 5 (Linked Lists)
    # ==========================================
    print("\n--- REVISION: Linked Lists ---")
    print("Q: Why use a dummy head node when modifying linked lists?")
    print("A: It simplifies edge cases like removing the first node - you always have a valid 'previous' node.")

    print("""
1. Fixed window: slide by removing left, adding right
2. Variable window: expand to explore, shrink to optimize
3. Use set to track unique elements in window
4. Window = everything between left and right pointers
5. This turns O(n*k) or O(n^2) into O(n)
""")
