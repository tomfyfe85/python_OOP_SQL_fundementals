"""
DSA Course - Module 13: Greedy Algorithms
=========================================

CONCEPT: Greedy Approach
------------------------
Make the locally optimal choice at each step, hoping it leads to
a globally optimal solution.

THE GREEDY PATTERN:
1. Define what "greedy choice" means for the problem
2. Prove (or trust) that greedy leads to optimal
3. Make the greedy choice
4. Reduce to a smaller subproblem
5. Repeat

WHEN GREEDY WORKS:
- Problem has "optimal substructure" (optimal solution contains optimal subsolutions)
- Problem has "greedy choice property" (local optimum leads to global optimum)

COMMON GREEDY PROBLEMS:
- Activity/interval selection (choose earliest ending)
- Fractional knapsack (choose best value/weight ratio)
- Huffman coding (combine smallest frequencies)
- Dijkstra's shortest path (choose closest unvisited)
- Minimum spanning tree (Kruskal's, Prim's)

WARNING:
Not all problems can be solved greedily! Counterexample:
- 0/1 Knapsack: greedy fails, need dynamic programming
- Coin change with arbitrary denominations

PROVING GREEDY WORKS:
- "Exchange argument": show swapping any choice for greedy choice doesn't worsen solution
- "Greedy stays ahead": show greedy is always at least as good at each step
"""


# ============================================
# EXAMPLE: Activity Selection
# ============================================

def activity_selection_example(activities: list[list[int]]) -> int:
    """
    Maximum number of non-overlapping activities.

    Given activities with [start, end] times, find maximum number
    that can be attended (no overlaps).

    Greedy insight: Always pick the activity that ENDS EARLIEST.
    This leaves maximum time for remaining activities.

    [[1,4],[3,5],[0,6],[5,7],[3,9],[5,9],[6,10],[8,11],[8,12],[2,14],[12,16]]
    -> 4 activities: [1,4], [5,7], [8,11], [12,16]
    """
    if not activities:
        return 0

    # Sort by END time (greedy: earliest end first)
    activities.sort(key=lambda x: x[1])

    count = 1
    last_end = activities[0][1]

    for i in range(1, len(activities)):
        start, end = activities[i]
        if start >= last_end:  # No overlap
            count += 1
            last_end = end

    return count


# Why earliest end time?
# If we pick activity A with end time E, we can't do anything during [start_A, E].
# The earlier E is, the more time remains for other activities.
#
# Trace: [[1,2], [2,3], [3,4], [1,3]]
# Sort by end: [[1,2], [1,3], [2,3], [3,4]]
#
# Pick [1,2], last_end=2, count=1
# [1,3]: start=1 < 2, skip (overlaps)
# [2,3]: start=2 >= 2, pick! last_end=3, count=2
# [3,4]: start=3 >= 3, pick! last_end=4, count=3
#
# Result: 3 activities


# ============================================
# QUESTION 1: Jump Game (Can Reach End?)
# ============================================

"""
PROBLEM: Can you reach the last index?

Given an array where nums[i] represents the maximum jump length from position i,
determine if you can reach the last index starting from index 0.

Examples:
- [2,3,1,1,4] -> True
  Start at 0 (value 2): can jump to 1 or 2
  Jump to 1 (value 3): can jump to 2, 3, or 4
  Reached index 4!

- [3,2,1,0,4] -> False
  All paths lead to index 3 (value 0), stuck!

- [0] -> True (already at last index)

HINT: Track the farthest index reachable.
      For each position (if reachable), update farthest.
      If farthest ever reaches or exceeds last index, return True.

      max_reach = 0
      for i in range(len(nums)):
          if i > max_reach:
              return False  # Can't reach this position
          max_reach = max(max_reach, i + nums[i])
          if max_reach >= len(nums) - 1:
              return True

Implement the function below:
"""


def can_jump(nums: list[int]) -> bool:
    """Return True if you can reach the last index."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2: Jump Game II (Minimum Jumps)
# ============================================

"""
PROBLEM: What's the minimum number of jumps to reach the end?

Given an array where nums[i] is the max jump length from position i,
return the minimum number of jumps to reach the last index.
Assume you can always reach the last index.

Examples:
- [2,3,1,1,4] -> 2
  Jump from 0->1 (length 1), then 1->4 (length 3)

- [2,3,0,1,4] -> 2
  Jump from 0->1, then 1->4

- [1,2,3] -> 2
  Jump 0->1, then 1->2

HINT: Greedy BFS-style approach.
      - Track current range [start, end] reachable with current jumps
      - From current range, find farthest we can reach (next range end)
      - When we need to go beyond current end, increment jumps

      jumps = 0
      current_end = 0
      farthest = 0

      for i in range(len(nums) - 1):  # Don't need to jump FROM last index
          farthest = max(farthest, i + nums[i])
          if i == current_end:  # Reached end of current jump's range
              jumps += 1
              current_end = farthest

Implement the function below:
"""


def min_jumps(nums: list[int]) -> int:
    """Return minimum number of jumps to reach last index."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 3: Gas Station
# ============================================

"""
PROBLEM: Can you complete a circuit of gas stations?

There are n gas stations in a circle. You have a car with unlimited tank.
- gas[i] = amount of gas at station i
- cost[i] = gas needed to travel from station i to i+1

Find the starting station index to complete the circuit, or -1 if impossible.
If a solution exists, it is guaranteed to be unique.

Examples:
- gas=[1,2,3,4,5], cost=[3,4,5,1,2] -> 3
  Start at station 3:
  Tank: 0+4=4, travel costs 1, arrive at 4 with 3
  Tank: 3+5=8, travel costs 2, arrive at 0 with 6
  Tank: 6+1=7, travel costs 3, arrive at 1 with 4
  Tank: 4+2=6, travel costs 4, arrive at 2 with 2
  Tank: 2+3=5, travel costs 5, arrive at 3 with 0 ✓

- gas=[2,3,4], cost=[3,4,3] -> -1
  Total gas (9) < total cost (10), impossible

HINT: Two key insights:
      1. If total gas < total cost, impossible
      2. If we fail at station j starting from i, then starting from
         any station between i and j will also fail.
         So try starting from j+1.

      total = 0
      tank = 0
      start = 0

      for i in range(len(gas)):
          gain = gas[i] - cost[i]
          total += gain
          tank += gain
          if tank < 0:  # Can't reach next station
              start = i + 1  # Try starting from next station
              tank = 0

      return start if total >= 0 else -1

Implement the function below:
"""


def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    """Return starting station index, or -1 if impossible."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 4: Task Scheduler
# ============================================

"""
PROBLEM: Minimum time to execute all tasks with cooldown.

Given tasks (letters A-Z) and cooldown n, find minimum time to execute all.
Same tasks must have at least n intervals between them.
Idle time counts as an interval.

Examples:
- tasks=["A","A","A","B","B","B"], n=2 -> 8
  A -> B -> idle -> A -> B -> idle -> A -> B
  (A's have 2 intervals between them)

- tasks=["A","A","A","B","B","B"], n=0 -> 6
  No cooldown needed: A,B,A,B,A,B or any order

- tasks=["A","A","A","A","A","A","B","C","D","E","F","G"], n=2 -> 16
  A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

HINT: Focus on the most frequent task.
      If most frequent task appears 'max_count' times,
      we need at least (max_count - 1) * (n + 1) + count_of_max_freq_tasks slots.

      Example: A,A,A,B,B,B with n=2
      max_count = 3 (both A and B appear 3 times)
      Minimum frame: (3-1) * (2+1) = 6 slots for spacing
      Plus count of tasks with max_count: 2
      Total: 6 + 2 = 8

      But if we have many different tasks, we might not need idle time.
      So answer = max(calculated_minimum, len(tasks))

Implement the function below:
"""


def least_interval(tasks: list[str], n: int) -> int:
    """Return minimum intervals to complete all tasks."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 13: Greedy Algorithms")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Activity Selection ---")
    assert activity_selection_example([[1, 2], [2, 3], [3, 4], [1, 3]]) == 3
    assert activity_selection_example([[1, 4], [3, 5], [0, 6], [5, 7], [3, 9], [5, 9], [6, 10], [8, 11], [8, 12], [2, 14], [12, 16]]) == 4
    assert activity_selection_example([]) == 0
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Jump Game (Can Reach?) ---")
    try:
        assert can_jump([2, 3, 1, 1, 4]) == True
        assert can_jump([3, 2, 1, 0, 4]) == False
        assert can_jump([0]) == True
        assert can_jump([2, 0, 0]) == True
        assert can_jump([1, 0, 1, 0]) == False
        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: Jump Game II (Min Jumps) ---")
    try:
        assert min_jumps([2, 3, 1, 1, 4]) == 2
        assert min_jumps([2, 3, 0, 1, 4]) == 2
        assert min_jumps([1, 2, 3]) == 2
        assert min_jumps([1]) == 0
        assert min_jumps([1, 1, 1, 1]) == 3
        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    # Test Question 3
    print("\n--- Question 3: Gas Station ---")
    try:
        assert can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
        assert can_complete_circuit([2, 3, 4], [3, 4, 3]) == -1
        assert can_complete_circuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]) == 4
        assert can_complete_circuit([2], [2]) == 0
        print("All Question 3 tests PASSED!")
    except AssertionError as e:
        print(f"Question 3 FAILED: {e}")
    except Exception as e:
        print(f"Question 3 ERROR: {e}")

    # Test Question 4
    print("\n--- Question 4: Task Scheduler ---")
    try:
        assert least_interval(["A", "A", "A", "B", "B", "B"], 2) == 8
        assert least_interval(["A", "A", "A", "B", "B", "B"], 0) == 6
        assert least_interval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2) == 16
        assert least_interval(["A"], 2) == 1
        # Edge cases
        assert least_interval(["A", "B"], 2) == 2, "Two different tasks"
        print("All Question 4 tests PASSED!")
    except AssertionError as e:
        print(f"Question 4 FAILED: {e}")
    except Exception as e:
        print(f"Question 4 ERROR: {e}")

    # ==========================================
    # REVISION: Module 12 (Merge Intervals)
    # ==========================================
    print("\n--- REVISION: Merge Intervals ---")
    print("Q: When do two intervals overlap?")
    print("A: When interval1.end >= interval2.start (after sorting by start).")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Greedy: make locally optimal choice at each step
2. Works when: local optimum leads to global optimum
3. Common strategy: sort by some criteria, then iterate
4. Activity selection: sort by end time, pick non-overlapping
5. Always verify greedy works! Some problems require DP instead
""")