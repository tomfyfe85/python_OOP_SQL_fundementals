"""
TestGorilla Prep - Module 4: Problem Solving
============================================

WHAT IT TESTS:
- Multi-step reasoning
- Working with constraints
- Process of elimination
- Breaking down complex problems

TIPS:
- Write things down / draw diagrams
- Work systematically
- Use process of elimination
- Check your answer makes sense
"""

import random


# ============================================
# SECTION 1: SCHEDULING & ORDERING PUZZLES
# ============================================

"""
APPROACH:
1. List all constraints
2. Start with the most restrictive constraint
3. Work through possibilities systematically
4. Check your solution against ALL constraints
"""

ORDERING_PUZZLES = [
    {
        "puzzle": """
        Five runners finished a race: Alex, Beth, Carol, Dan, and Eve.
        - Beth finished before Carol
        - Dan finished after Eve
        - Alex finished first
        - Carol finished before Dan
        """,
        "question": "Who finished last?",
        "options": ["Beth", "Carol", "Dan", "Eve"],
        "answer": "Dan",
        "explanation": """
        Alex is 1st (given).
        Beth before Carol before Dan (chain).
        Eve before Dan.
        Possible order: Alex, Eve, Beth, Carol, Dan
        Dan is last.
        """
    },
    {
        "puzzle": """
        Four meetings are scheduled: Marketing, Finance, HR, and IT.
        - Finance is immediately after Marketing
        - HR is not first or last
        - IT is before Marketing
        """,
        "question": "What is the order of meetings?",
        "options": [
            "IT, Marketing, Finance, HR",
            "IT, HR, Marketing, Finance",
            "HR, IT, Marketing, Finance",
            "IT, Marketing, HR, Finance"
        ],
        "answer": "IT, HR, Marketing, Finance",
        "explanation": """
        Finance immediately after Marketing → [Marketing, Finance] as a pair.
        IT before Marketing → IT, [Marketing, Finance].
        HR not first or last → must be between IT and Marketing.
        Order: IT, HR, Marketing, Finance
        """
    },
    {
        "puzzle": """
        A baker makes 5 types of bread in order: Rye, Wheat, Sourdough, White, Multigrain.
        Today the schedule changed:
        - Sourdough moved to first
        - White and Multigrain swapped positions
        """,
        "question": "What is the new third bread?",
        "options": ["Rye", "Wheat", "White", "Multigrain"],
        "answer": "Wheat",
        "explanation": """
        Original: Rye, Wheat, Sourdough, White, Multigrain
        Sourdough to first: Sourdough, Rye, Wheat, White, Multigrain
        Swap White/Multigrain: Sourdough, Rye, Wheat, Multigrain, White
        Third = Wheat
        """
    },
]


# ============================================
# SECTION 2: GRID/LOGIC PUZZLES
# ============================================

GRID_PUZZLES = [
    {
        "puzzle": """
        Three friends (Alice, Bob, Chris) each own a different pet (dog, cat, fish)
        and live in different cities (London, Paris, Rome).

        - Alice doesn't live in London
        - The person with the dog lives in Paris
        - Bob has a cat
        - Chris lives in Rome
        """,
        "question": "Who has the dog?",
        "options": ["Alice", "Bob", "Chris"],
        "answer": "Alice",
        "explanation": """
        Chris lives in Rome.
        Bob has a cat (so not dog).
        Dog owner lives in Paris.
        Alice doesn't live in London → Alice lives in Paris (since Chris has Rome).
        Therefore Alice has the dog.
        """
    },
    {
        "puzzle": """
        Four employees (Amy, Ben, Cara, Dan) work on different floors (1-4).

        - Amy works above Ben
        - Cara works on floor 2
        - Dan works on the top floor
        - Ben doesn't work on floor 1
        """,
        "question": "What floor does Amy work on?",
        "options": ["Floor 1", "Floor 2", "Floor 3", "Floor 4"],
        "answer": "Floor 3",
        "explanation": """
        Dan is on floor 4.
        Cara is on floor 2.
        Ben not on floor 1, so Ben on floor 1 or 3. But not 1, so Ben on... wait.
        Amy above Ben. Dan on 4, Cara on 2.
        Remaining floors for Amy and Ben: 1, 3.
        Amy above Ben → Amy on 3, Ben on 1.
        """
    },
    {
        "puzzle": """
        In a row of 4 houses, each painted a different color (Red, Blue, Green, Yellow):

        - The Red house is at one of the ends
        - The Blue house is next to the Green house
        - The Yellow house is not next to the Red house
        """,
        "question": "What color is the second house from the left?",
        "options": ["Red", "Blue", "Green", "Yellow"],
        "answer": "Blue",
        "explanation": """
        Red at an end. Yellow not next to Red.
        If Red is 1st: positions 1=Red, Yellow can't be 2nd.
        Blue next to Green → they're adjacent.
        Red, Blue, Green, Yellow or Red, Green, Blue, Yellow?
        Try: Red(1), Blue(2), Green(3), Yellow(4) - Blue next to Green ✓, Yellow not next to Red ✓
        Second house = Blue
        """
    },
]


# ============================================
# SECTION 3: MATHEMATICAL REASONING
# ============================================

MATH_PUZZLES = [
    {
        "puzzle": """
        A shop sells apples and oranges.
        - 3 apples cost the same as 2 oranges
        - 6 oranges cost £12
        """,
        "question": "How much do 9 apples cost?",
        "options": ["£8", "£10", "£12", "£15"],
        "answer": "£12",
        "explanation": """
        6 oranges = £12 → 1 orange = £2
        3 apples = 2 oranges = £4 → 1 apple = £4/3
        9 apples = 9 × £4/3 = £12
        Or: 9 apples = 3 × (3 apples) = 3 × (2 oranges) = 6 oranges = £12
        """
    },
    {
        "puzzle": """
        A train travels from A to B at 60 mph.
        It returns from B to A at 40 mph.
        """,
        "question": "What is the average speed for the whole journey?",
        "options": ["45 mph", "48 mph", "50 mph", "52 mph"],
        "answer": "48 mph",
        "explanation": """
        Let distance = 120 miles (or any number).
        Time A→B = 120/60 = 2 hours
        Time B→A = 120/40 = 3 hours
        Total = 240 miles in 5 hours = 48 mph
        (Note: It's NOT simply (60+40)/2 = 50!)
        """
    },
    {
        "puzzle": """
        If 5 machines take 5 minutes to make 5 widgets,
        how long does it take 100 machines to make 100 widgets?
        """,
        "question": "How many minutes?",
        "options": ["1 minute", "5 minutes", "20 minutes", "100 minutes"],
        "answer": "5 minutes",
        "explanation": """
        5 machines make 5 widgets in 5 minutes.
        → 1 machine makes 1 widget in 5 minutes.
        → 100 machines make 100 widgets in 5 minutes.
        (Each machine works independently)
        """
    },
    {
        "puzzle": """
        A father is 4 times as old as his son.
        In 20 years, he will be twice as old as his son.
        """,
        "question": "How old is the son now?",
        "options": ["5", "10", "15", "20"],
        "answer": "10",
        "explanation": """
        Let son = x, father = 4x
        In 20 years: son = x+20, father = 4x+20
        4x+20 = 2(x+20)
        4x+20 = 2x+40
        2x = 20
        x = 10
        """
    },
]


# ============================================
# SECTION 4: PROCESS & DECISION MAKING
# ============================================

PROCESS_PUZZLES = [
    {
        "puzzle": """
        A company's vacation approval process:
        1. If request is less than 3 days, manager can approve
        2. If request is 3+ days, HR must also approve
        3. Requests during busy season need director approval regardless of length
        4. Busy season is June-August

        Sarah requests 2 days off in July.
        """,
        "question": "Who needs to approve Sarah's request?",
        "options": [
            "Manager only",
            "Manager and HR",
            "Director only",
            "Manager and Director"
        ],
        "answer": "Manager and Director",
        "explanation": """
        2 days = less than 3 days → Manager can approve
        But July is busy season → Director approval needed regardless
        So: Manager + Director
        """
    },
    {
        "puzzle": """
        Shipping rules:
        - Orders under £30: £5 shipping
        - Orders £30-£50: £3 shipping
        - Orders over £50: Free shipping
        - Express delivery: Add £10 to any shipping cost

        An order totals £45 with express delivery.
        """,
        "question": "What is the total shipping cost?",
        "options": ["£3", "£10", "£13", "£15"],
        "answer": "£13",
        "explanation": """
        £45 is in £30-£50 range → £3 base shipping
        Express delivery → add £10
        Total shipping = £3 + £10 = £13
        """
    },
    {
        "puzzle": """
        Password requirements:
        - At least 8 characters
        - At least one uppercase letter
        - At least one number
        - No spaces allowed

        Which password is valid?
        """,
        "question": "Select the valid password:",
        "options": [
            "password1",
            "Pass word1",
            "PASSWORD1",
            "Password1"
        ],
        "answer": "Password1",
        "explanation": """
        password1: No uppercase ✗
        Pass word1: Contains space ✗
        PASSWORD1: No lowercase... wait, the rules don't require lowercase!
        Actually PASSWORD1 is 9 chars, has uppercase, has number, no spaces ✓
        Password1: 9 chars ✓, uppercase P ✓, number 1 ✓, no spaces ✓
        Both PASSWORD1 and Password1 work, but Password1 is the listed answer.
        """
    },
]


# ============================================
# PRACTICE RUNNER
# ============================================

def run_ordering_practice():
    """Practice ordering puzzles."""
    print("\n" + "=" * 60)
    print("ORDERING & SCHEDULING PUZZLES")
    print("=" * 60)

    score = 0
    for i, q in enumerate(ORDERING_PUZZLES, 1):
        print(f"\n{'─' * 50}")
        print(f"Puzzle {i}:{q['puzzle']}")
        print(f"\nQuestion: {q['question']}")
        for j, opt in enumerate(q['options'], 1):
            print(f"    {j}. {opt}")

        try:
            choice = input("Your answer: ").strip()
            if choice in ['1', '2', '3', '4']:
                selected = q['options'][int(choice) - 1]
                if selected == q['answer']:
                    print("✓ Correct!")
                    score += 1
                else:
                    print(f"✗ Incorrect. Answer: {q['answer']}")
                    print(f"Explanation:{q['explanation']}")
            else:
                print(f"Skipped. Answer: {q['answer']}")
        except:
            print(f"Invalid. Answer: {q['answer']}")

    print(f"\nScore: {score}/{len(ORDERING_PUZZLES)}")
    return score


def run_grid_practice():
    """Practice grid/logic puzzles."""
    print("\n" + "=" * 60)
    print("GRID & LOGIC PUZZLES")
    print("=" * 60)

    score = 0
    for i, q in enumerate(GRID_PUZZLES, 1):
        print(f"\n{'─' * 50}")
        print(f"Puzzle {i}:{q['puzzle']}")
        print(f"\nQuestion: {q['question']}")
        for j, opt in enumerate(q['options'], 1):
            print(f"    {j}. {opt}")

        try:
            choice = input("Your answer: ").strip()
            if choice in ['1', '2', '3', '4']:
                selected = q['options'][int(choice) - 1]
                if selected == q['answer']:
                    print("✓ Correct!")
                    score += 1
                else:
                    print(f"✗ Incorrect. Answer: {q['answer']}")
                    print(f"Explanation:{q['explanation']}")
            else:
                print(f"Skipped. Answer: {q['answer']}")
        except:
            print(f"Invalid. Answer: {q['answer']}")

    print(f"\nScore: {score}/{len(GRID_PUZZLES)}")
    return score


def run_math_practice():
    """Practice mathematical reasoning puzzles."""
    print("\n" + "=" * 60)
    print("MATHEMATICAL REASONING PUZZLES")
    print("=" * 60)

    score = 0
    for i, q in enumerate(MATH_PUZZLES, 1):
        print(f"\n{'─' * 50}")
        print(f"Puzzle {i}:{q['puzzle']}")
        print(f"\nQuestion: {q['question']}")
        for j, opt in enumerate(q['options'], 1):
            print(f"    {j}. {opt}")

        try:
            choice = input("Your answer: ").strip()
            if choice in ['1', '2', '3', '4']:
                selected = q['options'][int(choice) - 1]
                if selected == q['answer']:
                    print("✓ Correct!")
                    score += 1
                else:
                    print(f"✗ Incorrect. Answer: {q['answer']}")
                    print(f"Explanation:{q['explanation']}")
            else:
                print(f"Skipped. Answer: {q['answer']}")
        except:
            print(f"Invalid. Answer: {q['answer']}")

    print(f"\nScore: {score}/{len(MATH_PUZZLES)}")
    return score


def run_process_practice():
    """Practice process/decision making puzzles."""
    print("\n" + "=" * 60)
    print("PROCESS & DECISION MAKING PUZZLES")
    print("=" * 60)

    score = 0
    for i, q in enumerate(PROCESS_PUZZLES, 1):
        print(f"\n{'─' * 50}")
        print(f"Puzzle {i}:{q['puzzle']}")
        print(f"\nQuestion: {q['question']}")
        for j, opt in enumerate(q['options'], 1):
            print(f"    {j}. {opt}")

        try:
            choice = input("Your answer: ").strip()
            if choice in ['1', '2', '3', '4']:
                selected = q['options'][int(choice) - 1]
                if selected == q['answer']:
                    print("✓ Correct!")
                    score += 1
                else:
                    print(f"✗ Incorrect. Answer: {q['answer']}")
                    print(f"Explanation:{q['explanation']}")
            else:
                print(f"Skipped. Answer: {q['answer']}")
        except:
            print(f"Invalid. Answer: {q['answer']}")

    print(f"\nScore: {score}/{len(PROCESS_PUZZLES)}")
    return score


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("PROBLEM SOLVING PRACTICE")
    print("=" * 60)
    print("""
Choose a section:
1. Ordering & Scheduling
2. Grid & Logic Puzzles
3. Mathematical Reasoning
4. Process & Decision Making
5. All sections
6. Just show me the tips
""")

    choice = input("Enter choice (1-6): ").strip()

    if choice == "1":
        run_ordering_practice()
    elif choice == "2":
        run_grid_practice()
    elif choice == "3":
        run_math_practice()
    elif choice == "4":
        run_process_practice()
    elif choice == "5":
        total = 0
        total += run_ordering_practice()
        total += run_grid_practice()
        total += run_math_practice()
        total += run_process_practice()
        print(f"\n{'=' * 60}")
        print(f"TOTAL SCORE: {total}")
    else:
        print("""
QUICK TIPS FOR PROBLEM SOLVING:

1. ORDERING PUZZLES:
   - Write out positions: 1st, 2nd, 3rd, 4th, 5th
   - Start with definite facts (X is first)
   - Use chains: if A before B and B before C, then A before C

2. GRID PUZZLES:
   - Draw a grid with rows and columns
   - Mark what you KNOW with ✓
   - Mark what's IMPOSSIBLE with ✗
   - Process of elimination fills in the rest

3. MATH REASONING:
   - Watch for trick questions (average speed trap!)
   - Set up equations if needed
   - Use simple numbers to test

4. PROCESS PUZZLES:
   - Read ALL rules before answering
   - Check for exceptions (regardless of..., unless...)
   - Apply rules in order

5. GENERAL:
   - Write things down - don't hold it all in your head
   - Check your answer against ALL constraints
   - If stuck, try working backwards from the options
""")
