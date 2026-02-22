"""
Exercise 6.3: Recursion and Memoization

RECURSION
=========

A function that calls itself to solve smaller versions of the same problem.

Every recursive function needs:
1. BASE CASE: When to stop (prevents infinite recursion)
2. RECURSIVE CASE: Break the problem into a smaller version

===================================
EXAMPLE: Factorial
===================================

    5! = 5 × 4 × 3 × 2 × 1 = 120

    Recursive definition:
    - factorial(0) = 1           (base case)
    - factorial(n) = n × factorial(n-1)  (recursive case)

    def factorial(n):
        if n == 0:          # Base case
            return 1
        return n * factorial(n - 1)  # Recursive case

    Call stack:
    factorial(5) -> 5 * factorial(4)
                        4 * factorial(3)
                            3 * factorial(2)
                                2 * factorial(1)
                                    1 * factorial(0)
                                        return 1
                                    return 1
                                return 2
                            return 6
                        return 24
                    return 120

===================================
THE PROBLEM WITH NAIVE RECURSION
===================================

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    This is O(2^n)! fibonacci(40) makes over a BILLION calls.

    fib(5) calls fib(4) and fib(3)
    fib(4) calls fib(3) and fib(2)    <- fib(3) calculated TWICE!
    fib(3) calls fib(2) and fib(1)    <- fib(2) calculated THREE times!

    The same subproblems are solved over and over.

===================================
MEMOIZATION: The Fix
===================================

    Cache results of previous calls. If we've seen this input before,
    return the cached result instead of recalculating.

    def fibonacci_memo(n, cache={}):
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        cache[n] = fibonacci_memo(n-1, cache) + fibonacci_memo(n-2, cache)
        return cache[n]

    Now it's O(n) - each subproblem calculated only ONCE.

===================================
EXERCISE
===================================

PART 1: Basic Recursion

Implement these functions recursively (no loops!):

    def factorial(n: int) -> int:
        Return n! (n factorial).
        factorial(0) = 1, factorial(5) = 120

    def sum_list(arr: list[int]) -> int:
        Return the sum of all elements using recursion.
        Base case: empty list -> 0
        Recursive: first element + sum of rest

    def reverse_string(s: str) -> str:
        Reverse a string using recursion.
        Base case: empty string or single char -> return as is
        Recursive: last char + reverse of everything except last

---

PART 2: Fibonacci Three Ways

Implement Fibonacci three different ways and compare:

    def fib_recursive(n: int) -> int:
        Naive recursive. O(2^n) - slow!

    def fib_iterative(n: int) -> int:
        Iterative with a loop. O(n) - fast.

    def fib_memo(n: int) -> int:
        Recursive with memoization. O(n) - fast.
        Use a dict to cache results.

    fib(0) = 0, fib(1) = 1, fib(2) = 1, fib(3) = 2,
    fib(4) = 3, fib(5) = 5, fib(10) = 55

---

PART 3 (HARD): Recursive Challenges

    def flatten(nested: list) -> list:
        Flatten a nested list into a single list.
        [1, [2, [3, 4], 5], 6] -> [1, 2, 3, 4, 5, 6]
        Hint: If element is a list, recursively flatten it.

    def power(base: int, exp: int) -> int:
        Calculate base^exp using recursion.
        Use the "fast exponentiation" trick:
        - If exp is even: base^exp = (base^(exp//2))²
        - If exp is odd: base^exp = base × base^(exp-1)
        This makes it O(log n) instead of O(n)!

ESTIMATED TIME: 30-45 minutes
"""


# ============================================
# PART 1: Basic Recursion
# ============================================

def factorial(n: int) -> int:
    """Return n! using recursion."""
    # YOUR CODE HERE
    pass


def sum_list(arr: list[int]) -> int:
    """Return sum of all elements using recursion."""
    # YOUR CODE HERE
    pass


def reverse_string(s: str) -> str:
    """Reverse a string using recursion."""
    # YOUR CODE HERE
    pass


# ============================================
# PART 2: Fibonacci Three Ways
# ============================================

def fib_recursive(n: int) -> int:
    """Naive recursive Fibonacci. O(2^n)."""
    # YOUR CODE HERE
    pass


def fib_iterative(n: int) -> int:
    """Iterative Fibonacci. O(n)."""
    # YOUR CODE HERE
    pass


def fib_memo(n: int) -> int:
    """Memoized recursive Fibonacci. O(n)."""
    # YOUR CODE HERE
    pass


# ============================================
# PART 3 (HARD): Recursive Challenges
# ============================================

def flatten(nested: list) -> list:
    """Flatten a nested list into a single list."""
    # YOUR CODE HERE
    pass


def power(base: int, exp: int) -> int:
    """Calculate base^exp using fast exponentiation. O(log n)."""
    # YOUR CODE HERE
    pass


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    # ==========================================
    # PART 1 TESTS: Basic Recursion
    # ==========================================
    print("\n=== Test 1: Factorial ===")
    try:
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120
        assert factorial(10) == 3628800

        print("  Factorial works")
        print("Test 1 PASSED!")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")
    except Exception as e:
        print(f"Test 1 ERROR: {e}")

    print("\n=== Test 2: Sum List ===")
    try:
        assert sum_list([]) == 0
        assert sum_list([5]) == 5
        assert sum_list([1, 2, 3, 4, 5]) == 15
        assert sum_list([-1, 1]) == 0

        print("  Sum list works")
        print("Test 2 PASSED!")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 ERROR: {e}")

    print("\n=== Test 3: Reverse String ===")
    try:
        assert reverse_string("") == ""
        assert reverse_string("a") == "a"
        assert reverse_string("hello") == "olleh"
        assert reverse_string("abcde") == "edcba"

        print("  Reverse string works")
        print("Test 3 PASSED!")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 ERROR: {e}")

    # ==========================================
    # PART 2 TESTS: Fibonacci
    # ==========================================
    fib_expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    print("\n=== Test 4: Fibonacci (Recursive) ===")
    try:
        for i, expected in enumerate(fib_expected):
            assert fib_recursive(i) == expected, f"fib_recursive({i}) should be {expected}"

        print("  Recursive Fibonacci works (but slow for large n!)")
        print("Test 4 PASSED!")
    except AssertionError as e:
        print(f"Test 4 FAILED: {e}")
    except Exception as e:
        print(f"Test 4 ERROR: {e}")

    print("\n=== Test 5: Fibonacci (Iterative) ===")
    try:
        for i, expected in enumerate(fib_expected):
            assert fib_iterative(i) == expected, f"fib_iterative({i}) should be {expected}"

        # This one can handle large inputs
        assert fib_iterative(50) == 12586269025

        print("  Iterative Fibonacci works (fast!)")
        print("Test 5 PASSED!")
    except AssertionError as e:
        print(f"Test 5 FAILED: {e}")
    except Exception as e:
        print(f"Test 5 ERROR: {e}")

    print("\n=== Test 6: Fibonacci (Memoized) ===")
    try:
        for i, expected in enumerate(fib_expected):
            assert fib_memo(i) == expected, f"fib_memo({i}) should be {expected}"

        # This one can also handle large inputs
        assert fib_memo(50) == 12586269025

        print("  Memoized Fibonacci works (fast too!)")
        print("Test 6 PASSED!")
    except AssertionError as e:
        print(f"Test 6 FAILED: {e}")
    except Exception as e:
        print(f"Test 6 ERROR: {e}")

    # ==========================================
    # PART 3 TESTS (HARD): Uncomment when ready
    # ==========================================

    # print("\n=== Test 7: Flatten ===")
    # try:
    #     assert flatten([1, 2, 3]) == [1, 2, 3]
    #     assert flatten([1, [2, 3], 4]) == [1, 2, 3, 4]
    #     assert flatten([1, [2, [3, 4], 5], 6]) == [1, 2, 3, 4, 5, 6]
    #     assert flatten([]) == []
    #     assert flatten([[[[1]]]]) == [1]
    #     assert flatten([1, [], [2, []], 3]) == [1, 2, 3]
    #
    #     print("  Flatten works")
    #     print("Test 7 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 7 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 7 ERROR: {e}")

    # print("\n=== Test 8: Fast Power ===")
    # try:
    #     assert power(2, 0) == 1
    #     assert power(2, 1) == 2
    #     assert power(2, 10) == 1024
    #     assert power(3, 5) == 243
    #     assert power(5, 3) == 125
    #     assert power(2, 20) == 1048576
    #
    #     print("  Fast power works in O(log n)")
    #     print("Test 8 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 8 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 8 ERROR: {e}")

    print("\n" + "=" * 60)
    print("RECURSION KEY LESSONS")
    print("=" * 60)
    print("""
1. Every recursion needs a BASE CASE and a RECURSIVE CASE
2. The call stack tracks where you are in nested calls
3. Naive recursion can be O(2^n) - exponentially slow
4. Memoization caches results: O(2^n) -> O(n)
5. Iterative solutions avoid stack overflow for deep recursion
6. Use recursion when the problem has a natural recursive structure
7. Fibonacci three ways demonstrates the performance difference
""")
    print("=" * 60)
