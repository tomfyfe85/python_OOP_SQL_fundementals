"""
DSA Course - Module 15: Divide & Conquer
========================================

CONCEPT: Divide and Conquer
---------------------------
Break a problem into smaller subproblems, solve them recursively,
then combine the results.

THE THREE STEPS:
1. DIVIDE: Split problem into smaller subproblems
2. CONQUER: Solve subproblems recursively (base case for small problems)
3. COMBINE: Merge subproblem solutions into final solution

CLASSIC EXAMPLES:
- Merge Sort: divide array, sort halves, merge
- Quick Sort: partition around pivot, sort halves
- Binary Search: eliminate half each step
- Finding maximum subarray (Kadane's is better, but D&C works)

TIME COMPLEXITY ANALYSIS:
Use the Master Theorem: T(n) = aT(n/b) + f(n)
- a = number of subproblems
- n/b = size of each subproblem
- f(n) = cost to divide and combine

For Merge Sort: T(n) = 2T(n/2) + O(n) -> O(n log n)

WHEN TO USE:
- Problem naturally splits into independent subproblems
- Subproblems have same structure as original
- Combining solutions is efficient
"""


# ============================================
# EXAMPLE: Merge Sort
# ============================================

def merge_sort_example(nums: list[int]) -> list[int]:
    """
    Sort array using merge sort.

    Strategy:
    1. Divide: split array in half
    2. Conquer: recursively sort each half
    3. Combine: merge two sorted halves

    Time: O(n log n), Space: O(n)
    """
    # Base case: single element or empty is already sorted
    if len(nums) <= 1:
        return nums

    # Divide
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    # Conquer
    left_sorted = merge_sort_example(left)
    right_sorted = merge_sort_example(right)

    # Combine
    return merge(left_sorted, right_sorted)


def merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted arrays into one sorted array."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Let's trace: [38, 27, 43, 3]
#
# merge_sort([38, 27, 43, 3])
#   mid = 2
#   left = merge_sort([38, 27])
#     mid = 1
#     left = merge_sort([38]) -> [38]
#     right = merge_sort([27]) -> [27]
#     merge([38], [27]) -> [27, 38]
#   right = merge_sort([43, 3])
#     mid = 1
#     left = merge_sort([43]) -> [43]
#     right = merge_sort([3]) -> [3]
#     merge([43], [3]) -> [3, 43]
#   merge([27, 38], [3, 43]) -> [3, 27, 38, 43]


# ============================================
# QUESTION 1: Quick Sort
# ============================================

"""
PROBLEM: Implement Quick Sort.

Quick Sort:
1. Pick a pivot element
2. Partition: elements < pivot go left, >= pivot go right
3. Recursively sort left and right partitions

Average Time: O(n log n), Worst: O(n^2) if bad pivot choices
Space: O(log n) for recursion stack

Examples:
- [3,1,4,1,5,9,2,6] -> [1,1,2,3,4,5,6,9]
- [5,4,3,2,1] -> [1,2,3,4,5]
- [] -> []

Implement the function below (modify array in-place):
"""


def quick_sort(nums: list[int]) -> list[int]:
    """Sort array using quick sort. Return sorted array."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2: Count Inversions
# ============================================

"""
PROBLEM: Count inversions in an array.

An inversion is a pair (i, j) where i < j but nums[i] > nums[j].
In other words, a pair that's "out of order".

Examples:
- [2, 4, 1, 3, 5] -> 3 inversions
  (2,1), (4,1), (4,3) - pairs where larger number comes before smaller

- [1, 2, 3, 4, 5] -> 0 inversions (already sorted)

- [5, 4, 3, 2, 1] -> 10 inversions (reverse sorted = maximum inversions)

Implement the function below:
"""


def count_inversions(nums: list[int]) -> int:
    """Return the number of inversions in the array."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 3: Find Median of Two Sorted Arrays
# ============================================

"""
PROBLEM: Find the median of two sorted arrays in O(log(m+n)) time.

Given two sorted arrays nums1 and nums2, return the median.

Examples:
- nums1=[1,3], nums2=[2] -> 2.0
  Merged: [1,2,3], median is 2

- nums1=[1,2], nums2=[3,4] -> 2.5
  Merged: [1,2,3,4], median is (2+3)/2 = 2.5

- nums1=[0,0], nums2=[0,0] -> 0.0

Implement the function below:
"""


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    """Find median of two sorted arrays."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 4: Maximum Subarray (Divide & Conquer)
# ============================================

"""
PROBLEM: Find the maximum sum of a contiguous subarray.

Given an integer array, find the contiguous subarray with the largest sum.

Examples:
- [-2,1,-3,4,-1,2,1,-5,4] -> 6 (subarray [4,-1,2,1])
- [1] -> 1
- [5,4,-1,7,8] -> 23 (entire array)

Note: Kadane's algorithm (O(n)) is better for this problem,
but D&C approach is O(n log n) and good for learning.

Implement the function below:
"""


def max_subarray_dc(nums: list[int]) -> int:
    """Find maximum subarray sum using divide and conquer."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 15: Divide & Conquer")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Merge Sort ---")
    assert merge_sort_example([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]
    assert merge_sort_example([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert merge_sort_example([1]) == [1]
    assert merge_sort_example([]) == []
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Quick Sort ---")
    try:
        assert quick_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]
        assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
        assert quick_sort([1]) == [1]
        assert quick_sort([]) == []
        assert quick_sort([1, 1, 1]) == [1, 1, 1]
        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: Count Inversions ---")
    try:
        assert count_inversions([2, 4, 1, 3, 5]) == 3
        assert count_inversions([1, 2, 3, 4, 5]) == 0
        assert count_inversions([5, 4, 3, 2, 1]) == 10
        assert count_inversions([1, 3, 2]) == 1
        assert count_inversions([]) == 0
        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    # Test Question 3
    print("\n--- Question 3: Median of Two Sorted Arrays ---")
    try:
        assert find_median_sorted_arrays([1, 3], [2]) == 2.0
        assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
        assert find_median_sorted_arrays([0, 0], [0, 0]) == 0.0
        assert find_median_sorted_arrays([], [1]) == 1.0
        assert find_median_sorted_arrays([2], []) == 2.0
        print("All Question 3 tests PASSED!")
    except AssertionError as e:
        print(f"Question 3 FAILED: {e}")
    except Exception as e:
        print(f"Question 3 ERROR: {e}")

    # Test Question 4
    print("\n--- Question 4: Maximum Subarray (D&C) ---")
    try:
        assert max_subarray_dc([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
        assert max_subarray_dc([1]) == 1
        assert max_subarray_dc([5, 4, -1, 7, 8]) == 23
        assert max_subarray_dc([-1]) == -1
        assert max_subarray_dc([-2, -1]) == -1
        # Edge cases
        assert max_subarray_dc([1, 2, 3]) == 6, "All positive"
        assert max_subarray_dc([-1, -2, -3]) == -1, "All negative"
        print("All Question 4 tests PASSED!")
    except AssertionError as e:
        print(f"Question 4 FAILED: {e}")
    except Exception as e:
        print(f"Question 4 ERROR: {e}")

    # ==========================================
    # REVISION: Module 14 (Heaps)
    # ==========================================
    print("\n--- REVISION: Heaps ---")
    print("Q: To find K largest elements, which type of heap and what size?")
    print("A: Min-heap of size K. The smallest in the heap is the Kth largest overall.")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Divide & Conquer: divide, conquer (recursively), combine
2. Merge Sort: O(n log n), stable, but O(n) extra space
3. Quick Sort: O(n log n) average, O(n^2) worst, in-place
4. Count inversions: modified merge sort counts during merge
5. Many problems have both D&C and other solutions (e.g., Kadane for max subarray)
""")