"""
Codility Test Preparation Tips & Strategies

A comprehensive guide to acing Codility assessments.
"""


# ============================================
# UNDERSTANDING CODILITY SCORING
# ============================================

"""
SCORING BREAKDOWN:
------------------
1. Correctness (typically 50-60%):
   - Does your code produce correct output?
   - Tests edge cases, typical cases, extreme values

2. Performance (typically 40-50%):
   - Does your code run fast enough?
   - Tests with large inputs (N up to 100,000 or 1,000,000)

IMPORTANT: Example tests are NOT part of your score!
The real tests are hidden. Passing examples means nothing.
"""


# ============================================
# BEFORE YOU CODE: THE 5-MINUTE RULE
# ============================================

"""
Spend 5 minutes BEFORE writing any code:

1. READ THE PROBLEM TWICE
   - What exactly is being asked?
   - What are the constraints (N range, value range)?

2. IDENTIFY EDGE CASES
   - Empty input: [], 0, ""
   - Single element: [1], N=1
   - All same values: [5,5,5,5]
   - Negative numbers: [-1,-2,-3]
   - Maximum values: N=100000
   - Minimum case: What's the smallest valid input?

3. DETERMINE REQUIRED COMPLEXITY
   - N up to 100 -> O(N^3) might work
   - N up to 1,000 -> O(N^2) should work
   - N up to 100,000 -> O(N log N) needed
   - N up to 1,000,000 -> O(N) required

4. WRITE TEST CASES FIRST
   - Think of 3-5 test cases BEFORE coding
   - Include at least one edge case
"""


# ============================================
# COMMON PATTERNS & TECHNIQUES
# ============================================

"""
PATTERN 1: Hash Set for O(1) Lookup
-----------------------------------
When you need to check "does X exist?" repeatedly.

    # BAD: O(n) for each check
    if x in list_of_items:

    # GOOD: O(1) for each check
    items_set = set(list_of_items)
    if x in items_set:


PATTERN 2: Prefix Sum for Range Queries
---------------------------------------
When you need sum of subarray multiple times.

    # Compute prefix sums once
    prefix = [0]
    for x in A:
        prefix.append(prefix[-1] + x)

    # Sum from index i to j (inclusive) in O(1)
    range_sum = prefix[j+1] - prefix[i]


PATTERN 3: Two Pointers
-----------------------
When scanning from both ends or maintaining a window.

    left, right = 0, len(A) - 1
    while left < right:
        # process A[left] and A[right]
        if some_condition:
            left += 1
        else:
            right -= 1


PATTERN 4: Sorting Changes Everything
-------------------------------------
Many O(N^2) problems become O(N log N) with sorting.

    A.sort()  # O(N log N)
    # Now adjacent elements are related


PATTERN 5: XOR for Finding Unpaired
-----------------------------------
XOR cancels pairs: a ^ a = 0

    result = 0
    for x in A:
        result ^= x
    # result is the unpaired element


PATTERN 6: Counting / Frequency Map
-----------------------------------
    from collections import Counter
    freq = Counter(A)
    # freq[x] = number of times x appears


PATTERN 7: Greedy with Sorting
------------------------------
Many optimization problems:
1. Sort by some criteria
2. Iterate and make locally optimal choice


PATTERN 8: Sliding Window
-------------------------
For subarray/substring problems with constraints.

    left = 0
    for right in range(len(A)):
        # Expand window by including A[right]
        while window_invalid:
            # Shrink from left
            left += 1
"""


# ============================================
# COMPLEXITY CHEAT SHEET
# ============================================

def complexity_examples():
    """
    Common time complexities and what they mean for Codility:

    O(1)        - Constant: math operations, hash lookups
    O(log N)    - Logarithmic: binary search
    O(N)        - Linear: single loop through array
    O(N log N)  - Linearithmic: sorting, then linear scan
    O(N^2)      - Quadratic: nested loops (often too slow!)
    O(2^N)      - Exponential: all subsets (never use on Codility)

    RULE OF THUMB:
    - 10^8 operations per second is safe
    - N=100,000 with O(N^2) = 10^10 operations = TOO SLOW
    - N=100,000 with O(N log N) = ~1.7*10^6 = FAST
    """
    pass


# ============================================
# DEBUGGING STRATEGIES
# ============================================

"""
1. USE PRINT STATEMENTS (they show in output!)
   print(f"DEBUG: A={A}, current_sum={s}")

2. TEST LOCALLY FIRST
   - Write your own test cases
   - Run before submitting

3. CHECK BOUNDARY CONDITIONS
   - Off-by-one errors are common
   - range(n) vs range(n+1)
   - A[-1] when A is empty

4. VERIFY YOUR UNDERSTANDING
   - Re-read the problem
   - Are you solving what they asked?
"""


# ============================================
# COMMON MISTAKES TO AVOID
# ============================================

"""
MISTAKE 1: Not handling empty input
-----------------------------------
    def solution(A):
        return A[0]  # CRASH if A is empty!

    # FIX:
    def solution(A):
        if not A:
            return some_default
        return A[0]


MISTAKE 2: Integer overflow (less common in Python)
-----------------------------------
    # In Python, integers have arbitrary precision
    # But watch out for: return value > 1,000,000,000


MISTAKE 3: Modifying input while iterating
-----------------------------------
    for i, x in enumerate(A):
        if x < 0:
            A.remove(x)  # BUG: modifies list during iteration!

    # FIX: Use list comprehension
    A = [x for x in A if x >= 0]


MISTAKE 4: Using wrong data structure
-----------------------------------
    # Checking membership in list is O(N)
    if x in my_list:  # SLOW if done repeatedly

    # Use a set for O(1) membership
    my_set = set(my_list)
    if x in my_set:  # FAST


MISTAKE 5: Not considering negative numbers
-----------------------------------
    # Problem says "integers" not "positive integers"
    A = [-5, -3, -1, 2, 4]
    # Your code should handle this!


MISTAKE 6: Forgetting about duplicates
-----------------------------------
    A = [1, 1, 2, 2, 3, 3]
    len(A) != len(set(A))  # Different!
"""


# ============================================
# TEST STRATEGY CHECKLIST
# ============================================

def pre_submit_checklist():
    """
    Before clicking Submit, verify:

    [ ] Empty input handled?
    [ ] Single element input handled?
    [ ] All negative input handled?
    [ ] All same values handled?
    [ ] Maximum N handled efficiently?
    [ ] Return type correct?
    [ ] No hardcoded test cases?
    """
    pass


# ============================================
# EXAMPLE: APPLYING THE STRATEGIES
# ============================================

def missing_integer_properly(A):
    """
    Find smallest positive integer not in A.

    Let's apply our strategies:

    1. EDGE CASES:
       - Empty: return 1
       - All negative: return 1
       - Missing 1: return 1
       - Complete sequence [1,2,3]: return 4

    2. COMPLEXITY:
       - N up to 100,000
       - Need O(N) or O(N log N)

    3. PATTERN:
       - Hash set for O(1) lookup
    """
    # Handle edge case
    if not A:
        return 1

    # Use set for O(1) lookup
    positive = set(x for x in A if x > 0)

    # Check 1, 2, 3, ... (guaranteed answer <= N+1)
    i = 1
    while i in positive:
        i += 1

    return i


# ============================================
# PRACTICE ROUTINE
# ============================================

"""
RECOMMENDED PRACTICE PLAN:

Week 1: Easy Problems (15 min each)
- BinaryGap
- OddOccurrencesInArray
- CyclicRotation
- FrogJmp
- PermMissingElem

Week 2: Medium Problems (25 min each)
- MaxCounters
- MissingInteger
- CountDiv
- PassingCars
- GenomicRangeQuery

Week 3: Harder Problems (35 min each)
- MaxSliceSum
- Triangle
- NumberOfDiscIntersections
- Fish
- Nesting

TIPS:
1. Time yourself strictly
2. Don't look at solutions until you've tried
3. After solving, read the optimal solution
4. Redo problems you struggled with
"""


# ============================================
# QUICK REFERENCE: PYTHON TRICKS
# ============================================

"""
USEFUL PYTHON FOR CODILITY:

# Integer division (floor)
7 // 3  # = 2

# Ceiling division
import math
math.ceil(7 / 3)  # = 3
# Or: (a + b - 1) // b

# Sum formula: 1 + 2 + ... + n
n * (n + 1) // 2

# Sort in place vs return new
A.sort()           # Modifies A
sorted(A)          # Returns new list

# Sort by custom key
A.sort(key=lambda x: x[1])

# Counter for frequencies
from collections import Counter
freq = Counter([1, 2, 2, 3, 3, 3])
# freq = {1: 1, 2: 2, 3: 3}

# Default dict
from collections import defaultdict
d = defaultdict(int)  # Missing keys return 0
d = defaultdict(list) # Missing keys return []

# Binary search
from bisect import bisect_left, bisect_right

# Max/min with default
max(A, default=0)  # Returns 0 if A is empty
"""

if __name__ == "__main__":
    print("=" * 60)
    print("CODILITY TEST PREP - KEY POINTS")
    print("=" * 60)

    print("""
1. BEFORE CODING (5 min):
   - Read problem twice
   - List edge cases
   - Determine required complexity
   - Write test cases

2. COMMON PATTERNS:
   - Set for O(1) lookup
   - Prefix sum for range queries
   - Sorting + linear scan
   - Two pointers
   - XOR for unpaired elements

3. COMPLEXITY TARGETS:
   - N <= 1000: O(N^2) ok
   - N <= 100,000: Need O(N log N)
   - N <= 1,000,000: Need O(N)

4. BEFORE SUBMITTING:
   - Test empty input
   - Test single element
   - Test all negative
   - Test large N mentally

5. REMEMBER:
   - Example tests don't count!
   - Hidden tests are the real score
   - Performance is ~50% of score
""")

    # Test our properly implemented solution
    print("\nTesting missing_integer_properly:")
    test_cases = [
        ([1, 3, 6, 4, 1, 2], 5),
        ([1, 2, 3], 4),
        ([-1, -3], 1),
        ([2, 3, 4], 1),
        ([], 1),
    ]
    for A, expected in test_cases:
        result = missing_integer_properly(A.copy())
        status = "PASS" if result == expected else "FAIL"
        print(f"  {A} -> {result} [{status}]")
