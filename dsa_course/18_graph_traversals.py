"""
DSA Course - Module 18: Graph Traversals (BFS & DFS)
====================================================

CONCEPT: Graphs
---------------
A graph is a set of vertices (nodes) connected by edges.

REPRESENTATIONS:
1. Adjacency List: dict/list where adj[v] = list of neighbors
   - Space: O(V + E)
   - Best for sparse graphs

2. Adjacency Matrix: 2D array where matrix[i][j] = edge exists
   - Space: O(V^2)
   - Best for dense graphs

3. Edge List: list of (u, v) pairs
   - Space: O(E)
   - Best for algorithms like Kruskal's

GRAPH TYPES:
- Directed vs Undirected
- Weighted vs Unweighted
- Cyclic vs Acyclic
- Connected vs Disconnected

TRAVERSALS:

BFS (Breadth-First Search):
- Uses queue
- Visits nodes level by level
- Finds shortest path in unweighted graphs
- Good for: shortest path, level-order exploration

DFS (Depth-First Search):
- Uses recursion or stack
- Goes deep before backtracking
- Good for: cycle detection, topological sort, connected components

TIME COMPLEXITY: O(V + E) for both BFS and DFS
"""

from collections import deque


# ============================================
# EXAMPLE: BFS and DFS
# ============================================

def bfs_example(graph: dict, start: int) -> list[int]:
    """
    Breadth-First Search traversal.

    Graph (adjacency list):
    {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}

    BFS from 0: [0, 1, 2, 3]
    (visits nodes level by level)
    """
    visited = set()
    result = []
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def dfs_example(graph: dict, start: int) -> list[int]:
    """
    Depth-First Search traversal (iterative with stack).

    DFS from 0: [0, 2, 3, 1] (goes deep first)
    Order depends on neighbor order and stack behavior.
    """
    visited = set()
    result = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        result.append(node)

        # Add neighbors (reversed to maintain left-to-right order)
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)

    return result


def dfs_recursive(graph: dict, start: int, visited: set = None) -> list[int]:
    """DFS using recursion."""
    if visited is None:
        visited = set()

    visited.add(start)
    result = [start]

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result


# ============================================
# QUESTION 1: Number of Islands
# ============================================

"""
PROBLEM: Count the number of islands in a grid.

Given a 2D grid of '1's (land) and '0's (water), count islands.
An island is surrounded by water and formed by connecting adjacent lands
horizontally or vertically.

Examples:
- grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ] -> 1 island

- grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ] -> 3 islands

HINT: For each unvisited land cell, run DFS/BFS to mark all connected
      land cells as visited. Count how many times we start a new search.

      def numIslands(grid):
          count = 0
          for i in range(rows):
              for j in range(cols):
                  if grid[i][j] == '1':
                      dfs(grid, i, j)  # Mark entire island
                      count += 1
          return count

      def dfs(grid, i, j):
          if out of bounds or grid[i][j] != '1':
              return
          grid[i][j] = '0'  # Mark visited
          dfs(grid, i+1, j)
          dfs(grid, i-1, j)
          dfs(grid, i, j+1)
          dfs(grid, i, j-1)

Implement the function below:
"""


def num_islands(grid: list[list[str]]) -> int:
    """Return the number of islands in the grid."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2: Clone Graph
# ============================================

"""
PROBLEM: Deep copy a graph.

Given a reference to a node in a connected undirected graph,
return a deep copy (clone) of the graph.

Each node contains a val and list of neighbors.

Example:
    1 -- 2
    |    |
    4 -- 3

    Input: node 1
    Output: deep copy of entire graph

HINT: Use BFS or DFS with a hashmap to track cloned nodes.

      def cloneGraph(node):
          if not node:
              return None
          cloned = {node: Node(node.val)}
          queue = deque([node])

          while queue:
              curr = queue.popleft()
              for neighbor in curr.neighbors:
                  if neighbor not in cloned:
                      cloned[neighbor] = Node(neighbor.val)
                      queue.append(neighbor)
                  cloned[curr].neighbors.append(cloned[neighbor])

          return cloned[node]

Implement the function below:
"""


class GraphNode:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


def clone_graph(node: GraphNode) -> GraphNode:
    """Return a deep copy of the graph."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 3: Shortest Path in Unweighted Graph
# ============================================

"""
PROBLEM: Find shortest path between two nodes (unweighted).

Given an adjacency list and two nodes, return the shortest path length.
Return -1 if no path exists.

Examples:
- graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
  start=0, end=3 -> 2 (0->1->3 or 0->2->3)

- graph = {0: [1], 1: [0], 2: [3], 3: [2]}
  start=0, end=3 -> -1 (disconnected)

HINT: BFS gives shortest path in unweighted graphs!
      Track distance as you go:

      def shortestPath(graph, start, end):
          if start == end:
              return 0
          visited = {start}
          queue = deque([(start, 0)])  # (node, distance)

          while queue:
              node, dist = queue.popleft()
              for neighbor in graph.get(node, []):
                  if neighbor == end:
                      return dist + 1
                  if neighbor not in visited:
                      visited.add(neighbor)
                      queue.append((neighbor, dist + 1))
          return -1

Implement the function below:
"""


def shortest_path(graph: dict, start: int, end: int) -> int:
    """Return shortest path length, or -1 if no path exists."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 4: Detect Cycle in Undirected Graph
# ============================================

"""
PROBLEM: Check if an undirected graph contains a cycle.

Given an adjacency list representing an undirected graph,
return True if there's a cycle.

Examples:
- graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
  -> True (0-1-2-0 is a cycle)

- graph = {0: [1], 1: [0, 2], 2: [1]}
  -> False (it's a line: 0-1-2)

HINT: DFS with parent tracking.
      A cycle exists if we visit a node that's already visited
      AND it's not our parent (direct back edge doesn't count).

      def hasCycle(graph):
          visited = set()

          def dfs(node, parent):
              visited.add(node)
              for neighbor in graph.get(node, []):
                  if neighbor not in visited:
                      if dfs(neighbor, node):
                          return True
                  elif neighbor != parent:  # Visited but not parent = cycle
                      return True
              return False

          # Check all components
          for node in graph:
              if node not in visited:
                  if dfs(node, -1):
                      return True
          return False

Implement the function below:
"""


def has_cycle_undirected(graph: dict) -> bool:
    """Return True if undirected graph has a cycle."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 5: Connected Components
# ============================================

"""
PROBLEM: Count connected components in an undirected graph.

Given n nodes (0 to n-1) and edges, return the number of connected components.

Examples:
- n=5, edges=[[0,1],[1,2],[3,4]] -> 2
  Component 1: {0, 1, 2}
  Component 2: {3, 4}

- n=5, edges=[[0,1],[1,2],[2,3],[3,4]] -> 1
  All connected

- n=4, edges=[] -> 4
  Each node is its own component

HINT: Build adjacency list, then count DFS/BFS starts.

      graph = build_adjacency_list(n, edges)
      visited = set()
      count = 0

      for node in range(n):
          if node not in visited:
              dfs(graph, node, visited)
              count += 1

      return count

Implement the function below:
"""


def count_components(n: int, edges: list[list[int]]) -> int:
    """Return number of connected components."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 18: Graph Traversals (BFS & DFS)")
    print("=" * 60)

    # Test Example
    print("\n--- Example: BFS and DFS ---")
    graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
    print(f"BFS from 0: {bfs_example(graph, 0)}")
    print(f"DFS from 0: {dfs_example(graph, 0)}")
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Number of Islands ---")
    try:
        grid1 = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ]
        assert num_islands(grid1) == 1

        grid2 = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        assert num_islands(grid2) == 3

        assert num_islands([["0"]]) == 0
        assert num_islands([["1"]]) == 1

        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: Clone Graph ---")
    try:
        # Build graph: 1-2, 1-4, 2-3, 3-4
        n1 = GraphNode(1)
        n2 = GraphNode(2)
        n3 = GraphNode(3)
        n4 = GraphNode(4)
        n1.neighbors = [n2, n4]
        n2.neighbors = [n1, n3]
        n3.neighbors = [n2, n4]
        n4.neighbors = [n1, n3]

        cloned = clone_graph(n1)
        assert cloned is not n1  # Different object
        assert cloned.val == 1
        assert len(cloned.neighbors) == 2
        assert cloned.neighbors[0] is not n2  # Deep copy

        assert clone_graph(None) is None

        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    # Test Question 3
    print("\n--- Question 3: Shortest Path ---")
    try:
        graph = {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
        assert shortest_path(graph, 0, 3) == 2
        assert shortest_path(graph, 0, 0) == 0

        disconnected = {0: [1], 1: [0], 2: [3], 3: [2]}
        assert shortest_path(disconnected, 0, 3) == -1

        print("All Question 3 tests PASSED!")
    except AssertionError as e:
        print(f"Question 3 FAILED: {e}")
    except Exception as e:
        print(f"Question 3 ERROR: {e}")

    # Test Question 4
    print("\n--- Question 4: Detect Cycle (Undirected) ---")
    try:
        assert has_cycle_undirected({0: [1, 2], 1: [0, 2], 2: [0, 1]}) == True
        assert has_cycle_undirected({0: [1], 1: [0, 2], 2: [1]}) == False
        assert has_cycle_undirected({0: [1], 1: [0]}) == False
        assert has_cycle_undirected({0: []}) == False

        print("All Question 4 tests PASSED!")
    except AssertionError as e:
        print(f"Question 4 FAILED: {e}")
    except Exception as e:
        print(f"Question 4 ERROR: {e}")

    # Test Question 5
    print("\n--- Question 5: Connected Components ---")
    try:
        assert count_components(5, [[0, 1], [1, 2], [3, 4]]) == 2
        assert count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
        assert count_components(4, []) == 4
        assert count_components(1, []) == 1

        # Edge cases
        assert count_components(3, [[0, 1], [0, 2]]) == 1, "Star graph"

        print("All Question 5 tests PASSED!")
    except AssertionError as e:
        print(f"Question 5 FAILED: {e}")
    except Exception as e:
        print(f"Question 5 ERROR: {e}")

    # ==========================================
    # REVISION: Module 17 (Binary Trees)
    # ==========================================
    print("\n--- REVISION: Binary Trees ---")
    print("Q: Which traversal gives sorted order for a BST?")
    print("A: In-order traversal (left -> node -> right).")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. BFS uses queue, visits level by level, finds shortest path (unweighted)
2. DFS uses stack/recursion, goes deep first, good for cycles/components
3. Both are O(V + E) time complexity
4. Islands problem: DFS/BFS from each unvisited land, count starts
5. Cycle detection (undirected): visited neighbor that isn't parent = cycle
""")