"""
TestGorilla Prep - Module 6: Test-Taking Strategies
====================================================

General strategies and tips for cognitive ability tests.
"""


# ============================================
# BEFORE THE TEST
# ============================================

BEFORE_TEST = """
BEFORE THE TEST:

1. ENVIRONMENT
   - Find a quiet place with no distractions
   - Use a computer (not phone) if possible
   - Ensure stable internet connection
   - Close other browser tabs and applications
   - Have paper and pen ready for notes

2. PHYSICAL PREPARATION
   - Get a good night's sleep
   - Eat a light meal beforehand
   - Avoid caffeine if it makes you jittery
   - Use the bathroom before starting
   - Have water nearby

3. TECHNICAL SETUP
   - Use Chrome or Firefox (most compatible)
   - Check your webcam if required
   - Test your audio if required
   - Disable notifications on your computer

4. MENTAL PREPARATION
   - Read all instructions carefully
   - Do any practice questions offered
   - Take a few deep breaths
   - Remember: it's about demonstrating YOUR ability
"""


# ============================================
# DURING THE TEST
# ============================================

DURING_TEST = """
DURING THE TEST:

1. TIME MANAGEMENT
   - Note how many questions and total time
   - Calculate rough time per question
   - Don't spend too long on any single question
   - If stuck for >30 seconds, make best guess and move on
   - Some tests don't let you go back - keep moving

2. QUESTION STRATEGY
   - Read the question TWICE before answering
   - Identify what's actually being asked
   - Eliminate obviously wrong answers first
   - If two answers seem correct, look for subtle differences
   - Trust your first instinct if unsure

3. COMMON TRAPS TO AVOID
   - Rushing through easy questions (they still count!)
   - Spending too long on hard questions
   - Changing answers without good reason
   - Not reading all options before choosing
   - Assuming questions are harder than they are

4. STAY CALM
   - If you don't know an answer, that's okay
   - Some questions are designed to be very hard
   - Your score is relative to other candidates
   - One wrong answer won't fail you
"""


# ============================================
# QUESTION TYPE STRATEGIES
# ============================================

QUESTION_STRATEGIES = """
STRATEGIES BY QUESTION TYPE:

NUMERICAL REASONING:
- Estimate first, calculate second
- Use benchmarks: 10% = ÷10, 50% = ÷2
- For sequences: check differences, then ratios
- Round numbers for quick mental math
- Write calculations down - don't rely on memory

LOGICAL REASONING:
- Draw diagrams for spatial/ordering problems
- For if-then: remember the valid forms (modus ponens/tollens)
- For syllogisms: draw Venn diagrams
- Watch for: "some" vs "all", exceptions, negatives

VERBAL REASONING:
- For analogies: identify relationship FIRST
- For comprehension: answer from TEXT only, not knowledge
- "Cannot say" ≠ "I don't know"
- FALSE means contradicts text, not just "not mentioned"

PROBLEM SOLVING:
- Break complex problems into steps
- Write down constraints/rules
- Work backwards from answers if helpful
- Check your answer against ALL conditions

ATTENTION TO DETAIL:
- Go systematically (left to right, top to bottom)
- Compare character by character
- Watch for: 0/O, 1/l/I, similar-sounding words
- Verify numbers by adding twice
"""


# ============================================
# TIME MANAGEMENT CALCULATOR
# ============================================

def calculate_pace():
    """Calculate recommended pace for a test."""
    print("\n" + "=" * 60)
    print("TIME MANAGEMENT CALCULATOR")
    print("=" * 60)

    try:
        total_time = int(input("Total test time (minutes): "))
        num_questions = int(input("Number of questions: "))

        seconds_per_question = (total_time * 60) / num_questions
        minutes_per_question = total_time / num_questions

        print(f"\n{'─' * 40}")
        print(f"Time per question: {seconds_per_question:.0f} seconds ({minutes_per_question:.1f} minutes)")
        print(f"{'─' * 40}")

        print("\nRecommended pace:")
        print(f"- After 25% of time ({total_time * 0.25:.0f} min): Complete {num_questions * 0.25:.0f} questions")
        print(f"- After 50% of time ({total_time * 0.5:.0f} min): Complete {num_questions * 0.5:.0f} questions")
        print(f"- After 75% of time ({total_time * 0.75:.0f} min): Complete {num_questions * 0.75:.0f} questions")
        print(f"- Leave 2-3 minutes at end to review flagged questions")

        if seconds_per_question < 30:
            print("\n⚠️  This is a FAST-PACED test. Trust instincts, don't overthink!")
        elif seconds_per_question < 60:
            print("\n📝 Moderate pace. Balance speed with accuracy.")
        else:
            print("\n✓ Comfortable pace. Take time to think through each question.")

    except ValueError:
        print("Please enter valid numbers.")


# ============================================
# PRACTICE SCORE TRACKER
# ============================================

def track_practice():
    """Track practice scores to monitor improvement."""
    print("\n" + "=" * 60)
    print("PRACTICE SCORE TRACKER")
    print("=" * 60)
    print("""
Record your practice scores here to track improvement.

Recommended practice schedule:
- Day 1: Numerical Reasoning
- Day 2: Logical Reasoning
- Day 3: Verbal Reasoning
- Day 4: Problem Solving
- Day 5: Attention to Detail
- Day 6: Mixed practice (all types)
- Day 7: Review weak areas
""")

    print("\nTo track scores, create a simple log:")
    print("""
Date       | Module              | Score | Notes
───────────┼─────────────────────┼───────┼────────────────────
2024-01-15 | Numerical           | 7/10  | Struggled with %
2024-01-16 | Logical             | 8/10  | Good at syllogisms
2024-01-17 | Verbal              | 6/10  | Review analogies
...
""")


# ============================================
# COMMON MISTAKES
# ============================================

COMMON_MISTAKES = """
COMMON MISTAKES TO AVOID:

1. MISREADING THE QUESTION
   - "Which is NOT true?" - watch for negatives
   - "All of the following EXCEPT" - inverted question
   - "Most likely" vs "Definitely"

2. OVERTHINKING
   - The obvious answer is often correct
   - Don't add complexity that isn't there
   - If it seems too easy, it might just be easy

3. PATTERN ASSUMPTIONS
   - Don't assume the pattern you found is the only one
   - Check your pattern works for ALL given terms
   - Some sequences have two interleaved patterns

4. TIME PRESSURE ERRORS
   - Misreading numbers (123 vs 132)
   - Skipping negative signs
   - Forgetting to convert units

5. CONFIDENCE TRAPS
   - Changing correct answers to wrong ones
   - Second-guessing yourself too much
   - OR not checking confident answers

6. COMPREHENSION ERRORS
   - Using outside knowledge instead of passage info
   - Confusing "false" with "cannot say"
   - Not reading the full passage
"""


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("TEST-TAKING STRATEGIES")
    print("=" * 60)
    print("""
Choose a topic:
1. Before the Test
2. During the Test
3. Question Type Strategies
4. Time Management Calculator
5. Practice Score Tracker
6. Common Mistakes
7. Show All Tips
""")

    choice = input("Enter choice (1-7): ").strip()

    if choice == "1":
        print(BEFORE_TEST)
    elif choice == "2":
        print(DURING_TEST)
    elif choice == "3":
        print(QUESTION_STRATEGIES)
    elif choice == "4":
        calculate_pace()
    elif choice == "5":
        track_practice()
    elif choice == "6":
        print(COMMON_MISTAKES)
    elif choice == "7":
        print(BEFORE_TEST)
        print(DURING_TEST)
        print(QUESTION_STRATEGIES)
        print(COMMON_MISTAKES)
    else:
        print("Invalid choice.")

    print("\n" + "=" * 60)
    print("FINAL REMINDERS")
    print("=" * 60)
    print("""
✓ Get enough sleep the night before
✓ Find a quiet, distraction-free environment
✓ Have paper and pen ready
✓ Read questions carefully
✓ Don't spend too long on any one question
✓ Trust your first instinct
✓ Stay calm - you've prepared for this!

Good luck! 🍀
""")
