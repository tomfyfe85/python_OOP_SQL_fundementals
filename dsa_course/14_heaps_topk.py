"""
DSA Course - Module 14: Heaps & Top-K Problems
==============================================

CONCEPT: Heap (Priority Queue)
------------------------------
A heap is a complete binary tree where each parent is smaller (min-heap)
or larger (max-heap) than its children.

PROPERTIES:
- Min-heap: root is minimum element
- Max-heap: root is maximum element
- Complete binary tree: filled level by level, left to right

OPERATIONS:
- Insert (push): O(log n)
- Extract min/max (pop): O(log n)
- Peek (get min/max): O(1)
- Heapify array: O(n)

IN PYTHON:
Use `heapq` module - it's a MIN-HEAP by default!

    import heapq
    heap = []
    heapq.heappush(heap, 3)      # Add element
    smallest = heapq.heappop(heap)  # Remove and return smallest
    smallest = heap[0]           # Peek at smallest

FOR MAX-HEAP: Negate values!
    heapq.heappush(heap, -value)  # Push negated
    largest = -heapq.heappop(heap)  # Pop and negate back

WHEN TO USE HEAPS:
- Finding k smallest/largest elements
- Merge k sorted lists
- Median in data stream
- Task scheduling by priority
- Dijkstra's algorithm

TOP-K PATTERN:
To find k largest: use MIN-HEAP of size k
To find k smallest: use MAX-HEAP of size k

Why? We keep the k best elements. When heap exceeds k, we remove
the "worst" of our candidates (top of heap).
"""

import heapq


# ============================================
# EXAMPLE: Kth Largest Element
# ============================================

def find_kth_largest_example(nums: list[int], k: int) -> int:
    """
    Find the kth largest element in an unsorted array.

    [3,2,1,5,6,4], k=2 -> 5 (sorted: [1,2,3,4,5,6], 2nd largest is 5)

    Strategy: Use a min-heap of size k.
    The heap keeps the k largest elements seen so far.
    The root (smallest in heap) is the kth largest overall.
    """
    # Min-heap to keep k largest elements
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # Remove smallest (not in top k)

    return min_heap[0]  # Root is kth largest


# Alternative using heapq.nlargest (simpler but less educational)
def find_kth_largest_simple(nums: list[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


# Let's trace: nums=[3,2,1,5,6,4], k=2
#
# Push 3: heap=[3]
# Push 2: heap=[2,3]
# Push 1: heap=[1,2,3], size > k=2, pop 1 -> heap=[2,3]
# Push 5: heap=[2,3,5], size > k, pop 2 -> heap=[3,5]
# Push 6: heap=[3,5,6], size > k, pop 3 -> heap=[5,6]
# Push 4: heap=[4,5,6], size > k, pop 4 -> heap=[5,6]
#
# Return heap[0] = 5 (2nd largest)


# ============================================
# QUESTION 1: K Closest Points to Origin
# ============================================

"""
PROBLEM: Find k points closest to origin (0, 0).

Given an array of points where points[i] = [x, y], return the k closest
points to the origin. Order of output doesn't matter.

Distance formula: sqrt(x^2 + y^2), but we can compare x^2 + y^2 directly.

Examples:
- points=[[1,3],[-2,2]], k=1 -> [[-2,2]]
  Distances: [1,3] -> 10, [-2,2] -> 8
  Closest: [-2,2]

- points=[[3,3],[5,-1],[-2,4]], k=2 -> [[3,3],[-2,4]]
  Distances: 18, 26, 20
  Two closest: [3,3] and [-2,4]

HINT: Use a MAX-HEAP of size k (negate distances for max behavior).
      Keep the k smallest distances.

      for point in points:
          dist = x*x + y*y
          heapq.heappush(heap, (-dist, point))  # Negate for max-heap
          if len(heap) > k:
              heapq.heappop(heap)  # Remove farthest

Implement the function below:
"""


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    """Return k points closest to origin."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2: Top K Frequent Elements
# ============================================

"""
PROBLEM: Find the k most frequent elements.

Given an integer array and k, return the k most frequent elements.
Order doesn't matter. Answer is guaranteed to be unique.

Examples:
- nums=[1,1,1,2,2,3], k=2 -> [1,2]
  Frequencies: 1->3, 2->2, 3->1
  Top 2: 1 and 2

- nums=[1], k=1 -> [1]

HINT: Two steps:
      1. Count frequencies using a dictionary
      2. Use a min-heap of size k to keep top k frequencies

      Or use heapq.nlargest with key=frequency

Implement the function below:
"""


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Return k most frequent elements."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 3: Merge K Sorted Lists
# ============================================

"""
PROBLEM: Merge k sorted linked lists into one sorted list.

Given an array of k sorted linked lists, merge them into one sorted list.

Examples:
- lists=[[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]

- lists=[] -> []

- lists=[[]] -> []

HINT: Use a min-heap to always get the smallest element across all lists.

      1. Push first element of each list into heap: (value, list_index, node)
      2. Pop smallest, add to result
      3. If popped node has next, push next node
      4. Repeat until heap is empty

      Note: Python heapq compares tuples element by element.
            Include list_index to break ties (avoid comparing nodes).

For this exercise, we'll use simple lists instead of linked lists.
Implement the function below:
"""


def merge_k_sorted(lists: list[list[int]]) -> list[int]:
    """Merge k sorted lists into one sorted list."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 4: Find Median from Data Stream
# ============================================

"""
PROBLEM: Design a data structure for finding median from a data stream.

Implement MedianFinder class:
- __init__(): Initialize the object
- add_num(num): Add num to the data structure
- find_median(): Return median of all elements so far

Median: middle value in sorted list. If even count, average of two middle values.

Examples:
- add_num(1), add_num(2), find_median() -> 1.5
- add_num(3), find_median() -> 2.0

HINT: Use TWO heaps!
      - max_heap: stores smaller half (use negation for max behavior)
      - min_heap: stores larger half

      Invariants:
      1. All elements in max_heap <= all elements in min_heap
      2. Sizes differ by at most 1
      3. max_heap has equal or one more element

      Adding a number:
      1. Add to max_heap
      2. Move max of max_heap to min_heap
      3. If min_heap larger, move min back to max_heap

      Finding median:
      - If same size: average of both tops
      - Otherwise: top of max_heap

Implement the class below:
"""


class MedianFinder:
    """Data structure for finding median from data stream."""

    def __init__(self):
        # YOUR CODE HERE
        pass

    def add_num(self, num: int) -> None:
        # YOUR CODE HERE
        pass

    def find_median(self) -> float:
        # YOUR CODE HERE
        pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 14: Heaps & Top-K Problems")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Kth Largest Element ---")
    assert find_kth_largest_example([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest_example([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_kth_largest_example([1], 1) == 1
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: K Closest Points ---")
    try:
        result = k_closest([[1, 3], [-2, 2]], 1)
        assert result == [[-2, 2]], f"Got {result}"

        result = k_closest([[3, 3], [5, -1], [-2, 4]], 2)
        # Sort for comparison (order doesn't matter)
        assert sorted(result) == sorted([[3, 3], [-2, 4]]), f"Got {result}"

        result = k_closest([[0, 1], [1, 0]], 2)
        assert len(result) == 2

        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: Top K Frequent ---")
    try:
        result = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
        assert sorted(result) == [1, 2], f"Got {result}"

        result = top_k_frequent([1], 1)
        assert result == [1], f"Got {result}"

        result = top_k_frequent([1, 2, 2, 3, 3, 3], 2)
        assert sorted(result) == [2, 3], f"Got {result}"

        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    # Test Question 3
    print("\n--- Question 3: Merge K Sorted Lists ---")
    try:
        assert merge_k_sorted([[1, 4, 5], [1, 3, 4], [2, 6]]) == [1, 1, 2, 3, 4, 4, 5, 6]
        assert merge_k_sorted([]) == []
        assert merge_k_sorted([[]]) == []
        assert merge_k_sorted([[1], [2], [3]]) == [1, 2, 3]
        assert merge_k_sorted([[1, 2, 3]]) == [1, 2, 3]
        print("All Question 3 tests PASSED!")
    except AssertionError as e:
        print(f"Question 3 FAILED: {e}")
    except Exception as e:
        print(f"Question 3 ERROR: {e}")

    # Test Question 4
    print("\n--- Question 4: Find Median from Data Stream ---")
    try:
        mf = MedianFinder()
        mf.add_num(1)
        mf.add_num(2)
        assert mf.find_median() == 1.5, "After [1,2]"
        mf.add_num(3)
        assert mf.find_median() == 2.0, "After [1,2,3]"

        mf2 = MedianFinder()
        mf2.add_num(6)
        assert mf2.find_median() == 6.0
        mf2.add_num(10)
        assert mf2.find_median() == 8.0
        mf2.add_num(2)
        assert mf2.find_median() == 6.0

        print("All Question 4 tests PASSED!")
    except AssertionError as e:
        print(f"Question 4 FAILED: {e}")
    except Exception as e:
        print(f"Question 4 ERROR: {e}")

    # ==========================================
    # REVISION: Module 13 (Greedy)
    # ==========================================
    print("\n--- REVISION: Greedy Algorithms ---")
    print("Q: When does a greedy approach work?")
    print("A: When local optimal choices lead to global optimal solution. Always verify!")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Python heapq is a MIN-HEAP; negate values for max-heap behavior
2. Top-K largest: use min-heap of size k
3. Top-K smallest: use max-heap of size k
4. Merge K sorted: heap gives O(n log k) vs O(nk) naive
5. Streaming median: two heaps (max for small half, min for large half)
""")