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
    if not nums:
        return None
    
    no_dupes = sorted(set(nums))
    if len(no_dupes) == 1:
        return None
    
    return no_dupes[-2]



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

    average = sum(nums)/len(nums)
    return sum([1 for i in nums if i > average ])



# ============================================
# QUESTION 3: Move Zeroes (LeetCode 283)
# ============================================

"""
PROBLEM: Move all zeroes to the end while maintaining relative order.

Given an array of integers, move all 0's to the end while keeping
the relative order of the non-zero elements. Do this IN-PLACE.

Examples:
- [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
- [0] -> [0]
- [1, 2, 3] -> [1, 2, 3] (no zeros, unchanged)
- [0, 0, 1] -> [1, 0, 0]

HINT: Use a "write pointer" that tracks where the next non-zero should go.

      Iterate through the array:
      - When you find a non-zero, write it at the write pointer position
      - Increment the write pointer
      - After the loop, fill remaining positions with zeros

      Example walkthrough for [0, 1, 0, 3, 12]:
      write_pos = 0
      - See 0: skip
      - See 1: write to pos 0, write_pos = 1 -> [1, 1, 0, 3, 12]
      - See 0: skip
      - See 3: write to pos 1, write_pos = 2 -> [1, 3, 0, 3, 12]
      - See 12: write to pos 2, write_pos = 3 -> [1, 3, 12, 3, 12]
      - Fill rest with zeros -> [1, 3, 12, 0, 0]

Implement the function below:
"""


def move_zeroes(nums: list[int]) -> None:
    """Move all zeros to end in-place. Modify nums directly, return nothing."""
    wp = 0
    if 0 in nums:
        for i, num in enumerate(nums):
            if num == 0:
                continue
            if i == wp:
                wp += 1
                continue
            nums[wp] = nums[i]
            nums[i] = 0
            wp += 1



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

    # Test Question 3
    print("\n--- Question 3: Move Zeroes (LeetCode 283) ---")
    try:
        nums1 = [0, 1, 0, 3, 12]
        move_zeroes(nums1)
        assert nums1 == [1, 3, 12, 0, 0], f"Basic case: got {nums1}"

        nums2 = [0]
        move_zeroes(nums2)
        assert nums2 == [0], "Single zero"

        nums3 = [1, 2, 3]
        move_zeroes(nums3)
        assert nums3 == [1, 2, 3], "No zeros"

        nums4 = [0, 0, 1]
        move_zeroes(nums4)
        assert nums4 == [1, 0, 0], f"Zeros at start: got {nums4}"

        nums5 = [1, 0, 0]
        move_zeroes(nums5)
        assert nums5 == [1, 0, 0], "Zeros at end already"

        # Edge cases to catch wp tracking bugs
        nums6 = [2, 1, 0]
        move_zeroes(nums6)
        assert nums6 == [2, 1, 0], "Non-zeros already at front"

        nums7 = [1, 2, 3, 0, 0]
        move_zeroes(nums7)
        assert nums7 == [1, 2, 3, 0, 0], "Multiple non-zeros at front"

        print("All Question 3 tests PASSED!")
    except AssertionError as e:
        print(f"Question 3 FAILED: {e}")
    except Exception as e:
        print(f"Question 3 ERROR: {e}")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Most array problems involve iterating and tracking state
2. Sometimes you need multiple passes through the array
3. Always handle edge cases: empty, single element, all same
4. Think about what state you need to track BEFORE coding
""")
