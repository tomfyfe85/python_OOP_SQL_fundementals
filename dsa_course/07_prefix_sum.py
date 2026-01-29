"""
DSA Course - Module 7: Prefix Sum
=================================

CONCEPT: Prefix Sum (Cumulative Sum)
------------------------------------
Precompute cumulative sums so you can calculate any range sum in O(1).

THE IDEA:
prefix[i] = sum of all elements from index 0 to i-1

Then: sum from index i to j = prefix[j+1] - prefix[i]

WHY IT WORKS:
prefix[j+1] = nums[0] + nums[1] + ... + nums[j]
prefix[i]   = nums[0] + nums[1] + ... + nums[i-1]
Difference  = nums[i] + nums[i+1] + ... + nums[j]  <- that's our range!

TIME COMPLEXITY:
- Build prefix array: O(n)
- Query any range sum: O(1)
- Total for m queries: O(n + m) instead of O(n * m)

WHEN TO USE:
- Multiple range sum queries
- Finding subarrays with specific sum
- Running totals and cumulative statistics
"""


# ============================================
# EXAMPLE: Range Sum Query
# ============================================

class NumArrayExample:
    """
    Calculate sum of elements between indices left and right (inclusive).

    Brute force: sum each time -> O(n) per query
    Prefix sum: precompute, then O(1) per query
    """

    def __init__(self, nums: list[int]):
        """Build the prefix sum array."""
        # prefix[i] = sum of nums[0..i-1]
        # prefix[0] = 0 (sum of nothing)
        # prefix[1] = nums[0]
        # prefix[2] = nums[0] + nums[1]
        # etc.

        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sum_range(self, left: int, right: int) -> int:
        """Return sum of nums[left..right] in O(1)."""
        return self.prefix[right + 1] - self.prefix[left]


# Let's trace through: nums = [1, 2, 3, 4, 5]
#
# Building prefix:
# prefix = [0]
# num=1: prefix = [0, 1]
# num=2: prefix = [0, 1, 3]
# num=3: prefix = [0, 1, 3, 6]
# num=4: prefix = [0, 1, 3, 6, 10]
# num=5: prefix = [0, 1, 3, 6, 10, 15]
#
# Query sum_range(1, 3) -> sum of [2, 3, 4]
# = prefix[4] - prefix[1]
# = 10 - 1
# = 9 ✓ (2+3+4=9)


# ============================================
# QUESTION 1: Running Sum of Array
# ============================================

"""
PROBLEM: Return the running sum of an array.

Given an array nums, return an array where result[i] is the
sum of nums[0] through nums[i].

Examples:
- [1, 2, 3, 4] -> [1, 3, 6, 10]
  result[0] = 1
  result[1] = 1 + 2 = 3
  result[2] = 1 + 2 + 3 = 6
  result[3] = 1 + 2 + 3 + 4 = 10

- [1, 1, 1, 1, 1] -> [1, 2, 3, 4, 5]

HINT: This is literally building a prefix sum array!
      Each element = previous running sum + current element

Implement the function below:
"""


def running_sum(nums: list[int]) -> list[int]:
    """Return the running sum array."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2: Subarray Sum Equals K
# ============================================

"""
PROBLEM: Count subarrays that sum to exactly k.

Given an array of integers and an integer k, return the total
number of contiguous subarrays whose sum equals k.

Examples:
- nums=[1,1,1], k=2 -> 2
  Subarrays: [1,1] at index 0-1 and [1,1] at index 1-2

- nums=[1,2,3], k=3 -> 2
  Subarrays: [1,2] and [3]

HINT: This combines prefix sum with hash map!

Key insight: If prefix[j] - prefix[i] = k, then subarray i..j-1 sums to k
Rearranged: prefix[i] = prefix[j] - k

So for each position j:
- Calculate current prefix sum
- Check how many times (current_sum - k) appeared before
- That's how many subarrays ending at j sum to k!

Use a hash map to count occurrences of each prefix sum.
Initialize with {0: 1} because empty prefix has sum 0.

Implement the function below:
"""


def subarray_sum(nums: list[int], k: int) -> int:
    """Return count of subarrays that sum to k."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 7: Prefix Sum")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Range Sum Query ---")
    arr = NumArrayExample([1, 2, 3, 4, 5])
    assert arr.sum_range(0, 2) == 6   # 1+2+3
    assert arr.sum_range(1, 3) == 9   # 2+3+4
    assert arr.sum_range(0, 4) == 15  # 1+2+3+4+5
    assert arr.sum_range(2, 2) == 3   # just 3
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Running Sum ---")
    try:
        assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10], "Basic case"
        assert running_sum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5], "All ones"
        assert running_sum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17], "Mixed"
        assert running_sum([1]) == [1], "Single element"
        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: Subarray Sum Equals K ---")
    try:
        assert subarray_sum([1, 1, 1], 2) == 2, "Two subarrays"
        assert subarray_sum([1, 2, 3], 3) == 2, "[1,2] and [3]"
        assert subarray_sum([1], 1) == 1, "Single element"
        assert subarray_sum([1, -1, 0], 0) == 3, "With negatives"
        assert subarray_sum([1, 2, 1, 2, 1], 3) == 4, "Multiple"
        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Prefix sum: prefix[i] = sum of elements before index i
2. Range sum: sum(i to j) = prefix[j+1] - prefix[i]
3. Build once O(n), query O(1) - great for multiple queries
4. Prefix sum + hash map = count subarrays with target sum
5. Start with {0: 1} to handle subarrays starting at index 0
""")
