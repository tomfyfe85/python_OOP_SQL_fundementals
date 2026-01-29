"""
MissingInteger Problem - Solution Review

PROBLEM: Find the smallest positive integer (greater than 0) that does not occur in array A.

Examples:
- [1, 3, 6, 4, 1, 2] -> 5
- [1, 2, 3] -> 4
- [-1, -3] -> 1
- [2, 3, 4] -> 1
"""


# ============================================
# YOUR ORIGINAL SOLUTION (33% score)
# ============================================

def solution_original(A):
    if len(A) == 0:
        return 1

    A.sort()
    neg_num = A[-1]
    if neg_num < 0 and neg_num != -1:
        return neg_num + 1
    if neg_num == -1:
        return 1

    num = 1
    for i in A:
        if i == num:
            continue
        if i == num + 1:
            num += 1
        else:
            return num + 1
    return A[-1] + 1


# ============================================
# WHY IT FAILED - Bug Analysis
# ============================================

"""
BUG 1: Doesn't check if 1 exists
---------------------------------------
Your code starts tracking from A[0], but the problem needs the smallest
POSITIVE integer starting from 1.

    A = [2, 3, 4]
    - Your code: num=2, increments to 4, returns 5
    - Correct: 1 is missing, return 1

    A = [2]
    - Your code: returns 3
    - Correct: return 1


BUG 2: Negative number handling returns wrong values
---------------------------------------
    neg_num = A[-1]  # This is the MAX value, not necessarily negative!

    A = [-3, -2]
    - neg_num = -2
    - Condition: -2 < 0 and -2 != -1 is True
    - Returns: -2 + 1 = -1  (WRONG! Should be 1)


BUG 3: Loop logic assumes sequence starts at A[0]
---------------------------------------
The loop looks for consecutive numbers starting from A[0],
but should look for 1, 2, 3, 4... regardless of what's in the array.
"""


# ============================================
# CORRECT SOLUTION - Using Set (Recommended)
# ============================================

def solution_set(A):
    """
    O(n) time, O(n) space - Clean and readable.
    This approach is recommended for interviews.
    """
    # Only keep positive integers in a set for O(1) lookup
    positive = set(x for x in A if x > 0)

    # Check 1, 2, 3, ... until we find one missing
    i = 1
    while i in positive:
        i += 1
    return i


# ============================================
# CORRECT SOLUTION - In-Place (Advanced)
# ============================================

def solution_inplace(A):
    """
    O(n) time, O(1) space - Uses array itself as hash map.
    More complex but shows deeper understanding.

    Key insight: Answer must be in range [1, len(A)+1]
    - If array has n elements, at most n distinct positive integers
    - So answer is at most n+1
    """
    n = len(A)

    # Step 1: Place each number x at index x-1 (if valid)
    # After this: A[i] should equal i+1 if i+1 exists in original array
    for i in range(n):
        while 1 <= A[i] <= n and A[A[i] - 1] != A[i]:
            # Swap A[i] to its correct position
            target_idx = A[i] - 1
            A[i], A[target_idx] = A[target_idx], A[i]

    # Step 2: Find first position where A[i] != i+1
    for i in range(n):
        if A[i] != i + 1:
            return i + 1

    # All positions filled correctly, answer is n+1
    return n + 1


# ============================================
# TEST CASES
# ============================================

if __name__ == "__main__":
    test_cases = [
        ([1, 3, 6, 4, 1, 2], 5),
        ([1, 2, 3], 4),
        ([-1, -3], 1),
        ([2, 3, 4], 1),           # BUG 1: Your code returns 5
        ([2], 1),                  # BUG 1: Your code returns 3
        ([-3, -2], 1),            # BUG 2: Your code returns -1
        ([1], 2),
        ([], 1),
        ([1, 2, 3, 4, 5], 6),
        ([5, 4, 3, 2, 1], 6),
        ([1, 1, 1, 1], 2),
        ([-1, 0, 1, 2, 3], 4),
        ([100, 200, 300], 1),
    ]

    print("=" * 60)
    print("COMPARING SOLUTIONS")
    print("=" * 60)

    for A, expected in test_cases:
        A_copy1 = A.copy()
        A_copy2 = A.copy()
        A_copy3 = A.copy()

        try:
            original = solution_original(A_copy1)
        except Exception as e:
            original = f"ERROR: {e}"

        set_result = solution_set(A_copy2)
        inplace_result = solution_inplace(A_copy3)

        original_status = "PASS" if original == expected else "FAIL"
        set_status = "PASS" if set_result == expected else "FAIL"
        inplace_status = "PASS" if inplace_result == expected else "FAIL"

        print(f"\nInput: {A}")
        print(f"  Expected: {expected}")
        print(f"  Original: {original} [{original_status}]")
        print(f"  Set:      {set_result} [{set_status}]")
        print(f"  In-place: {inplace_result} [{inplace_status}]")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS")
    print("=" * 60)
    print("""
1. Always consider edge cases FIRST:
   - Empty array
   - All negative numbers
   - Array missing 1 (the smallest positive)
   - Array with duplicates

2. The set-based solution is clean and efficient enough (O(n))

3. The in-place solution shows deeper algorithmic thinking:
   - Recognize that answer is bounded by len(A)+1
   - Use the array itself as a hash map
""")
