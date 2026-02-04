"""
DSA Course - Module 20: Trie (Prefix Tree)
==========================================

CONCEPT: Trie Data Structure
----------------------------
A tree-like structure for storing strings where each node represents
a character. Common prefixes share the same path from root.

STRUCTURE:
         root
        / | \
       a  b  c
      /       \
     p         a
    / \         \
   p   e        r
  /             |
 l              s
 e

Stores: "apple", "ape", "cars"

OPERATIONS:
- Insert word: O(m) where m = word length
- Search word: O(m)
- Search prefix: O(m)
- Delete word: O(m)

ADVANTAGES:
- Fast prefix operations (autocomplete!)
- No hash collisions (unlike hash tables)
- Alphabetically ordered iteration

WHEN TO USE:
- Autocomplete / typeahead
- Spell checking
- IP routing (longest prefix match)
- Word games (finding valid words)
- Prefix matching problems

SPACE COMPLEXITY:
- Worst case: O(alphabet_size * max_word_length * num_words)
- In practice, shared prefixes save a lot of space
"""


# ============================================
# Trie Implementation
# ============================================

class TrieNode:
    """A node in the Trie."""
    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.is_end = False  # True if this node marks end of a word


class Trie:
    """
    Trie (Prefix Tree) implementation.

    Example:
        trie = Trie()
        trie.insert("apple")
        trie.search("apple")   # True
        trie.search("app")     # False
        trie.starts_with("app") # True
        trie.insert("app")
        trie.search("app")     # True
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        """Return True if word is in the trie."""
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        """Return True if any word starts with the given prefix."""
        return self._find_node(prefix) is not None

    def _find_node(self, prefix: str) -> TrieNode:
        """Helper: traverse trie following the prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node


# Let's trace inserting "apple" and "app":
#
# Insert "apple":
#   root -> 'a' -> 'p' -> 'p' -> 'l' -> 'e'(end)
#
# Insert "app":
#   root -> 'a' -> 'p' -> 'p'(end) -> 'l' -> 'e'(end)
#   (reuses existing nodes, just marks 'p' as end)
#
# Search "app": traverse a->p->p, is_end=True -> True
# Search "ap": traverse a->p, is_end=False -> False
# starts_with "ap": traverse a->p, node exists -> True


# ============================================
# QUESTION 1: Implement Trie (from scratch)
# ============================================

"""
PROBLEM: Implement a Trie with insert, search, and startsWith methods.

This is the same as the example above, but implement it yourself!

Examples:
    trie = MyTrie()
    trie.insert("apple")
    trie.search("apple")   # returns True
    trie.search("app")     # returns False
    trie.starts_with("app") # returns True
    trie.insert("app")
    trie.search("app")     # returns True

HINT: Follow the structure shown in the example.
      - Each node has children dict and is_end flag
      - Insert: create nodes as needed, mark end
      - Search: traverse, check is_end at final node
      - StartsWith: traverse, check if node exists

Implement the class below:
"""


class MyTrie:
    """Implement your own Trie."""

    def __init__(self):
        # YOUR CODE HERE
        pass

    def insert(self, word: str) -> None:
        # YOUR CODE HERE
        pass

    def search(self, word: str) -> bool:
        # YOUR CODE HERE
        pass

    def starts_with(self, prefix: str) -> bool:
        # YOUR CODE HERE
        pass


# ============================================
# QUESTION 2: Word Search II
# ============================================

"""
PROBLEM: Find all words from a dictionary that exist in a grid.

Given an m x n board of characters and a list of words,
return all words that can be constructed from letters of sequentially
adjacent cells (horizontal or vertical). Each cell can only be used once per word.

Examples:
- board = [["o","a","a","n"],
           ["e","t","a","e"],
           ["i","h","k","r"],
           ["i","f","l","v"]]
  words = ["oath","pea","eat","rain"]
  -> ["eat","oath"]

- board = [["a","b"],["c","d"]]
  words = ["abcb"]
  -> [] (can't reuse cells)

HINT: Build a Trie from the word list, then DFS from each cell.

      1. Insert all words into Trie
      2. For each cell, run DFS using Trie to prune invalid paths
      3. If we reach a word ending, add to results

      def dfs(i, j, node, path):
          char = board[i][j]
          if char not in node.children:
              return

          child = node.children[char]
          path += char

          if child.is_end:
              result.add(path)

          board[i][j] = '#'  # Mark visited
          for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
              dfs(i+di, j+dj, child, path)
          board[i][j] = char  # Restore

Implement the function below:
"""


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    """Find all words from dictionary that exist in the grid."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 3: Design Add and Search Words
# ============================================

"""
PROBLEM: Design a data structure that supports adding words and searching.

Search can contain '.' which matches any letter.

Examples:
    wd = WordDictionary()
    wd.add_word("bad")
    wd.add_word("dad")
    wd.add_word("mad")
    wd.search("pad")  # False
    wd.search("bad")  # True
    wd.search(".ad")  # True (matches bad, dad, mad)
    wd.search("b..")  # True (matches bad)

HINT: Use a Trie, but handle '.' by trying all children.

      def search(word):
          def dfs(node, i):
              if i == len(word):
                  return node.is_end

              char = word[i]
              if char == '.':
                  # Try all children
                  for child in node.children.values():
                      if dfs(child, i + 1):
                          return True
                  return False
              else:
                  if char not in node.children:
                      return False
                  return dfs(node.children[char], i + 1)

          return dfs(self.root, 0)

Implement the class below:
"""


class WordDictionary:
    """Support add_word and search with '.' wildcard."""

    def __init__(self):
        # YOUR CODE HERE
        pass

    def add_word(self, word: str) -> None:
        # YOUR CODE HERE
        pass

    def search(self, word: str) -> bool:
        # YOUR CODE HERE
        pass


# ============================================
# QUESTION 4: Longest Word in Dictionary
# ============================================

"""
PROBLEM: Find the longest word that can be built one character at a time.

Given a list of words, find the longest word that can be built by
adding one letter at a time, where each intermediate word is also in the dictionary.

If multiple answers, return the lexicographically smallest.

Examples:
- words = ["w","wo","wor","worl","world"] -> "world"
  Build: w -> wo -> wor -> worl -> world

- words = ["a","banana","app","appl","ap","apply","apple"] -> "apple"
  Build: a -> ap -> app -> appl -> apple
  "apply" is same length but "apple" < "apply" lexicographically

HINT: Insert all words into Trie, then BFS/DFS to find longest buildable word.

      A word is "buildable" if every prefix is also a word (is_end = True).

      Sort words by length, then alphabetically.
      For each word, check if all prefixes exist.

      Or use Trie: DFS only following nodes where is_end = True.

Implement the function below:
"""


def longest_word(words: list[str]) -> str:
    """Find longest word buildable one character at a time."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 20: Trie (Prefix Tree)")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Trie Operations ---")
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.starts_with("app") == True
    trie.insert("app")
    assert trie.search("app") == True
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Implement Trie ---")
    try:
        my_trie = MyTrie()
        my_trie.insert("apple")
        assert my_trie.search("apple") == True, "Search apple"
        assert my_trie.search("app") == False, "Search app (not inserted)"
        assert my_trie.starts_with("app") == True, "Prefix app"
        my_trie.insert("app")
        assert my_trie.search("app") == True, "Search app (after insert)"
        assert my_trie.starts_with("appl") == True
        assert my_trie.starts_with("b") == False
        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: Word Search II ---")
    try:
        board = [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"]
        ]
        words = ["oath", "pea", "eat", "rain"]
        result = find_words(board, words)
        assert sorted(result) == ["eat", "oath"], f"Got {result}"

        board2 = [["a", "b"], ["c", "d"]]
        assert find_words(board2, ["abcb"]) == []

        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    # Test Question 3
    print("\n--- Question 3: Add and Search Words ---")
    try:
        wd = WordDictionary()
        wd.add_word("bad")
        wd.add_word("dad")
        wd.add_word("mad")
        assert wd.search("pad") == False
        assert wd.search("bad") == True
        assert wd.search(".ad") == True
        assert wd.search("b..") == True
        assert wd.search("...") == True
        assert wd.search("....") == False
        print("All Question 3 tests PASSED!")
    except AssertionError as e:
        print(f"Question 3 FAILED: {e}")
    except Exception as e:
        print(f"Question 3 ERROR: {e}")

    # Test Question 4
    print("\n--- Question 4: Longest Word ---")
    try:
        assert longest_word(["w", "wo", "wor", "worl", "world"]) == "world"
        assert longest_word(["a", "banana", "app", "appl", "ap", "apply", "apple"]) == "apple"
        assert longest_word(["a", "b", "c"]) == "a"  # Lexicographically smallest
        assert longest_word([]) == ""
        # Edge cases
        assert longest_word(["a"]) == "a", "Single word"
        print("All Question 4 tests PASSED!")
    except AssertionError as e:
        print(f"Question 4 FAILED: {e}")
    except Exception as e:
        print(f"Question 4 ERROR: {e}")

    # ==========================================
    # REVISION: Module 19 (Topological Sort)
    # ==========================================
    print("\n--- REVISION: Topological Sort ---")
    print("Q: On what type of graph does topological sort work?")
    print("A: Only DAGs (Directed Acyclic Graphs). If there's a cycle, no valid ordering exists.")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Trie: tree where each node is a character, paths form words
2. Insert/Search/StartsWith all O(word length)
3. Shared prefixes save space and enable prefix operations
4. Perfect for: autocomplete, spell check, prefix matching
5. For wildcard search, use DFS trying all children at '.'
6. Word Search II: build Trie from words, DFS grid using Trie to prune
""")