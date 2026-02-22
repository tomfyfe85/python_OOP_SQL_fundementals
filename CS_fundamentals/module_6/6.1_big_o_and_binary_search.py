"""
Exercise 6.1: Big O Notation and Binary Search

BIG O NOTATION
==============

Big O describes how an algorithm's performance scales with input size.
It answers: "As the input gets bigger, how much slower does this get?"

===================================
COMMON TIME COMPLEXITIES (fastest to slowest)
===================================

    O(1)        Constant    - Doesn't grow with input
                              dict lookup, array index access

    O(log n)    Logarithmic - Halves the problem each step
                              binary search

    O(n)        Linear      - Visits every element once
                              linear search, single loop

    O(n log n)  Linearithmic - Best comparison sorting
                              merge sort, Python's sorted()

    O(n²)       Quadratic   - Nested loops
                              bubble sort, brute force pairs

    O(2^n)      Exponential - Doubles with each element
                              naive recursion (Fibonacci)

===================================
HOW TO DETERMINE BIG O
===================================

Rules of thumb:
1. Drop constants: O(2n) -> O(n)
2. Drop lower terms: O(n² + n) -> O(n²)
3. Single loop over input: O(n)
4. Nested loops over input: O(n²)
5. Halving the input each step: O(log n)
6. Doing O(n) work O(log n) times: O(n log n)

===================================
SEARCHING
===================================

LINEAR SEARCH: Check every element. O(n).
    Good for: unsorted data, small lists

BINARY SEARCH: Halve the search space each step. O(log n).
    Requires: SORTED data
    Much faster for large datasets

===================================
EXAMPLE: Binary Search (Iterative)
===================================

    def binary_search(arr, target):
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                return mid          # Found it!
            elif arr[mid] < target:
                left = mid + 1      # Target is in right half
            else:
                right = mid - 1     # Target is in left half

        return -1  # Not found

    # Trace: binary_search([1, 3, 5, 7, 9, 11], 7)
    # left=0, right=5, mid=2 -> arr[2]=5 < 7 -> left=3
    # left=3, right=5, mid=4 -> arr[4]=9 > 7 -> right=3
    # left=3, right=3, mid=3 -> arr[3]=7 == 7 -> return 3!

===================================
EXERCISE
===================================

PART 1: Identify Time Complexity

For each function below, determine its Big O time complexity.
Fill in the return value with the correct string.

---

PART 2: Implement Binary Search

Implement both iterative and recursive versions.

Function: binary_search_iterative(arr: list[int], target: int) -> int
    Return the INDEX of target in sorted arr, or -1 if not found.

Function: binary_search_recursive(arr: list[int], target: int) -> int
    Same as above but using recursion.
    Hint: You'll need a helper with left/right parameters.

---

PART 3 (HARD): Search Variations

Function: find_first_occurrence(arr: list[int], target: int) -> int
    In a sorted array with DUPLICATES, find the index of the FIRST
    occurrence of target. Return -1 if not found.
    Example: [1, 2, 2, 2, 3, 4] target=2 -> return 1 (not 2 or 3)

Function: find_insertion_point(arr: list[int], target: int) -> int
    Return the index where target should be inserted to keep arr sorted.
    If target exists, return the index of the first occurrence.
    Example: [1, 3, 5, 7] target=4 -> return 2
    Example: [1, 3, 5, 7] target=5 -> return 2

ESTIMATED TIME: 30-45 minutes
"""


# ============================================
# PART 1: Identify Time Complexity
# ============================================

def complexity_1(arr):
    """What is the Big O of this function?"""
    return arr[0] if arr else None

def answer_1() -> str:
    # YOUR ANSWER: return one of "O(1)", "O(log n)", "O(n)", "O(n^2)"
    pass


def complexity_2(arr):
    """What is the Big O of this function?"""
    total = 0
    for item in arr:
        total += item
    return total

def answer_2() -> str:
    pass


def complexity_3(arr):
    """What is the Big O of this function?"""
    for i in arr:
        for j in arr:
            print(i, j)

def answer_3() -> str:
    pass


def complexity_4(n):
    """What is the Big O of this function?"""
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count

def answer_4() -> str:
    pass


def complexity_5(arr):
    """What is the Big O of this function?"""
    total = 0
    for item in arr:
        total += item
    for i in arr:
        for j in arr:
            total += i * j
    return total

def answer_5() -> str:
    # Hint: remember the rule about dropping lower terms
    pass


# ============================================
# PART 2: Binary Search
# ============================================

def binary_search_iterative(arr: list[int], target: int) -> int:
    """Return index of target in sorted arr, or -1 if not found."""
    # YOUR CODE HERE
    pass


def binary_search_recursive(arr: list[int], target: int) -> int:
    """Return index of target in sorted arr, or -1 if not found. Use recursion."""
    # YOUR CODE HERE
    # Hint: Define a helper function with left, right parameters
    pass


# ============================================
# PART 3 (HARD): Search Variations
# ============================================

def find_first_occurrence(arr: list[int], target: int) -> int:
    """Return index of FIRST occurrence of target in sorted arr with duplicates."""
    # YOUR CODE HERE
    pass


def find_insertion_point(arr: list[int], target: int) -> int:
    """Return index where target should be inserted to keep arr sorted."""
    # YOUR CODE HERE
    pass


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    # ==========================================
    # PART 1 TESTS: Big O Identification
    # ==========================================
    print("\n=== Test 1: Big O Identification ===")
    try:
        assert answer_1() == "O(1)", f"complexity_1 is not {answer_1()}"
        assert answer_2() == "O(n)", f"complexity_2 is not {answer_2()}"
        assert answer_3() == "O(n^2)", f"complexity_3 is not {answer_3()}"
        assert answer_4() == "O(log n)", f"complexity_4 is not {answer_4()}"
        assert answer_5() == "O(n^2)", f"complexity_5 is not {answer_5()}"

        print("  All Big O answers correct!")
        print("Test 1 PASSED!")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")
    except Exception as e:
        print(f"Test 1 ERROR: {e}")

    # ==========================================
    # PART 2 TESTS: Binary Search
    # ==========================================
    print("\n=== Test 2: Binary Search (Iterative) ===")
    try:
        arr = [1, 3, 5, 7, 9, 11, 13]

        assert binary_search_iterative(arr, 7) == 3
        assert binary_search_iterative(arr, 1) == 0   # First element
        assert binary_search_iterative(arr, 13) == 6   # Last element
        assert binary_search_iterative(arr, 4) == -1   # Not found
        assert binary_search_iterative([], 5) == -1    # Empty array
        assert binary_search_iterative([5], 5) == 0    # Single element found
        assert binary_search_iterative([5], 3) == -1   # Single element not found

        print("  Iterative binary search works")
        print("Test 2 PASSED!")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 ERROR: {e}")

    print("\n=== Test 3: Binary Search (Recursive) ===")
    try:
        arr = [1, 3, 5, 7, 9, 11, 13]

        assert binary_search_recursive(arr, 7) == 3
        assert binary_search_recursive(arr, 1) == 0
        assert binary_search_recursive(arr, 13) == 6
        assert binary_search_recursive(arr, 4) == -1
        assert binary_search_recursive([], 5) == -1
        assert binary_search_recursive([5], 5) == 0

        print("  Recursive binary search works")
        print("Test 3 PASSED!")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 ERROR: {e}")

    # ==========================================
    # PART 3 TESTS (HARD): Uncomment when ready
    # ==========================================

    # print("\n=== Test 4: Find First Occurrence ===")
    # try:
    #     assert find_first_occurrence([1, 2, 2, 2, 3, 4], 2) == 1
    #     assert find_first_occurrence([1, 1, 1, 1], 1) == 0
    #     assert find_first_occurrence([1, 2, 3, 4, 5], 3) == 2
    #     assert find_first_occurrence([1, 2, 3], 4) == -1
    #     assert find_first_occurrence([], 1) == -1
    #     assert find_first_occurrence([5, 5, 5, 5, 5], 5) == 0
    #
    #     print("  First occurrence found correctly")
    #     print("Test 4 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 4 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 4 ERROR: {e}")

    # print("\n=== Test 5: Find Insertion Point ===")
    # try:
    #     assert find_insertion_point([1, 3, 5, 7], 4) == 2
    #     assert find_insertion_point([1, 3, 5, 7], 0) == 0
    #     assert find_insertion_point([1, 3, 5, 7], 8) == 4
    #     assert find_insertion_point([1, 3, 5, 7], 5) == 2
    #     assert find_insertion_point([], 5) == 0
    #     assert find_insertion_point([2, 2, 2], 2) == 0
    #
    #     print("  Insertion point found correctly")
    #     print("Test 5 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 5 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 5 ERROR: {e}")

    print("\n" + "=" * 60)
    print("BIG O & BINARY SEARCH KEY LESSONS")
    print("=" * 60)
    print("""
1. Big O describes SCALABILITY, not exact speed
2. Drop constants and lower-order terms
3. Binary search: O(log n) - halves the problem each step
4. Binary search REQUIRES sorted data
5. log₂(1,000,000) ≈ 20 steps vs 1,000,000 for linear search!
6. Two versions: iterative (while loop) and recursive (helper function)
""")
    print("=" * 60)
