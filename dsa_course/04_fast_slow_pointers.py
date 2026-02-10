"""
DSA Course - Module 4: Fast & Slow Pointers (Floyd's Tortoise & Hare)
====================================================================

CONCEPT: Fast and Slow Pointers
-------------------------------
Two pointers moving at different speeds through a SEQUENCE.
Typically: slow moves 1 step, fast moves 2 steps.

THE KEY INSIGHT:
If there's a cycle, fast will eventually "lap" slow and they'll meet.
If there's no cycle, fast will reach the end.

IMPORTANT: This pattern works on ANY sequence, not just linked lists.
A "sequence" is anything where you can compute the next value from the current one:
- Repeatedly applying a math function to a number
- Following indices in an array
- Traversing nodes in a linked list (covered in Module 5)

WHY IT WORKS (intuition, no math needed):
- Think of two runners on a circular track
- The faster one will eventually catch up to the slower one
- They must meet if the track loops back

MAIN USE CASES:
1. CYCLE DETECTION - Do we ever revisit the same state?
2. FINDING CYCLE START - Where does the loop begin?
3. FINDING MIDDLE - When fast reaches end, slow is at middle
"""


# ============================================
# EXAMPLE: Cycle Detection in a Number Sequence
# ============================================

def example_detect_cycle():
    """
    Demonstrate cycle detection using the digit-square-sum sequence.

    Take any number and repeatedly replace it with the sum of squares of its digits:
        19 -> 1² + 9² = 82 -> 8² + 2² = 68 -> 6² + 8² = 100 -> 1 -> 1 -> 1 (reaches 1, stays there)
        2  -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 (CYCLE! 4 appeared before)

    We can detect whether this sequence cycles back on itself using fast/slow pointers,
    WITHOUT storing every number we've seen.
    """

    def next_val(n):
        """Compute sum of squares of digits."""
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total

    # Let's trace with n = 2
    print("Tracing sequence starting from 2:")
    val = 2
    for _ in range(12):
        print(f"  {val} -> ", end="")
        val = next_val(val)
    print(f"{val} ...")

    # Now let's use fast/slow pointers to detect the cycle
    print("\nFast/slow pointer detection starting from 2:")
    slow = 2
    fast = 2
    step = 0

    while True:
        slow = next_val(slow)          # 1 step
        fast = next_val(next_val(fast)) # 2 steps
        step += 1
        print(f"  Step {step}: slow={slow}, fast={fast}")
        if slow == fast:
            print(f"  -> They met at {slow}! Cycle detected.")
            break

    # Now trace starting from 19 (which reaches 1)
    print("\nTracing sequence starting from 19:")
    val = 19
    for _ in range(8):
        print(f"  {val} -> ", end="")
        val = next_val(val)
    print(f"{val} ...")
    print("  -> Reaches 1 and stays at 1 (a fixed point, not a harmful cycle)")


example_detect_cycle()


# ============================================
# QUESTION 1: Sequence Cycle Detection
# ============================================

"""
PROBLEM: Detect if applying a function repeatedly creates a cycle.

Given a starting value and a function f, the sequence is:
    x, f(x), f(f(x)), f(f(f(x))), ...

Use fast and slow pointers to determine:
- Does the sequence reach a target value, OR
- Does it enter a cycle (revisiting a value without hitting the target)?

Return True if the sequence reaches the target, False if it cycles without reaching it.

Examples:
    start=19, f=digit_square_sum, target=1 -> True  (19 -> 82 -> 68 -> ... -> 1)
    start=2,  f=digit_square_sum, target=1 -> False (2 -> 4 -> 16 -> ... -> 4 CYCLE)
    start=5,  f=digit_square_sum, target=1 -> False (5 -> 25 -> 29 -> ... cycles)

Hint: How do you handle the case where the target IS part of a cycle (like 1 -> 1 -> 1)?
      If slow or fast ever equals the target, return True immediately.
"""


def reaches_target(start: int, f, target: int) -> bool:
    """
    Return True if repeatedly applying f(x) starting from start eventually reaches target.
    Return False if the sequence enters a cycle without reaching target.
    """
    # YOUR CODE HERE
    pass


# ============================================
# QUESTION 2 (CAPSTONE): Happy Number - LeetCode #202
# ============================================

"""
PROBLEM: Determine if a number is "happy".  (LeetCode #202)

A happy number is defined by this process:
1. Start with any positive integer
2. Replace it with the sum of squares of its digits
3. Repeat until you get 1 (happy!) or enter an endless cycle (not happy)

Examples:
- 19 -> 1² + 9² = 82 -> 8² + 2² = 68 -> 6² + 8² = 100
       -> 1² + 0² + 0² = 1 -> HAPPY!
- 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> CYCLE, not happy

You could solve this with a set (store seen numbers), but the fast/slow pointer
approach uses O(1) space — no extra storage needed.

Implement using fast and slow pointers:
"""


def is_happy(n: int) -> bool:
    """Return True if n is a happy number, False otherwise."""
    # YOUR CODE HERE
    # Hint: You'll need a helper to compute the next number in the sequence.
    pass


# ============================================
# REVISION: Quick Review from Module 3
# ============================================

"""
REVISION: Check if a string is a palindrome using two pointers.

Use left and right pointers converging toward the center.

Example: "racecar" -> True, "hello" -> False
"""


def revision_is_palindrome(s: str) -> bool:
    """Return True if the string is a palindrome."""
    # YOUR CODE HERE
    pass


# ============================================
# TEST CASES - Run to verify your solutions
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("MODULE 4: Fast & Slow Pointers")
    print("=" * 60)

    # Test Question 1
    print("\n--- Question 1: Sequence Cycle Detection ---")
    try:
        def digit_square_sum(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10
            return total

        assert reaches_target(19, digit_square_sum, 1) == True, "19 reaches 1"
        assert reaches_target(2, digit_square_sum, 1) == False, "2 cycles, never reaches 1"
        assert reaches_target(7, digit_square_sum, 1) == True, "7 reaches 1"
        assert reaches_target(4, digit_square_sum, 1) == False, "4 cycles"
        assert reaches_target(1, digit_square_sum, 1) == True, "1 is already the target"

        print("All Question 1 tests PASSED!")
    except AssertionError as e:
        print(f"Question 1 FAILED: {e}")
    except Exception as e:
        print(f"Question 1 ERROR: {e}")

    # Test Question 2 (Capstone)
    print("\n--- Question 2 (Capstone): Happy Number - LeetCode #202 ---")
    try:
        assert is_happy(19) == True, "19 is happy"
        assert is_happy(2) == False, "2 is not happy"
        assert is_happy(1) == True, "1 is happy"
        assert is_happy(7) == True, "7 is happy"
        assert is_happy(4) == False, "4 is not happy"
        assert is_happy(100) == True, "100 -> 1"
        assert is_happy(10) == True, "10 is happy"
        print("All Question 2 tests PASSED!")
    except AssertionError as e:
        print(f"Question 2 FAILED: {e}")
    except Exception as e:
        print(f"Question 2 ERROR: {e}")

    # ==========================================
    # REVISION: Module 3 (Two Pointers)
    # ==========================================
    print("\n--- REVISION: Two Pointers ---")
    try:
        assert revision_is_palindrome("racecar") == True
        assert revision_is_palindrome("hello") == False
        assert revision_is_palindrome("a") == True
        assert revision_is_palindrome("") == True
        print("Revision PASSED!")
    except AssertionError as e:
        print(f"Revision FAILED: {e}")
    except Exception as e:
        print(f"Revision ERROR: {e}")

    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("""
1. Fast & slow pointers: slow moves 1 step, fast moves 2 steps
2. Cycle detection: if they meet, the sequence loops
3. This works on ANY sequence — numbers, arrays, linked lists
4. Happy Number: classic application without linked lists
5. O(1) space: no need to store every value you've seen
6. In Module 5 (Linked Lists), we'll revisit this pattern on nodes!
""")
