"""
DSA Course - Module 19: Topological Sort
========================================

CONCEPT: Topological Sort
-------------------------
A linear ordering of vertices in a Directed Acyclic Graph (DAG)
such that for every edge (u, v), u comes before v.

REAL-WORLD EXAMPLES:
- Course prerequisites: take CS101 before CS201
- Build dependencies: compile library before application
- Task scheduling: finish task A before starting task B

KEY PROPERTIES:
- Only works on DAGs (Directed Acyclic Graphs)
- If graph has a cycle, topological sort is impossible
- Multiple valid orderings may exist

TWO APPROACHES:

1. KAHN'S ALGORITHM (BFS-based):
   - Track in-degree (incoming edges) for each node
   - Start with nodes that have in-degree 0
   - Remove them, reduce in-degrees of neighbors
   - Repeat until done

2. DFS-based:
   - Run DFS, add nodes to result AFTER visiting all descendants
   - Reverse the result (or prepend instead of append)
   - Cycle detection: track nodes in current path

TIME COMPLEXITY: O(V + E) for both approaches
"""

from collections import deque


# ============================================
# EXAMPLE: Topological Sort (Kahn's Algorithm)
# ============================================

def topo_sort_kahn_example(num_nodes: int, edges: list[list[int]]) -> list[int]:
    """
    Topological sort using Kahn's algorithm (BFS).

    edges[i] = [a, b] means a must come before b (a -> b)

    Example:
    num_nodes = 4
    edges = [[0,1], [0,2], [1,3], [2,3]]

    Graph:
        0 -> 1
        |    |
        v    v
        2 -> 3

    Valid orderings: [0,1,2,3] or [0,2,1,3]
    """
    # Build adjacency list and in-degree count
    adj = {i: [] for i in range(num_nodes)}
    in_degree = {i: 0 for i in range(num_nodes)}

    for a, b in edges:
        adj[a].append(b)
        in_degree[b] += 1

    # Start with nodes that have no prerequisites
    queue = deque([node for node in range(num_nodes) if in_degree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If we didn't process all nodes, there's a cycle
    if len(result) != num_nodes:
        return []  # Cycle detected, no valid ordering

    return result


# Let's trace: 4 nodes, edges [[0,1], [0,2], [1,3], [2,3]]
#
# in_degree: {0: 0, 1: 1, 2: 1, 3: 2}
# Start: queue = [0], result = []
#
# Process 0: result = [0]
#   neighbors: 1, 2
#   in_degree[1] = 0, add to queue
#   in_degree[2] = 0, add to queue
#   queue = [1, 2]
#
# Process 1: result = [0, 1]
#   neighbor: 3
#   in_degree[3] = 1
#   queue = [2]
#
# Process 2: result = [0, 1, 2]
#   neighbor: 3
#   in_degree[3] = 0, add to queue
#   queue = [3]
#
# Process 3: result = [0, 1, 2, 3]
#
# Return [0, 1, 2, 3]


def topo_sort_dfs_example(num_nodes: int, edges: list[list[int]]) -> list[int]:
    """
    Topological sort using DFS.

    Add nodes to result after all descendants are processed.
    """
    adj = {i: [] for i in range(num_nodes)}
    for a, b in edges:
        adj[a].append(b)

    visited = set()
    in_stack = set()  # For cycle detection
    result = []
    has_cycle = False

    def dfs(node):
        nonlocal has_cycle
        if node in in_stack:
            has_cycle = True
            return
        if node in visited:
            return

        in_stack.add(node)
        visited.add(node)

        for neighbor in adj[node]:
            dfs(neighbor)

        in_stack.remove(node)
        result.append(node)  # Add after processing all descendants

    for node in range(num_nodes):
        if node not in visited:
            dfs(node)
            if has_cycle:
                return []

    return result[::-1]  # Reverse for correct order


# ============================================
# QUESTION 1: Course Schedule (Can Finish?)
# ============================================

"""
PROBLEM: Determine if you can finish all courses.

There are numCourses courses labeled 0 to numCourses-1.
prerequisites[i] = [a, b] means you must take b before a.

Return True if you can finish all courses (no cycle in dependencies).

Examples:
- numCourses=2, prerequisites=[[1,0]] -> True
  Take 0, then 1

- numCourses=2, prerequisites=[[1,0],[0,1]] -> False
  Cycle: 0 requires 1, 1 requires 0

- numCourses=3, prerequisites=[[1,0],[2,1]] -> True
  Take 0 -> 1 -> 2

HINT: This is cycle detection in a directed graph.
      If we can do topological sort (process all nodes), no cycle exists.

      Use Kahn's algorithm: if result length < numCourses, there's a cycle.

Implement the function below:
"""


def can_finish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """Return True if all courses can be finished."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2: Course Schedule II (Find Order)
# ============================================

"""
PROBLEM: Return the order to take all courses.

Same setup as Course Schedule, but return an ordering.
If impossible (cycle), return empty array.

Examples:
- numCourses=2, prerequisites=[[1,0]] -> [0,1]
- numCourses=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]] -> [0,1,2,3] or [0,2,1,3]
- numCourses=1, prerequisites=[] -> [0]

HINT: Just run topological sort!
      Return the ordering if valid, empty array if cycle detected.

Implement the function below:
"""


def find_order(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    """Return a valid course ordering, or [] if impossible."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 3: Alien Dictionary
# ============================================

"""
PROBLEM: Determine the order of letters in an alien language.

Given a sorted dictionary of words from an alien language,
derive the ordering of letters.

Examples:
- words = ["wrt","wrf","er","ett","rftt"]
  -> "wertf"
  Reasoning:
    wrt vs wrf: t comes before f
    wrt vs er: w comes before e
    er vs ett: r comes before t
    ett vs rftt: e comes before r

- words = ["z","x"]
  -> "zx" (z comes before x)

- words = ["z","x","z"]
  -> "" (invalid: z before x, but z after x too)

HINT: Build a graph from adjacent word comparisons.
      Compare adjacent words, find first differing char.
      That gives us an edge: char1 -> char2 (char1 comes before char2).

      Then run topological sort on the character graph.

      Edge case: if word1 is prefix of word2 but longer, invalid!
      Example: ["abc", "ab"] is invalid.

Implement the function below:
"""


def alien_order(words: list[str]) -> str:
    """Return the order of letters, or '' if invalid."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 4: Parallel Courses (Minimum Semesters)
# ============================================

"""
PROBLEM: Minimum semesters to take all courses with parallelism.

You can take multiple courses in one semester if prerequisites are met.
Return minimum semesters needed, or -1 if impossible (cycle).

Examples:
- n=3, relations=[[1,3],[2,3]]
  -> 2 semesters
  Semester 1: courses 1, 2 (no prerequisites)
  Semester 2: course 3 (needs 1 and 2)

- n=3, relations=[[1,2],[2,3],[3,1]]
  -> -1 (cycle)

HINT: This is "longest path" in a DAG, or BFS with level counting.

      Modified Kahn's algorithm:
      - Process all in-degree 0 nodes as one semester
      - Count semesters until all processed

      semesters = 0
      while queue:
          semesters += 1
          for each node in current batch:
              process and update in-degrees
              add new in-degree 0 nodes

Implement the function below:
"""


def minimum_semesters(n: int, relations: list[list[int]]) -> int:
    """Return minimum semesters, or -1 if impossible."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 19: Topological Sort")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Topological Sort ---")
    result = topo_sort_kahn_example(4, [[0, 1], [0, 2], [1, 3], [2, 3]])
    # Verify it's a valid topological ordering
    assert 0 in result and result.index(0) < result.index(1)
    assert result.index(0) < result.index(2)
    assert result.index(1) < result.index(3)
    assert result.index(2) < result.index(3)
    print(f"Kahn's result: {result}")

    result_dfs = topo_sort_dfs_example(4, [[0, 1], [0, 2], [1, 3], [2, 3]])
    print(f"DFS result: {result_dfs}")
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Course Schedule (Can Finish?) ---")
    try:
        assert can_finish(2, [[1, 0]]) == True
        assert can_finish(2, [[1, 0], [0, 1]]) == False
        assert can_finish(3, [[1, 0], [2, 1]]) == True
        assert can_finish(1, []) == True
        assert can_finish(3, [[0, 1], [0, 2], [1, 2]]) == True
        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: Course Schedule II (Find Order) ---")
    try:
        result = find_order(2, [[1, 0]])
        assert result == [0, 1], f"Got {result}"

        result = find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
        assert len(result) == 4
        assert result.index(0) < result.index(1)
        assert result.index(0) < result.index(2)
        assert result.index(1) < result.index(3)
        assert result.index(2) < result.index(3)

        assert find_order(2, [[1, 0], [0, 1]]) == []  # Cycle
        assert find_order(1, []) == [0]

        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    # Test Question 3
    print("\n--- Question 3: Alien Dictionary ---")
    try:
        result = alien_order(["wrt", "wrf", "er", "ett", "rftt"])
        # Verify ordering constraints
        assert result.index('t') < result.index('f')
        assert result.index('w') < result.index('e')
        assert result.index('r') < result.index('t')
        assert result.index('e') < result.index('r')

        assert alien_order(["z", "x"]) == "zx"
        assert alien_order(["z", "x", "z"]) == ""  # Invalid
        assert alien_order(["abc", "ab"]) == ""  # Invalid: longer prefix first

        print("All Question 3 tests PASSED!")
    except AssertionError as e:
        print(f"Question 3 FAILED: {e}")
    except Exception as e:
        print(f"Question 3 ERROR: {e}")

    # Test Question 4
    print("\n--- Question 4: Parallel Courses ---")
    try:
        assert minimum_semesters(3, [[1, 3], [2, 3]]) == 2
        assert minimum_semesters(3, [[1, 2], [2, 3], [3, 1]]) == -1
        assert minimum_semesters(1, []) == 1
        assert minimum_semesters(3, [[1, 2], [2, 3]]) == 3  # Sequential

        print("All Question 4 tests PASSED!")
    except AssertionError as e:
        print(f"Question 4 FAILED: {e}")
    except Exception as e:
        print(f"Question 4 ERROR: {e}")

    # ==========================================
    # REVISION: Module 18 (Graph Traversals)
    # ==========================================
    print("\n--- REVISION: Graph Traversals ---")
    print("Q: When do you use BFS vs DFS for graphs?")
    print("A: BFS for shortest path (unweighted). DFS for cycle detection, connected components.")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Topological sort: linear ordering where dependencies come first
2. Only works on DAGs (Directed Acyclic Graphs)
3. Kahn's algorithm (BFS): process in-degree 0 nodes, reduce neighbors
4. DFS approach: add to result after visiting all descendants, reverse
5. Cycle detection: if not all nodes processed, cycle exists
6. Course schedule = dependency graph, alien dictionary = character graph
""")