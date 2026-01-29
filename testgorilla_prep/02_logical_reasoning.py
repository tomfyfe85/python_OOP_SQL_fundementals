"""
TestGorilla Prep - Module 2: Logical Reasoning
===============================================

WHAT IT TESTS:
- Pattern recognition (shapes, sequences)
- Deductive reasoning (if A then B)
- Syllogisms (All A are B, X is A, therefore...)
- Logical relationships

TIPS:
- Draw it out if needed
- Eliminate obviously wrong answers
- Check your logic by testing the reverse
- Don't add assumptions not given in the problem
"""

import random


# ============================================
# SECTION 1: DEDUCTIVE REASONING (IF-THEN)
# ============================================

"""
KEY LOGIC RULES:

1. MODUS PONENS (Valid):
   If A then B.
   A is true.
   Therefore B is true.

2. MODUS TOLLENS (Valid):
   If A then B.
   B is false.
   Therefore A is false.

3. AFFIRMING THE CONSEQUENT (INVALID!):
   If A then B.
   B is true.
   Therefore A is true.  <- WRONG! B could be true for other reasons.

4. DENYING THE ANTECEDENT (INVALID!):
   If A then B.
   A is false.
   Therefore B is false.  <- WRONG! B could still be true.

Example:
"If it rains, the ground is wet."
- It rained → Ground is wet (VALID)
- Ground is dry → It didn't rain (VALID)
- Ground is wet → It rained (INVALID - sprinkler could cause wet ground)
- It didn't rain → Ground is dry (INVALID - sprinkler could wet it)
"""

DEDUCTIVE_QUESTIONS = [
    {
        "premise": "If a person is a doctor, they have a medical degree.",
        "statement": "Sarah is a doctor.",
        "question": "What can we conclude?",
        "options": [
            "Sarah has a medical degree",
            "Sarah works in a hospital",
            "Sarah is wealthy",
            "Nothing can be concluded"
        ],
        "answer": "Sarah has a medical degree",
        "explanation": "If doctor → has medical degree. Sarah is doctor. Therefore Sarah has medical degree. (Modus Ponens)"
    },
    {
        "premise": "If a person is a doctor, they have a medical degree.",
        "statement": "Tom does not have a medical degree.",
        "question": "What can we conclude?",
        "options": [
            "Tom is not a doctor",
            "Tom is a nurse",
            "Tom failed medical school",
            "Nothing can be concluded"
        ],
        "answer": "Tom is not a doctor",
        "explanation": "If doctor → has medical degree. Tom doesn't have degree. Therefore Tom is not a doctor. (Modus Tollens)"
    },
    {
        "premise": "If a person is a doctor, they have a medical degree.",
        "statement": "Jane has a medical degree.",
        "question": "What can we conclude?",
        "options": [
            "Jane is a doctor",
            "Jane might be a doctor, but not necessarily",
            "Jane is definitely not a doctor",
            "Jane is a medical student"
        ],
        "answer": "Jane might be a doctor, but not necessarily",
        "explanation": "Having a degree doesn't mean you're a doctor (could be retired, changed careers). Affirming the consequent is invalid."
    },
    {
        "premise": "All managers attend the Monday meeting. All people who attend the Monday meeting receive the memo.",
        "statement": "David is a manager.",
        "question": "What can we conclude?",
        "options": [
            "David receives the memo",
            "David sends the memo",
            "David chairs the meeting",
            "Nothing can be concluded"
        ],
        "answer": "David receives the memo",
        "explanation": "Manager → attends meeting → receives memo. David is manager, so he receives memo."
    },
    {
        "premise": "If it is sunny, people go to the beach. If people go to the beach, ice cream sales increase.",
        "statement": "Ice cream sales have not increased.",
        "question": "What can we conclude?",
        "options": [
            "It is not sunny",
            "It is cloudy",
            "The beach is closed",
            "People don't like ice cream"
        ],
        "answer": "It is not sunny",
        "explanation": "Sunny → beach → ice cream sales. Sales didn't increase → no beach → not sunny. Chain of Modus Tollens."
    },
]


# ============================================
# SECTION 2: SYLLOGISMS
# ============================================

"""
SYLLOGISM PATTERNS:

VALID:
- All A are B. X is A. Therefore X is B.
- All A are B. No B are C. Therefore no A are C.
- Some A are B. All B are C. Therefore some A are C.

INVALID:
- All A are B. X is B. Therefore X is A.  (Not necessarily!)
- Some A are B. Therefore all A are B.  (Not necessarily!)

TRICK: Draw Venn diagrams to visualize the relationships.
"""

SYLLOGISM_QUESTIONS = [
    {
        "premises": [
            "All roses are flowers.",
            "All flowers need water."
        ],
        "question": "Which conclusion is valid?",
        "options": [
            "All roses need water",
            "All things that need water are roses",
            "Some flowers are roses",
            "Water is essential for life"
        ],
        "answer": "All roses need water",
        "explanation": "Roses ⊂ Flowers ⊂ Things that need water. So roses need water."
    },
    {
        "premises": [
            "All programmers use computers.",
            "John uses a computer."
        ],
        "question": "Which conclusion is valid?",
        "options": [
            "John is a programmer",
            "John might be a programmer",
            "John is not a programmer",
            "Computers are essential"
        ],
        "answer": "John might be a programmer",
        "explanation": "Many people use computers (not just programmers). We can't conclude John IS a programmer, only that he might be."
    },
    {
        "premises": [
            "No reptiles are mammals.",
            "All snakes are reptiles."
        ],
        "question": "Which conclusion is valid?",
        "options": [
            "No snakes are mammals",
            "Some snakes are mammals",
            "Mammals are warm-blooded",
            "Snakes are dangerous"
        ],
        "answer": "No snakes are mammals",
        "explanation": "Snakes ⊂ Reptiles. Reptiles ∩ Mammals = ∅. Therefore Snakes ∩ Mammals = ∅."
    },
    {
        "premises": [
            "Some athletes are wealthy.",
            "All wealthy people pay high taxes."
        ],
        "question": "Which conclusion is valid?",
        "options": [
            "All athletes pay high taxes",
            "Some athletes pay high taxes",
            "No athletes pay high taxes",
            "Taxes are unfair"
        ],
        "answer": "Some athletes pay high taxes",
        "explanation": "Some athletes are wealthy → those wealthy athletes pay high taxes. So SOME athletes pay high taxes."
    },
    {
        "premises": [
            "All birds have feathers.",
            "Penguins are birds."
        ],
        "question": "Which conclusion is valid?",
        "options": [
            "All birds can fly",
            "Penguins have feathers",
            "Penguins can swim",
            "Feathers are waterproof"
        ],
        "answer": "Penguins have feathers",
        "explanation": "Birds → have feathers. Penguins are birds. Therefore penguins have feathers."
    },
]


# ============================================
# SECTION 3: LOGICAL SEQUENCES & PATTERNS
# ============================================

"""
PATTERN TYPES:
1. Rotation patterns
2. Reflection patterns
3. Addition/removal of elements
4. Color/shading changes
5. Size changes

Since we're in text, we'll use text-based patterns.
"""

PATTERN_QUESTIONS = [
    {
        "pattern": "AB, CD, EF, GH, ?",
        "question": "What comes next?",
        "options": ["HI", "IJ", "JK", "GI"],
        "answer": "IJ",
        "explanation": "Each pair is consecutive letters: AB, CD, EF, GH, IJ"
    },
    {
        "pattern": "Z, Y, X, W, V, ?",
        "question": "What comes next?",
        "options": ["T", "U", "S", "R"],
        "answer": "U",
        "explanation": "Alphabet backwards: Z, Y, X, W, V, U"
    },
    {
        "pattern": "A1, B2, C3, D4, ?",
        "question": "What comes next?",
        "options": ["E5", "D5", "E4", "F5"],
        "answer": "E5",
        "explanation": "Letter advances by 1, number advances by 1: E5"
    },
    {
        "pattern": "MON, TUE, WED, THU, ?",
        "question": "What comes next?",
        "options": ["SAT", "FRI", "SUN", "WEK"],
        "answer": "FRI",
        "explanation": "Days of the week in order"
    },
    {
        "pattern": "J, F, M, A, M, J, ?",
        "question": "What comes next?",
        "options": ["J", "A", "S", "O"],
        "answer": "J",
        "explanation": "First letters of months: January, February, March, April, May, June, July"
    },
    {
        "pattern": "◯, ◯◯, ◯◯◯, ◯◯◯◯, ?",
        "question": "What comes next?",
        "options": ["◯◯◯◯", "◯◯◯◯◯", "◯◯◯", "◯◯◯◯◯◯"],
        "answer": "◯◯◯◯◯",
        "explanation": "Add one circle each step: 1, 2, 3, 4, 5"
    },
    {
        "pattern": "AZ, BY, CX, DW, ?",
        "question": "What comes next?",
        "options": ["EV", "EU", "EW", "FV"],
        "answer": "EV",
        "explanation": "First letter goes forward (A,B,C,D,E), second goes backward (Z,Y,X,W,V)"
    },
]


# ============================================
# SECTION 4: LOGICAL PUZZLES
# ============================================

PUZZLE_QUESTIONS = [
    {
        "puzzle": """
        Amy is taller than Beth.
        Beth is taller than Carol.
        Diana is shorter than Carol.
        """,
        "question": "Who is the shortest?",
        "options": ["Amy", "Beth", "Carol", "Diana"],
        "answer": "Diana",
        "explanation": "Order: Amy > Beth > Carol > Diana. Diana is shortest."
    },
    {
        "puzzle": """
        The red house is to the left of the blue house.
        The green house is to the right of the blue house.
        The yellow house is to the right of the green house.
        """,
        "question": "Which house is second from the left?",
        "options": ["Red", "Blue", "Green", "Yellow"],
        "answer": "Blue",
        "explanation": "Order: Red, Blue, Green, Yellow. Blue is second from left."
    },
    {
        "puzzle": """
        Five people are in a queue: A, B, C, D, E.
        A is not first or last.
        B is immediately after A.
        E is last.
        C is first.
        """,
        "question": "What position is D in?",
        "options": ["2nd", "3rd", "4th", "5th"],
        "answer": "4th",
        "explanation": "C is 1st, E is 5th. A is not 1st/5th and B follows A. So: C, A, B, D, E. D is 4th."
    },
    {
        "puzzle": """
        Either it's raining or the sprinkler is on.
        The sprinkler is not on.
        """,
        "question": "What can we conclude?",
        "options": [
            "It's raining",
            "It's not raining",
            "The ground is wet",
            "Nothing can be concluded"
        ],
        "answer": "It's raining",
        "explanation": "A OR B is true. B is false. Therefore A must be true."
    },
]


# ============================================
# PRACTICE RUNNER
# ============================================

def run_deductive_practice():
    """Practice deductive reasoning."""
    print("\n" + "=" * 60)
    print("DEDUCTIVE REASONING PRACTICE")
    print("=" * 60)

    score = 0
    questions = random.sample(DEDUCTIVE_QUESTIONS, min(4, len(DEDUCTIVE_QUESTIONS)))

    for i, q in enumerate(questions, 1):
        print(f"\n{'─' * 40}")
        print(f"Premise: {q['premise']}")
        print(f"Given: {q['statement']}")
        print(f"\nQ{i}: {q['question']}")
        for j, opt in enumerate(q['options'], 1):
            print(f"    {j}. {opt}")

        try:
            choice = input("Your answer (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                selected = q['options'][int(choice) - 1]
                if selected == q['answer']:
                    print("✓ Correct!")
                    score += 1
                else:
                    print(f"✗ Incorrect. Answer: {q['answer']}")
                    print(f"  {q['explanation']}")
            else:
                print(f"  Skipped. Answer: {q['answer']}")
        except:
            print(f"  Invalid. Answer: {q['answer']}")

    print(f"\nScore: {score}/{len(questions)}")
    return score


def run_syllogism_practice():
    """Practice syllogisms."""
    print("\n" + "=" * 60)
    print("SYLLOGISM PRACTICE")
    print("=" * 60)

    score = 0
    questions = random.sample(SYLLOGISM_QUESTIONS, min(4, len(SYLLOGISM_QUESTIONS)))

    for i, q in enumerate(questions, 1):
        print(f"\n{'─' * 40}")
        print("Premises:")
        for p in q['premises']:
            print(f"  • {p}")
        print(f"\nQ{i}: {q['question']}")
        for j, opt in enumerate(q['options'], 1):
            print(f"    {j}. {opt}")

        try:
            choice = input("Your answer (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                selected = q['options'][int(choice) - 1]
                if selected == q['answer']:
                    print("✓ Correct!")
                    score += 1
                else:
                    print(f"✗ Incorrect. Answer: {q['answer']}")
                    print(f"  {q['explanation']}")
            else:
                print(f"  Skipped. Answer: {q['answer']}")
        except:
            print(f"  Invalid. Answer: {q['answer']}")

    print(f"\nScore: {score}/{len(questions)}")
    return score


def run_pattern_practice():
    """Practice pattern recognition."""
    print("\n" + "=" * 60)
    print("PATTERN RECOGNITION PRACTICE")
    print("=" * 60)

    score = 0
    questions = random.sample(PATTERN_QUESTIONS, min(5, len(PATTERN_QUESTIONS)))

    for i, q in enumerate(questions, 1):
        print(f"\n{'─' * 40}")
        print(f"Pattern: {q['pattern']}")
        print(f"\nQ{i}: {q['question']}")
        for j, opt in enumerate(q['options'], 1):
            print(f"    {j}. {opt}")

        try:
            choice = input("Your answer (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                selected = q['options'][int(choice) - 1]
                if selected == q['answer']:
                    print("✓ Correct!")
                    score += 1
                else:
                    print(f"✗ Incorrect. Answer: {q['answer']}")
                    print(f"  {q['explanation']}")
            else:
                print(f"  Skipped. Answer: {q['answer']}")
        except:
            print(f"  Invalid. Answer: {q['answer']}")

    print(f"\nScore: {score}/{len(questions)}")
    return score


def run_puzzle_practice():
    """Practice logical puzzles."""
    print("\n" + "=" * 60)
    print("LOGICAL PUZZLE PRACTICE")
    print("=" * 60)

    score = 0
    for i, q in enumerate(PUZZLE_QUESTIONS, 1):
        print(f"\n{'─' * 40}")
        print(f"Puzzle:{q['puzzle']}")
        print(f"Q{i}: {q['question']}")
        for j, opt in enumerate(q['options'], 1):
            print(f"    {j}. {opt}")

        try:
            choice = input("Your answer (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                selected = q['options'][int(choice) - 1]
                if selected == q['answer']:
                    print("✓ Correct!")
                    score += 1
                else:
                    print(f"✗ Incorrect. Answer: {q['answer']}")
                    print(f"  {q['explanation']}")
            else:
                print(f"  Skipped. Answer: {q['answer']}")
        except:
            print(f"  Invalid. Answer: {q['answer']}")

    print(f"\nScore: {score}/{len(PUZZLE_QUESTIONS)}")
    return score


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("LOGICAL REASONING PRACTICE")
    print("=" * 60)
    print("""
Choose a section:
1. Deductive Reasoning (If-Then)
2. Syllogisms (All A are B...)
3. Pattern Recognition
4. Logical Puzzles
5. All sections
6. Just show me the tips
""")

    choice = input("Enter choice (1-6): ").strip()

    if choice == "1":
        run_deductive_practice()
    elif choice == "2":
        run_syllogism_practice()
    elif choice == "3":
        run_pattern_practice()
    elif choice == "4":
        run_puzzle_practice()
    elif choice == "5":
        total = 0
        total += run_deductive_practice()
        total += run_syllogism_practice()
        total += run_pattern_practice()
        total += run_puzzle_practice()
        print(f"\n{'=' * 60}")
        print(f"TOTAL SCORE: {total}")
    else:
        print("""
QUICK TIPS FOR LOGICAL REASONING:

1. IF-THEN STATEMENTS:
   - "If A then B" does NOT mean "If B then A"
   - Valid: A true → B true
   - Valid: B false → A false
   - INVALID: B true → A true

2. SYLLOGISMS:
   - Draw Venn diagrams
   - "All A are B" means A is inside B
   - "Some A are B" means A and B overlap
   - "No A are B" means A and B don't overlap

3. PATTERNS:
   - Look for: letters, numbers, shapes changing
   - Check: rotation, reflection, addition, removal
   - Test your answer by checking the pattern holds

4. PUZZLES:
   - Write down what you know
   - Draw diagrams for position problems
   - Process of elimination

5. COMMON TRAPS:
   - Adding assumptions not given
   - Confusing "some" with "all"
   - Reversing if-then statements
""")
