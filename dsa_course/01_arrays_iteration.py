"""
DSA Course - Module 1: Arrays & Iteration
==========================================

CONCEPT: Arrays and Basic Iteration
-----------------------------------
Arrays (lists in Python) are ordered collections of elements.
Most DSA problems start with iterating through an array to find,
count, or transform elements.

KEY PATTERNS:
1. Linear scan - look at each element once O(n)
2. Track state while iterating (max, min, sum, count)
3. Build result while iterating

WHEN TO USE:
- Finding a specific element
- Computing aggregates (sum, max, min)
- Transforming data
- Checking conditions across elements

TIME COMPLEXITY:
- Accessing by index: O(1)
- Iterating through all: O(n)
- Searching unsorted: O(n)
"""


# ============================================
# EXAMPLE: Find Maximum Element
# ============================================

def find_maximum_example(nums: list[int]) -> int:
    """
    Find the largest number in an array.

    Strategy:
    1. Assume first element is max
    2. Iterate through rest
    3. Update max when we find larger

    This is the fundamental pattern: track state while iterating.
    """
    if not nums:
        return None

    max_val = nums[0]  # Start with first element

    for num in nums:
        if num > max_val:
            max_val = num

    return max_val


# Let's trace through: [3, 1, 4, 1, 5, 9, 2, 6]
#
# max_val = 3
# num=3: 3 > 3? No
# num=1: 1 > 3? No
# num=4: 4 > 3? Yes -> max_val = 4
# num=1: 1 > 4? No
# num=5: 5 > 4? Yes -> max_val = 5
# num=9: 9 > 5? Yes -> max_val = 9
# num=2: 2 > 9? No
# num=6: 6 > 9? No
# Return 9


# ============================================
# QUESTION 1: Second Largest Element
# ============================================

"""
PROBLEM: Find the second largest element in an array.

Given an array of integers, return the second largest element.
If there's no second largest (array too small or all same), return None.

Examples:
- [3, 1, 4, 1, 5, 9] -> 5 (largest is 9, second is 5)
- [1, 1, 1] -> None (all same, no second largest)
- [5] -> None (only one element)
- [3, 3, 3, 2] -> 2 (largest is 3, second is 2)

HINT: Track TWO values while iterating: largest AND second largest.
      Think about when to update each one.

Implement the function below:
"""


def second_largest(nums: list[int]) -> int | None:
    """Return the second largest element, or None if it doesn't exist."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2: Count Elements Greater Than Average
# ============================================

"""
PROBLEM: Count how many elements are greater than the average.

Given an array of integers, return the count of elements that are
strictly greater than the average of all elements.

Examples:
- [1, 2, 3, 4, 5] -> 2 (average is 3.0, elements 4 and 5 are greater)
- [10, 10, 10] -> 0 (average is 10, nothing is greater)
- [1, 100] -> 1 (average is 50.5, only 100 is greater)

HINT: You need to iterate TWICE:
      1. First pass: calculate the average
      2. Second pass: count elements > average

This is a common pattern: sometimes you need info from the whole
array before you can process individual elements.

Implement the function below:
"""


def count_above_average(nums: list[int]) -> int:
    """Return count of elements strictly greater than the average."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 1: Arrays & Iteration")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Find Maximum ---")
    assert find_maximum_example([3, 1, 4, 1, 5, 9, 2, 6]) == 9
    assert find_maximum_example([1]) == 1
    assert find_maximum_example([-5, -2, -10]) == -2
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Second Largest ---")
    try:
        assert second_largest([3, 1, 4, 1, 5, 9]) == 5, "Basic case failed"
        assert second_largest([1, 1, 1]) is None, "All same should return None"
        assert second_largest([5]) is None, "Single element should return None"
        assert second_largest([3, 3, 3, 2]) == 2, "Duplicates of max"
        assert second_largest([1, 2]) == 1, "Two elements"
        assert second_largest([-1, -5, -2]) == -2, "Negative numbers"
        assert second_largest([5, 5]) is None, "Two same elements"
        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: Count Above Average ---")
    try:
        assert count_above_average([1, 2, 3, 4, 5]) == 2, "Basic case"
        assert count_above_average([10, 10, 10]) == 0, "All same"
        assert count_above_average([1, 100]) == 1, "Two elements"
        assert count_above_average([1]) == 0, "Single element"
        assert count_above_average([1, 2, 3, 4, 5, 6]) == 3, "Even count"
        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Most array problems involve iterating and tracking state
2. Sometimes you need multiple passes through the array
3. Always handle edge cases: empty, single element, all same
4. Think about what state you need to track BEFORE coding
""")
