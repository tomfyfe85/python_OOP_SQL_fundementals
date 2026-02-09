"""
DSA Course - Module 6: Frequency Counting
=========================================

CONCEPT: Counting Element Frequencies
-------------------------------------
Many problems become simple once you count how often each element appears.
Use a dictionary (hash map) to count frequencies in O(n) time.

PYTHON TOOLS:
- dict: {element: count}
- collections.Counter: does the counting for you

COMMON PATTERNS:

1. BUILD FREQUENCY MAP, THEN QUERY
   - First pass: count everything
   - Second pass: use counts to solve problem

2. COMPARE FREQUENCY MAPS
   - Two strings are anagrams if they have same frequencies
   - Two arrays have same elements if frequencies match

3. FIND BY FREQUENCY
   - Find most common element
   - Find elements appearing exactly k times

WHEN TO USE:
- Anagram problems
- Finding duplicates/unique elements
- "How many times does X appear?"
- Comparing two collections for same elements
"""


from collections import Counter


# ============================================
# EXAMPLE: Valid Anagram
# ============================================

def is_anagram_example(s: str, t: str) -> bool:
    """
    Check if t is an anagram of s.
    Anagram = same characters, same frequencies, different order.

    Strategy:
    - Count frequency of each char in s
    - Count frequency of each char in t
    - Compare: if same, they're anagrams
    """
    if len(s) != len(t):
        return False

    # Method 1: Using Counter (easiest)
    return Counter(s) == Counter(t)


def is_anagram_manual(s: str, t: str) -> bool:
    """Same as above but building the dict manually."""
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for char in s:
        count_s[char] = count_s.get(char, 0) + 1

    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    return count_s == count_t


# Let's trace through: s="anagram", t="nagaram"
#
# count_s = {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
# count_t = {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}
#
# count_s == count_t? Yes! (order doesn't matter in dicts)
# Return True


# ============================================
# QUESTION 1: Find All Anagrams in String
# ============================================

"""
PROBLEM: Find all start indices of anagrams of p in string s.

Given strings s and p, return an array of all start indices
where an anagram of p begins in s.

Examples:
- s="cbaebabacd", p="abc" -> [0, 6]
  Index 0: "cba" is anagram of "abc"
  Index 6: "bac" is anagram of "abc"

- s="abab", p="ab" -> [0, 1, 2]
  Index 0: "ab" is anagram of "ab"
  Index 1: "ba" is anagram of "ab"
  Index 2: "ab" is anagram of "ab"

Implement the function below:
"""


def find_anagrams(s: str, p: str) -> list[int]:
    """Return list of starting indices of p's anagrams in s."""
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2: Majority Element
# ============================================

"""
PROBLEM: Find the element that appears more than n/2 times.

Given an array of size n, find the majority element.
The majority element appears more than floor(n/2) times.
You may assume the majority element always exists.

Examples:
- [3, 2, 3] -> 3 (appears 2 times, n/2 = 1.5, 2 > 1.5)
- [2, 2, 1, 1, 1, 2, 2] -> 2 (appears 4 times, n/2 = 3.5, 4 > 3.5)

Implement the function below:
"""


def majority_element(nums: list[int]) -> int:
    """Return the element appearing more than n/2 times."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 6: Frequency Counting")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Valid Anagram ---")
    assert is_anagram_example("anagram", "nagaram") == True
    assert is_anagram_example("rat", "car") == False
    assert is_anagram_manual("listen", "silent") == True
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Find All Anagrams ---")
    try:
        result1 = find_anagrams("cbaebabacd", "abc")
        assert result1 == [0, 6], f"Expected [0, 6], got {result1}"

        result2 = find_anagrams("abab", "ab")
        assert result2 == [0, 1, 2], f"Expected [0, 1, 2], got {result2}"

        result3 = find_anagrams("aaaa", "aa")
        assert result3 == [0, 1, 2], f"Expected [0, 1, 2], got {result3}"

        result4 = find_anagrams("hello", "xyz")
        assert result4 == [], f"Expected [], got {result4}"

        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2
    print("\n--- Question 2: Majority Element ---")
    try:
        assert majority_element([3, 2, 3]) == 3, "Basic case"
        assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2, "Longer array"
        assert majority_element([1]) == 1, "Single element"
        assert majority_element([1, 1, 1, 1]) == 1, "All same"
        # Edge cases
        assert majority_element([1, 2, 1]) == 1, "Simple majority"
        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    # ==========================================
    # REVISION: Module 6 (Sliding Window)
    # ==========================================
    print("\n--- REVISION: Sliding Window ---")
    print("Q: What's the difference between fixed and variable sliding window?")
    print("A: Fixed: window size stays constant (slide). Variable: expand/shrink based on conditions.")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Counter(iterable) gives you frequency map instantly
2. Two Counter objects can be compared with ==
3. dict.get(key, default) avoids KeyError
4. Frequency counting + sliding window = powerful combo
5. Most common: Counter(x).most_common(1)[0][0]
""")
