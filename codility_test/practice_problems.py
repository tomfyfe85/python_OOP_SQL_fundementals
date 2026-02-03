"""
Codility Practice Problems

Common problems you'll encounter on Codility tests.
Each problem includes:
- Problem description
- Solution template (try yourself first!)
- Reference solution
- Test cases
"""


# ============================================
# PROBLEM 1: BinaryGap
# Difficulty: Easy | Lesson: Iterations
# ============================================

"""
PROBLEM: Find the longest sequence of zeros in binary representation of N.

A binary gap is a maximal sequence of consecutive zeros surrounded by ones.

Examples:
- N=1041 (10000010001) -> 5 (gap between position 4 and 9)
- N=32 (100000) -> 0 (zeros not surrounded by ones on both sides)
- N=15 (1111) -> 0 (no zeros)
"""

def binary_gap_solution(N):
    binary = bin(N)[2:]

    max_gap = 0
    current = 0

    for bit in binary:
        if bit == '0':
            current += 1
        else:
            max_gap = max(max_gap, current)
            current = 0

    return max_gap







# ============================================
# PROBLEM 2: CyclicRotation
# Difficulty: Easy | Lesson: Arrays
# ============================================

"""
PROBLEM: Rotate array A to the right by K positions.

Examples:
- A=[3,8,9,7,6], K=3 -> [9,7,6,3,8]
- A=[1,2,3,4], K=2 -> [3,4,1,2]
"""

from collections import deque
def cyclic_rotation_solution(A, K):
    dq = deque(A)
    dq.rotate(K)
    # print(list(dq))
    return list(dq)
  













# def cyclic_rotation_solution(A, K):
#     if len(A) == 0:
#         return A

#     K = K % len(A)  # Handle K > len(A)
#     return A[-K:] + A[:-K]


# ============================================
# PROBLEM 3: OddOccurrencesInArray
# Difficulty: Easy | Lesson: Arrays
# ============================================

"""
PROBLEM: Find the element that occurs an odd number of times.

Array has odd length. All elements except one occur an even number of times.

Examples:
- [9,3,9,3,9,7,9] -> 7
- [1,1,2] -> 2
"""


def odd_occurrences_template(A):
    """Try implementing this yourself first!"""
    pass


def odd_occurrences_solution(A):
    # XOR trick: a ^ a = 0, so pairs cancel out
    result = 0
    for num in A:
        result ^= num
    return result


# ============================================
# PROBLEM 4: FrogJmp
# Difficulty: Easy | Lesson: Time Complexity
# ============================================

"""
PROBLEM: Count minimal jumps from X to Y with jump distance D.

Examples:
- X=10, Y=85, D=30 -> 3 (jumps to 40, 70, 100)
- X=10, Y=10, D=5 -> 0 (already there)
"""


def frog_jmp_template(X, Y, D):
    """Try implementing this yourself first!"""
    pass


def frog_jmp_solution(X, Y, D):
    import math
    distance = Y - X
    return math.ceil(distance / D)


# ============================================
# PROBLEM 5: PermMissingElem
# Difficulty: Easy | Lesson: Time Complexity
# ============================================

"""
PROBLEM: Find missing element in array containing 1 to N+1.

Array A has N elements from range [1..N+1]. One element is missing.

Examples:
- [2,3,1,5] -> 4
- [1] -> 2
"""


def perm_missing_template(A):
    """Try implementing this yourself first!"""
    pass


def perm_missing_solution(A):
    n = len(A) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(A)
    return expected_sum - actual_sum


# ============================================
# PROBLEM 6: TapeEquilibrium
# Difficulty: Easy | Lesson: Time Complexity
# ============================================

"""
PROBLEM: Minimize |sum of left part - sum of right part|.

Split array at position P (1 <= P < N).
Find P that minimizes absolute difference.

Examples:
- [3,1,2,4,3] -> 1 (split as [3,1,2] and [4,3]: |6-7|=1)
"""


def tape_equilibrium_template(A):
    """Try implementing this yourself first!"""
    pass


def tape_equilibrium_solution(A):
    total = sum(A)
    left_sum = 0
    min_diff = float('inf')

    for i in range(len(A) - 1):  # Don't include last element
        left_sum += A[i]
        right_sum = total - left_sum
        diff = abs(left_sum - right_sum)
        min_diff = min(min_diff, diff)

    return min_diff


# ============================================
# PROBLEM 7: FrogRiverOne
# Difficulty: Easy | Lesson: Counting Elements
# ============================================

"""
PROBLEM: Find earliest time when frog can cross river.

Leaves fall at positions A[K] at time K.
Frog needs leaves at all positions 1..X to cross.

Examples:
- X=5, A=[1,3,1,4,2,3,5,4] -> 6 (at time 6, positions 1-5 are covered)
- X=2, A=[1,1,1] -> -1 (position 2 never gets a leaf)
"""


def frog_river_template(X, A):
    """Try implementing this yourself first!"""
    pass


def frog_river_solution(X, A):
    needed = set(range(1, X + 1))

    for time, position in enumerate(A):
        needed.discard(position)
        if not needed:
            return time

    return -1


# ============================================
# PROBLEM 8: MaxCounters
# Difficulty: Medium | Lesson: Counting Elements
# ============================================

"""
PROBLEM: Apply operations on N counters.

Operations:
- increase(X): counter X += 1
- max_counter: set all counters to current max

A[K] = X means increase(X) if 1 <= X <= N
A[K] = N+1 means max_counter

Examples:
- N=5, A=[3,4,4,6,1,4,4] -> [3,2,2,4,2]
"""


def max_counters_template(N, A):
    """Try implementing this yourself first!"""
    pass


def max_counters_solution(N, A):
    counters = [0] * N
    max_val = 0
    last_max = 0  # Lazy propagation

    for op in A:
        if op <= N:
            idx = op - 1
            # Apply lazy update if needed
            if counters[idx] < last_max:
                counters[idx] = last_max
            counters[idx] += 1
            max_val = max(max_val, counters[idx])
        else:
            last_max = max_val

    # Final lazy propagation
    for i in range(N):
        if counters[i] < last_max:
            counters[i] = last_max

    return counters


# ============================================
# PROBLEM 9: PassingCars
# Difficulty: Easy | Lesson: Prefix Sums
# ============================================

"""
PROBLEM: Count passing cars (P traveling east, Q traveling west).

A[i] = 0 means car traveling east
A[i] = 1 means car traveling west
Count pairs (P, Q) where P < Q, A[P]=0, A[Q]=1

Examples:
- [0,1,0,1,1] -> 5
"""


def passing_cars_template(A):
    """Try implementing this yourself first!"""
    pass


def passing_cars_solution(A):
    east_count = 0
    passing = 0

    for car in A:
        if car == 0:
            east_count += 1
        else:
            passing += east_count
            if passing > 1_000_000_000:
                return -1

    return passing


# ============================================
# PROBLEM 10: MaxProfit (Stock)
# Difficulty: Easy | Lesson: Maximum Slice
# ============================================

"""
PROBLEM: Find max profit from buying and selling stock.

A[i] is price on day i. Buy on one day, sell on a later day.

Examples:
- [23171,21011,21123,21366,21013,21367] -> 356 (buy at 21011, sell at 21367)
"""


def max_profit_template(A):
    """Try implementing this yourself first!"""
    pass


def max_profit_solution(A):
    if len(A) < 2:
        return 0

    min_price = A[0]
    max_profit = 0

    for price in A[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit


# ============================================
# TEST ALL SOLUTIONS
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("CODILITY PRACTICE PROBLEMS - TEST RESULTS")
    print("=" * 60)

    # Test BinaryGap
    print("\n1. BinaryGap")
    assert binary_gap_solution(1041) == 5
    assert binary_gap_solution(32) == 0
    assert binary_gap_solution(15) == 0
    print("   PASSED")

    # Test CyclicRotation
    print("\n2. CyclicRotation")
    assert cyclic_rotation_solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
    assert cyclic_rotation_solution([1, 2, 3, 4], 2) == [3, 4, 1, 2]
    assert cyclic_rotation_solution([], 5) == []
    print("   PASSED")

    # # Test OddOccurrences
    # print("\n3. OddOccurrencesInArray")
    # assert odd_occurrences_solution([9, 3, 9, 3, 9, 7, 9]) == 7
    # assert odd_occurrences_solution([1, 1, 2]) == 2
    # print("   PASSED")

    # # Test FrogJmp
    # print("\n4. FrogJmp")
    # assert frog_jmp_solution(10, 85, 30) == 3
    # assert frog_jmp_solution(10, 10, 5) == 0
    # print("   PASSED")

    # # Test PermMissingElem
    # print("\n5. PermMissingElem")
    # assert perm_missing_solution([2, 3, 1, 5]) == 4
    # assert perm_missing_solution([1]) == 2
    # print("   PASSED")

    # # Test TapeEquilibrium
    # print("\n6. TapeEquilibrium")
    # assert tape_equilibrium_solution([3, 1, 2, 4, 3]) == 1
    # print("   PASSED")

    # # Test FrogRiverOne
    # print("\n7. FrogRiverOne")
    # assert frog_river_solution(5, [1, 3, 1, 4, 2, 3, 5, 4]) == 6
    # assert frog_river_solution(2, [1, 1, 1]) == -1
    # print("   PASSED")

    # # Test MaxCounters
    # print("\n8. MaxCounters")
    # assert max_counters_solution(5, [3, 4, 4, 6, 1, 4, 4]) == [3, 2, 2, 4, 2]
    # print("   PASSED")

    # # Test PassingCars
    # print("\n9. PassingCars")
    # assert passing_cars_solution([0, 1, 0, 1, 1]) == 5
    # print("   PASSED")

    # # Test MaxProfit
    # print("\n10. MaxProfit")
    # assert max_profit_solution([23171, 21011, 21123, 21366, 21013, 21367]) == 356
    # assert max_profit_solution([5, 4, 3, 2, 1]) == 0
    # print("   PASSED")

    # print("\n" + "=" * 60)
    # print("ALL TESTS PASSED!")
    # print("=" * 60)
    # print("\nTry implementing the _template functions yourself,")
    # print("then compare with the _solution functions.")
