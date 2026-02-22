"""
Exercise 6.2: Sorting Algorithms

SORTING ALGORITHMS
==================

Sorting is one of the most fundamental problems in computer science.
Understanding different sorting algorithms teaches you about
trade-offs, time complexity, and algorithm design patterns.

===================================
COMPARISON OF SORTING ALGORITHMS
===================================

    Algorithm       Best      Average    Worst     Space    Stable?
    ---------------------------------------------------------------
    Bubble Sort     O(n)      O(n²)      O(n²)     O(1)     Yes
    Selection Sort  O(n²)     O(n²)      O(n²)     O(1)     No
    Insertion Sort  O(n)      O(n²)      O(n²)     O(1)     Yes
    Merge Sort      O(n log n) O(n log n) O(n log n) O(n)   Yes
    Quick Sort      O(n log n) O(n log n) O(n²)     O(log n) No

    Stable = equal elements maintain their original order

===================================
KEY CONCEPTS
===================================

BUBBLE SORT: Compare adjacent pairs, swap if out of order. Repeat.
    Like bubbles rising - largest values "bubble" to the end.

SELECTION SORT: Find the minimum, put it first. Find next minimum, etc.
    Select the smallest remaining element each pass.

INSERTION SORT: Build sorted portion one element at a time.
    Like sorting cards in your hand - insert each card in the right spot.

MERGE SORT: Divide array in half, sort each half, merge them back.
    Divide and conquer. Always O(n log n) but uses extra memory.

===================================
EXAMPLE: Merge Sort Step by Step
===================================

    [38, 27, 43, 3, 9, 82, 10]

    Split: [38, 27, 43] and [3, 9, 82, 10]
    Split: [38] [27, 43] and [3, 9] [82, 10]
    Split: [38] [27] [43] and [3] [9] [82] [10]

    Merge: [27, 38] [43] and [3, 9] [10, 82]
    Merge: [27, 38, 43] and [3, 9, 10, 82]
    Merge: [3, 9, 10, 27, 38, 43, 82]

===================================
EXERCISE
===================================

PART 1: Bubble Sort

Implement bubble sort.

    def bubble_sort(arr: list) -> list:
        Return a NEW sorted list (don't modify the original).

    How it works:
    1. Walk through the array comparing adjacent elements
    2. Swap if they're in the wrong order
    3. Repeat until no swaps needed

    Optimisation: If a pass has no swaps, the array is already sorted - stop early.

---

PART 2: Insertion Sort

Implement insertion sort.

    def insertion_sort(arr: list) -> list:
        Return a NEW sorted list.

    How it works:
    1. Start from the second element
    2. Compare it with elements to its left
    3. Shift larger elements right to make room
    4. Insert the element in its correct position

---

PART 3: Merge Sort

Implement merge sort using divide and conquer.

    def merge_sort(arr: list) -> list:
        Return a NEW sorted list.

    How it works:
    1. Base case: array of length 0 or 1 is already sorted
    2. Split array into two halves
    3. Recursively sort each half
    4. Merge the two sorted halves together

    You'll likely want a helper:
    def merge(left: list, right: list) -> list:
        Merge two sorted lists into one sorted list.

---

PART 4 (HARD): Quick Sort

Implement quick sort.

    def quick_sort(arr: list) -> list:
        Return a NEW sorted list.

    How it works:
    1. Base case: array of length 0 or 1
    2. Choose a pivot (last element is simplest)
    3. Partition: elements < pivot go left, elements > pivot go right
    4. Recursively sort left and right partitions
    5. Combine: sorted_left + [pivot] + sorted_right

ESTIMATED TIME: 45-60 minutes
"""


# ============================================
# PART 1: Bubble Sort
# ============================================

def bubble_sort(arr: list) -> list:
    """Return a new sorted list using bubble sort."""
    # YOUR CODE HERE
    pass


# ============================================
# PART 2: Insertion Sort
# ============================================

def insertion_sort(arr: list) -> list:
    """Return a new sorted list using insertion sort."""
    # YOUR CODE HERE
    pass


# ============================================
# PART 3: Merge Sort
# ============================================

def merge_sort(arr: list) -> list:
    """Return a new sorted list using merge sort."""
    # YOUR CODE HERE
    pass


# ============================================
# PART 4 (HARD): Quick Sort
# ============================================

def quick_sort(arr: list) -> list:
    """Return a new sorted list using quick sort."""
    # YOUR CODE HERE
    pass


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    # Shared test data
    test_cases = [
        ([], []),
        ([1], [1]),
        ([3, 1, 2], [1, 2, 3]),
        ([5, 2, 8, 1, 9, 3], [1, 2, 3, 5, 8, 9]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Already sorted
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Reverse sorted
        ([3, 3, 1, 1, 2, 2], [1, 1, 2, 2, 3, 3]),  # Duplicates
        ([42], [42]),  # Single element
    ]

    # ==========================================
    # PART 1 TESTS: Bubble Sort
    # ==========================================
    print("\n=== Test 1: Bubble Sort ===")
    try:
        for input_arr, expected in test_cases:
            result = bubble_sort(input_arr)
            assert result == expected, f"bubble_sort({input_arr}) = {result}, expected {expected}"
            assert input_arr == input_arr, "Original array should not be modified"

        print("  All bubble sort tests passed")
        print("Test 1 PASSED!")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")
    except Exception as e:
        print(f"Test 1 ERROR: {e}")

    # ==========================================
    # PART 2 TESTS: Insertion Sort
    # ==========================================
    print("\n=== Test 2: Insertion Sort ===")
    try:
        for input_arr, expected in test_cases:
            result = insertion_sort(input_arr)
            assert result == expected, f"insertion_sort({input_arr}) = {result}, expected {expected}"

        print("  All insertion sort tests passed")
        print("Test 2 PASSED!")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 ERROR: {e}")

    # ==========================================
    # PART 3 TESTS: Merge Sort
    # ==========================================
    print("\n=== Test 3: Merge Sort ===")
    try:
        for input_arr, expected in test_cases:
            result = merge_sort(input_arr)
            assert result == expected, f"merge_sort({input_arr}) = {result}, expected {expected}"

        print("  All merge sort tests passed")
        print("Test 3 PASSED!")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 ERROR: {e}")

    # ==========================================
    # PART 4 TESTS (HARD): Quick Sort
    # ==========================================

    # Uncomment when ready:

    # print("\n=== Test 4: Quick Sort ===")
    # try:
    #     for input_arr, expected in test_cases:
    #         result = quick_sort(input_arr)
    #         assert result == expected, f"quick_sort({input_arr}) = {result}, expected {expected}"
    #
    #     print("  All quick sort tests passed")
    #     print("Test 4 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 4 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 4 ERROR: {e}")

    print("\n" + "=" * 60)
    print("SORTING KEY LESSONS")
    print("=" * 60)
    print("""
1. O(n²) sorts (bubble, insertion, selection) are simple but slow
2. O(n log n) sorts (merge, quick) are fast but more complex
3. Merge sort: always O(n log n) but uses O(n) extra space
4. Quick sort: O(n log n) average but O(n²) worst case
5. Insertion sort is actually fast for NEARLY sorted data
6. Python's built-in sorted() uses Timsort: O(n log n), stable
7. In practice, use sorted() - implement these to LEARN
""")
    print("=" * 60)
