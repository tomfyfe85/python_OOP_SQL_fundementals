"""
DSA Course - Module 3: Two Pointers
===================================

CONCEPT: Two Pointers Technique
-------------------------------
Use two pointers to traverse an array, often from opposite ends
or at different speeds. This often turns O(n^2) into O(n).

TWO MAIN PATTERNS:

1. OPPOSITE ENDS (converging pointers)
    - Start: left=0, right=len-1
    - Move toward each other based on some condition
    - Stop when they meet
    - Use for: palindrome, two sum on sorted array, container problems

2. SAME DIRECTION (different speeds)
    - Both start at beginning (or one ahead)
    - Fast pointer explores, slow pointer marks position
    - Use for: removing duplicates, partitioning

WHEN TO USE:
- Array is SORTED (or needs to be)
- Looking for pairs with some property
- Need to compare elements from both ends
- In-place array modification
"""


# ============================================
# EXAMPLE: Valid Palindrome
# ============================================

def is_palindrome_example(s: str) -> bool:
    """
    Check if string is a palindrome (reads same forwards and backwards).
    Ignore non-alphanumeric characters and case.

    Strategy:
    - Use two pointers from opposite ends
    - Skip non-alphanumeric characters
    - Compare characters (case-insensitive)
    - If all match, it's a palindrome
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# Let's trace through: "A man, a plan, a canal: Panama"
#
# After cleaning mentally: "amanaplanacanalpanama"
# left=0 ('A'), right=end ('a'): 'a' == 'a' -> continue
# left=1 ('m'), right=end-1 ('m'): 'm' == 'm' -> continue
# ... keeps matching until left >= right
# Return True


# ============================================
# QUESTION 1: Reverse String In-Place
# ============================================

"""
PROBLEM: Reverse a list of characters IN-PLACE.

Given a list of characters, reverse it. You must do this by modifying
the input list directly with O(1) extra memory.

Examples:
- ["h","e","l","l","o"] -> ["o","l","l","e","h"]
- ["H","a","n","n","a","h"] -> ["h","a","n","n","a","H"]

Implement the function below:
"""


def reverse_string(s: list[str]) -> None:
    """Reverse the list in-place. Return nothing."""
    import math
    half_length = math.floor(len(s)/2) - 1
    reverse_count = -1
    count = 0
    
    for _ in s:
        if count <= half_length:
            p1 = s[count]
            p2 = s[reverse_count]

            s[reverse_count] = p1
            s[count] = p2

            count += 1
            reverse_count -= 1
        





# ============================================
# QUESTION 2: Two Sum II - Sorted Array (LeetCode #167)
# ============================================

"""
PROBLEM: Find two numbers in a SORTED array that add to target.

This is LeetCode #167 and demonstrates the power of two pointers
on sorted data - we get O(n) instead of O(n^2).

Given a 1-indexed sorted array and a target, return the indices
of two numbers that add up to target. (Return 1-indexed!)

Examples:
- numbers=[1,2,3,4,7,11,15], target=9 -> [1, 2] (2+7=9)
- numbers=[2,3,4], target=6 -> [1, 3] (2+4=6)
- numbers=[-1,0], target=-1 -> [1, 2] (-1+0=-1)

NOTE: Return 1-indexed (add 1 to your indices)

Implement the function below:
"""


def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    """Return 1-indexed positions of two numbers that sum to target."""
    count = 0
    reverse_count = -1
    length = len(numbers)

    for _ in numbers:
        p1 = numbers[count]
        p2 = numbers[reverse_count]

        if p1 + p2 == target:
            return list([count + 1, (length - abs(reverse_count)) + 1])
        
        if p1 + p2 > target:
            reverse_count -= 1
        else:
            count += 1
        


# ============================================
# REVISION: Quick Review from Module 2
# ============================================

"""
REVISION: Check if two numbers in a SET sum to target.

Use a set for O(1) lookup. For each number, check if its complement exists.

Example: nums={2, 7, 11, 15}, target=9 -> True (2+7=9)
"""


def revision_two_sum(nums: set[int], target: int) -> bool:
    """Return True if any two numbers in the set sum to target."""
    seen = set()
    for num in nums:
        diff = target - num
        if diff in seen:
            return True
        seen.add(num)
    return False
# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("MODULE 3: Two Pointers")
    print("=" * 60)

    # Test Example
    print("\n--- Example: Valid Palindrome ---")
    assert is_palindrome_example("A man, a plan, a canal: Panama") == True
    assert is_palindrome_example("race a car") == False
    assert is_palindrome_example(" ") == True
    print("Example tests passed!")

    # Test Question 1
    print("\n--- Question 1: Reverse String ---")
    try:
        s1 = ["h", "e", "l", "l", "o"]
        reverse_string(s1)
        assert s1 == ["o", "l", "l", "e", "h"], "Basic case"

        s2 = ["H", "a", "n", "n", "a", "h"]
        reverse_string(s2)
        assert s2 == ["h", "a", "n", "n", "a", "H"], "Palindrome"

        s3 = ["a"]
        reverse_string(s3)
        assert s3 == ["a"], "Single element"

        s4 = ["a", "b"]
        reverse_string(s4)
        assert s4 == ["b", "a"], "Two elements"

        # Edge cases
        s5 = []
        reverse_string(s5)
        assert s5 == [], "Empty list"

        s6 = ["a", "b", "c"]
        reverse_string(s6)
        assert s6 == ["c", "b", "a"], "Odd number of elements"

        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2 (LeetCode #167)
    print("\n--- Question 2: Two Sum II - Sorted (LeetCode #167) ---")
    try:
        assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2], "Basic case"
        assert two_sum_sorted([2, 3, 4], 6) == [1, 3], "Middle skip"
        assert two_sum_sorted([-1, 0], -1) == [1, 2], "Negative numbers"
        assert two_sum_sorted([1, 2, 3, 4, 5], 9) == [4, 5], "End pair"
        assert two_sum_sorted([1, 2, 3, 4, 5], 3) == [1, 2], "Start pair"
        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    # ==========================================
    # REVISION: Module 2 (Hash Maps & Sets)
    # ==========================================
    print("\n--- REVISION: Hash Maps & Sets ---")
    try:
        assert revision_two_sum({2, 7, 11, 15}, 9) == True, "Sum exists"
        assert revision_two_sum({1, 2, 3}, 10) == False, "Sum doesn't exist"
        print("Revision PASSED!")
    except AssertionError as e:
        print(f"Revision FAILED: {e}")
    except Exception as e:
        print(f"Revision ERROR: {e}")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Two pointers from opposite ends: great for sorted arrays
2. Move pointers based on comparison with target
3. In-place operations often use two pointers + swapping
4. Remember: while left < right (not <=, unless needed)
5. Sorted arrays enable O(n) instead of O(n^2) for pair problems
""")
