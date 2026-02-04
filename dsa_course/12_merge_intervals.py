"""
DSA Course - Module 12: Merge Intervals
=======================================

CONCEPT: Interval Problems
--------------------------
An interval represents a range: [start, end].
Common operations: merge overlapping, find intersections, insert new intervals.

THE KEY INSIGHT:
Sort intervals by start time, then process sequentially.
After sorting, overlapping intervals are adjacent!

WHEN INTERVALS OVERLAP:
    Interval A: [1, 5]
    Interval B: [3, 7]

    |--A--|
       |--B--|
    1  3  5  7

    They overlap because A.end >= B.start

MERGE RULE:
    If intervals overlap: new interval = [min(starts), max(ends)]
    [1, 5] + [3, 7] = [1, 7]

COMMON PATTERNS:
1. Merge overlapping intervals
2. Insert interval into sorted list
3. Find intersection of two interval lists
4. Meeting rooms (count overlaps)

TIME COMPLEXITY:
- Sort: O(n log n)
- Process: O(n)
- Total: O(n log n)
"""


# ============================================
# EXAMPLE: Merge Overlapping Intervals
# ============================================

def merge_intervals_example(intervals: list[list[int]]) -> list[list[int]]:
    """
    Merge all overlapping intervals.

    [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
    [1,3] and [2,6] overlap -> merge to [1,6]

    Strategy:
    1. Sort by start time
    2. For each interval:
       - If overlaps with last merged: extend last merged
       - Otherwise: add as new interval
    """
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:  # Overlapping
            # Extend the last interval
            last[1] = max(last[1], current[1])
        else:
            # No overlap, add new interval
            merged.append(current)

    return merged


# Let's trace through: [[1,3],[2,6],[8,10],[15,18]]
#
# After sort (already sorted): [[1,3],[2,6],[8,10],[15,18]]
# merged = [[1,3]]
#
# Process [2,6]: 2 <= 3? Yes, overlap!
#   last[1] = max(3, 6) = 6
#   merged = [[1,6]]
#
# Process [8,10]: 8 <= 6? No, no overlap
#   merged = [[1,6], [8,10]]
#
# Process [15,18]: 15 <= 10? No, no overlap
#   merged = [[1,6], [8,10], [15,18]]
#
# Return [[1,6],[8,10],[15,18]]


# ============================================
# QUESTION 1: Insert Interval
# ============================================

"""
PROBLEM: Insert a new interval into a sorted list of non-overlapping intervals.

Given a sorted list of non-overlapping intervals and a new interval,
insert the new interval and merge if necessary. Return the result sorted.

Examples:
- intervals=[[1,3],[6,9]], newInterval=[2,5] -> [[1,5],[6,9]]
  [2,5] overlaps with [1,3] -> merge to [1,5]

- intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval=[4,8]
  -> [[1,2],[3,10],[12,16]]
  [4,8] overlaps with [3,5], [6,7], [8,10] -> merge all to [3,10]

- intervals=[], newInterval=[5,7] -> [[5,7]]

HINT: Process in three phases:
      1. Add all intervals that end BEFORE new interval starts
      2. Merge all overlapping intervals with new interval
      3. Add all intervals that start AFTER new interval ends

      Phase 2 (merging):
      while i < n and intervals[i][0] <= newInterval[1]:
          newInterval[0] = min(newInterval[0], intervals[i][0])
          newInterval[1] = max(newInterval[1], intervals[i][1])
          i += 1

Implement the function below:
"""


def insert_interval(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    """Insert new interval and merge if necessary."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2: Meeting Rooms (Can Attend All?)
# ============================================

"""
PROBLEM: Can a person attend all meetings?

Given an array of meeting time intervals where intervals[i] = [start, end],
determine if a person could attend all meetings (no overlaps).

Examples:
- [[0,30],[5,10],[15,20]] -> False
  [0,30] overlaps with [5,10] and [15,20]

- [[7,10],[2,4]] -> True
  After sorting: [2,4], [7,10] - no overlap

- [[1,5],[5,10]] -> True
  End of first = start of second is OK (not overlapping)

HINT: Sort by start time, then check if any meeting starts before previous ends.

      for i in range(1, len(intervals)):
          if intervals[i][0] < intervals[i-1][1]:
              return False  # Overlap!

Implement the function below:
"""


def can_attend_all(intervals: list[list[int]]) -> bool:
    """Return True if all meetings can be attended (no overlaps)."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 3: Meeting Rooms II (Minimum Rooms)
# ============================================

"""
PROBLEM: Find the minimum number of meeting rooms required.

Given an array of meeting intervals, find the minimum number of rooms
needed so all meetings can happen (some may need to run in parallel).

Examples:
- [[0,30],[5,10],[15,20]] -> 2
  Timeline:
  Room 1: [0--------------------30]
  Room 2:      [5--10]  [15--20]
  We need 2 rooms because [0,30] overlaps with others.

- [[7,10],[2,4]] -> 1
  No overlap, 1 room suffices.

- [[1,5],[5,10]] -> 1
  End=start is not overlap, back-to-back meetings work.

- [[1,4],[2,5],[3,6]] -> 3
  All three overlap at time 3, need 3 rooms.

HINT: Think of it as counting maximum concurrent meetings.
      Use "sweep line" technique:
      1. Create events: +1 for start, -1 for end
      2. Sort events (if same time, process ends before starts)
      3. Sweep through, track running count
      4. Maximum count = rooms needed

      Alternative: Use a min-heap of end times
      - For each meeting, if it can use an existing room (heap top <= start),
        pop that room and push new end time
      - Otherwise, add a new room (push end time)
      - Heap size = rooms needed

Implement the function below:
"""


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    """Return minimum number of meeting rooms required."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 4: Interval List Intersections
# ============================================

"""
PROBLEM: Find intersection of two lists of intervals.

Given two lists of CLOSED intervals (sorted and disjoint within each list),
return the intersection of these two interval lists.

Examples:
- firstList=[[0,2],[5,10],[13,23],[24,25]]
  secondList=[[1,5],[8,12],[15,24],[25,26]]
  -> [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

  [0,2] ∩ [1,5] = [1,2]
  [5,10] ∩ [1,5] = [5,5]
  [5,10] ∩ [8,12] = [8,10]
  etc.

HINT: Use two pointers, one for each list.

      Intersection exists if: max(start1, start2) <= min(end1, end2)
      If so, intersection = [max(starts), min(ends)]

      After processing, advance the pointer for whichever interval ends first.

      while i < len(first) and j < len(second):
          lo = max(first[i][0], second[j][0])
          hi = min(first[i][1], second[j][1])
          if lo <= hi:
              result.append([lo, hi])
          if first[i][1] < second[j][1]:
              i += 1
          else:
              j += 1

Implement the function below:
"""


def interval_intersection(firstList: list[list[int]],
                          secondList: list[list[int]]) -> list[list[int]]:
    """Return intersection of two interval lists."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 12: Merge Intervals")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Merge Overlapping Intervals ---")
    assert merge_intervals_example([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge_intervals_example([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge_intervals_example([[1, 4], [0, 4]]) == [[0, 4]]
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Insert Interval ---")
    try:
        assert insert_interval([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
        assert insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
        assert insert_interval([], [5, 7]) == [[5, 7]]
        assert insert_interval([[1, 5]], [2, 3]) == [[1, 5]]
        assert insert_interval([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: Meeting Rooms (Can Attend All?) ---")
    try:
        assert can_attend_all([[0, 30], [5, 10], [15, 20]]) == False
        assert can_attend_all([[7, 10], [2, 4]]) == True
        assert can_attend_all([[1, 5], [5, 10]]) == True  # End=start OK
        assert can_attend_all([[1, 5]]) == True
        assert can_attend_all([]) == True
        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    # Test Question 3
    print("\n--- Question 3: Meeting Rooms II (Min Rooms) ---")
    try:
        assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
        assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
        assert min_meeting_rooms([[1, 5], [5, 10]]) == 1
        assert min_meeting_rooms([[1, 4], [2, 5], [3, 6]]) == 3
        assert min_meeting_rooms([]) == 0
        print("All Question 3 tests PASSED!")
    except AssertionError as e:
        print(f"Question 3 FAILED: {e}")
    except Exception as e:
        print(f"Question 3 ERROR: {e}")

    # Test Question 4
    print("\n--- Question 4: Interval List Intersections ---")
    try:
        first = [[0, 2], [5, 10], [13, 23], [24, 25]]
        second = [[1, 5], [8, 12], [15, 24], [25, 26]]
        expected = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
        assert interval_intersection(first, second) == expected

        assert interval_intersection([[1, 3], [5, 9]], []) == []
        assert interval_intersection([], [[4, 8], [10, 12]]) == []
        assert interval_intersection([[1, 7]], [[3, 10]]) == [[3, 7]]

        print("All Question 4 tests PASSED!")
    except AssertionError as e:
        print(f"Question 4 FAILED: {e}")
    except Exception as e:
        print(f"Question 4 ERROR: {e}")

    # ==========================================
    # REVISION: Module 11 (Recursion/Backtracking)
    # ==========================================
    print("\n--- REVISION: Recursion/Backtracking ---")
    print("Q: What's the backtracking pattern?")
    print("A: Make choice -> recurse -> undo choice. Explore all paths in a decision tree.")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Sort intervals by start time - makes overlapping intervals adjacent
2. Overlap condition: interval1.end >= interval2.start
3. Merge: [min(starts), max(ends)]
4. Sweep line: convert to events (+1 start, -1 end), track running count
5. Two pointers for intersecting two lists: advance the one that ends first
""")