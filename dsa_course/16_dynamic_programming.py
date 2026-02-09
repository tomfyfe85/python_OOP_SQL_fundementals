"""
DSA Course - Module 16: Dynamic Programming
===========================================

CONCEPT: Dynamic Programming (DP)
---------------------------------
Break a problem into overlapping subproblems, solve each once,
store results to avoid recomputation.

DP vs DIVIDE & CONQUER:
- D&C: subproblems are independent (no overlap)
- DP: subproblems overlap (same subproblem solved multiple times)

TWO APPROACHES:

1. TOP-DOWN (Memoization):
   - Recursive solution with caching
   - Compute on demand, store in memo dict/array
   - More intuitive, matches recursive thinking

2. BOTTOM-UP (Tabulation):
   - Build solution iteratively from smallest subproblems
   - Fill a table in order of dependencies
   - Often more efficient (no recursion overhead)

THE FRAMEWORK:
1. Define state: What information do we need to describe a subproblem?
2. Define recurrence: How do we compute state from smaller states?
3. Define base cases: What are the simplest subproblems?
4. Define answer: Which state(s) give us the final answer?
5. Determine order: In what order should we compute states?

COMMON PATTERNS:
- 1D DP: dp[i] depends on previous dp values
- 2D DP: dp[i][j] for strings, grids, ranges
- State machine: dp[i][state] for problems with modes/states
- Knapsack: subset selection with constraints

TIME/SPACE ANALYSIS:
- Time: O(number of states × time per state)
- Space: O(number of states), often reducible
"""


# ============================================
# EXAMPLE: Fibonacci (Classic DP Intro)
# ============================================

def fib_memo(n: int, memo: dict = None) -> int:
    """
    Fibonacci with memoization (top-down DP).

    F(n) = F(n-1) + F(n-2)
    F(0) = 0, F(1) = 1

    Without memo: O(2^n) - exponential!
    With memo: O(n) - each subproblem computed once
    """
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_tabulation(n: int) -> int:
    """
    Fibonacci with tabulation (bottom-up DP).

    Build table from F(0) to F(n).
    """
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def fib_optimized(n: int) -> int:
    """
    Fibonacci with O(1) space.

    We only need previous two values, not entire table.
    """
    if n <= 1:
        return n

    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr

    return prev1


# ============================================
# QUESTION 1: Climbing Stairs
# ============================================

"""
PROBLEM: How many distinct ways to climb n stairs?

You can climb 1 or 2 steps at a time.

Examples:
- n=2 -> 2 ways: (1+1) or (2)
- n=3 -> 3 ways: (1+1+1), (1+2), (2+1)
- n=4 -> 5 ways: (1+1+1+1), (1+1+2), (1+2+1), (2+1+1), (2+2)

Implement the function below:
"""


def climb_stairs(n: int) -> int:
    """Return number of distinct ways to climb n stairs."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2: House Robber
# ============================================

"""
PROBLEM: Maximum money from robbing houses (can't rob adjacent).

Given an array of non-negative integers representing money in each house,
find the maximum amount you can rob without robbing adjacent houses.

Examples:
- [1,2,3,1] -> 4 (rob houses 0 and 2: 1+3=4)
- [2,7,9,3,1] -> 12 (rob houses 0, 2, 4: 2+9+1=12)
- [2,1,1,2] -> 4 (rob houses 0 and 3: 2+2=4)

Implement the function below:
"""


def rob(nums: list[int]) -> int:
    """Return maximum money that can be robbed."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 3: Coin Change (Minimum Coins)
# ============================================

"""
PROBLEM: Minimum number of coins to make up an amount.

Given coin denominations and a target amount, find the fewest
coins needed. Return -1 if not possible.

Examples:
- coins=[1,2,5], amount=11 -> 3 (5+5+1)
- coins=[2], amount=3 -> -1 (impossible)
- coins=[1], amount=0 -> 0

Implement the function below:
"""


def coin_change(coins: list[int], amount: int) -> int:
    """Return minimum coins needed, or -1 if impossible."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 4: Longest Increasing Subsequence
# ============================================

"""
PROBLEM: Find the length of the longest strictly increasing subsequence.

A subsequence doesn't have to be contiguous, but must maintain relative order.

Examples:
- [10,9,2,5,3,7,101,18] -> 4 (subsequence [2,3,7,101] or [2,5,7,101])
- [0,1,0,3,2,3] -> 4 (subsequence [0,1,2,3])
- [7,7,7,7,7] -> 1 (all same, length 1)

Note: There's also an O(n log n) solution using binary search,
but the O(n^2) DP solution is easier to understand.

Implement the function below:
"""


def length_of_lis(nums: list[int]) -> int:
    """Return length of longest increasing subsequence."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 5: Unique Paths in Grid
# ============================================

"""
PROBLEM: Count unique paths from top-left to bottom-right.

In an m x n grid, you can only move right or down.
How many unique paths are there?

Examples:
- m=3, n=7 -> 28
- m=3, n=2 -> 3 (Right-Down-Down, Down-Right-Down, Down-Down-Right)
- m=1, n=1 -> 1

Implement the function below:
"""


def unique_paths(m: int, n: int) -> int:
    """Return number of unique paths in m x n grid."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 16: Dynamic Programming")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Fibonacci ---")
    assert fib_memo(10) == 55
    assert fib_tabulation(10) == 55
    assert fib_optimized(10) == 55
    assert fib_memo(0) == 0
    assert fib_memo(1) == 1
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Climbing Stairs ---")
    try:
        assert climb_stairs(2) == 2
        assert climb_stairs(3) == 3
        assert climb_stairs(4) == 5
        assert climb_stairs(1) == 1
        assert climb_stairs(5) == 8
        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: House Robber ---")
    try:
        assert rob([1, 2, 3, 1]) == 4
        assert rob([2, 7, 9, 3, 1]) == 12
        assert rob([2, 1, 1, 2]) == 4
        assert rob([1]) == 1
        assert rob([1, 2]) == 2
        assert rob([]) == 0
        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    # Test Question 3
    print("\n--- Question 3: Coin Change ---")
    try:
        assert coin_change([1, 2, 5], 11) == 3
        assert coin_change([2], 3) == -1
        assert coin_change([1], 0) == 0
        assert coin_change([1], 1) == 1
        assert coin_change([1, 2, 5], 100) == 20
        print("All Question 3 tests PASSED!")
    except AssertionError as e:
        print(f"Question 3 FAILED: {e}")
    except Exception as e:
        print(f"Question 3 ERROR: {e}")

    # Test Question 4
    print("\n--- Question 4: Longest Increasing Subsequence ---")
    try:
        assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
        assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
        assert length_of_lis([7, 7, 7, 7, 7]) == 1
        assert length_of_lis([1, 2, 3, 4, 5]) == 5
        assert length_of_lis([5, 4, 3, 2, 1]) == 1
        print("All Question 4 tests PASSED!")
    except AssertionError as e:
        print(f"Question 4 FAILED: {e}")
    except Exception as e:
        print(f"Question 4 ERROR: {e}")

    # Test Question 5
    print("\n--- Question 5: Unique Paths ---")
    try:
        assert unique_paths(3, 7) == 28
        assert unique_paths(3, 2) == 3
        assert unique_paths(1, 1) == 1
        assert unique_paths(2, 2) == 2
        assert unique_paths(3, 3) == 6
        # Edge cases
        assert unique_paths(1, 5) == 1, "Single row"
        assert unique_paths(5, 1) == 1, "Single column"
        print("All Question 5 tests PASSED!")
    except AssertionError as e:
        print(f"Question 5 FAILED: {e}")
    except Exception as e:
        print(f"Question 5 ERROR: {e}")

    # ==========================================
    # REVISION: Module 15 (Divide & Conquer)
    # ==========================================
    print("\n--- REVISION: Divide & Conquer ---")
    print("Q: What are the three steps of divide and conquer?")
    print("A: Divide (split problem), Conquer (solve recursively), Combine (merge results).")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. DP = recursion + memoization, or bottom-up tabulation
2. Identify: state (what info describes subproblem?), recurrence, base cases
3. Top-down: natural recursive thinking, cache results
4. Bottom-up: fill table in dependency order, often more efficient
5. Space optimization: if dp[i] only depends on recent values, reduce space
""")