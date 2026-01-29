"""
TestGorilla Prep - Module 1: Numerical Reasoning
=================================================

WHAT IT TESTS:
- Number sequences and patterns
- Percentages, ratios, proportions
- Basic arithmetic under time pressure
- Data interpretation from tables/charts

TIPS:
- Don't overthink - patterns are usually simple
- Check all answer options - sometimes you can eliminate
- Round numbers for quick estimation
- Practice mental math shortcuts

TIME: Usually 10-15 seconds per question
"""

import random


# ============================================
# SECTION 1: NUMBER SEQUENCES
# ============================================

"""
PATTERN TYPES TO RECOGNIZE:

1. ARITHMETIC: Add/subtract same number each time
   2, 5, 8, 11, 14, ? -> +3 each time -> 17

2. GEOMETRIC: Multiply/divide by same number
   3, 6, 12, 24, ? -> ×2 each time -> 48

3. ALTERNATING: Two patterns interleaved
   1, 10, 2, 20, 3, 30, ? -> (1,2,3...) and (10,20,30...)

4. FIBONACCI-LIKE: Add previous two numbers
   1, 1, 2, 3, 5, 8, ? -> 5+8 = 13

5. SQUARED/CUBED: Perfect squares or cubes
   1, 4, 9, 16, 25, ? -> 1², 2², 3², 4², 5², 6² = 36

6. INCREASING DIFFERENCES: +1, +2, +3, +4...
   2, 3, 5, 8, 12, ? -> +1, +2, +3, +4, +5 = 17
"""

SEQUENCE_QUESTIONS = [
    {
        "sequence": [2, 4, 6, 8, 10],
        "options": ["11", "12", "14", "10"],
        "answer": "12",
        "explanation": "Arithmetic sequence: +2 each time. 10 + 2 = 12"
    },
    {
        "sequence": [3, 6, 12, 24, 48],
        "options": ["72", "96", "60", "84"],
        "answer": "96",
        "explanation": "Geometric sequence: ×2 each time. 48 × 2 = 96"
    },
    {
        "sequence": [1, 4, 9, 16, 25],
        "options": ["30", "36", "49", "32"],
        "answer": "36",
        "explanation": "Perfect squares: 1², 2², 3², 4², 5², 6² = 36"
    },
    {
        "sequence": [1, 1, 2, 3, 5, 8],
        "options": ["11", "13", "10", "15"],
        "answer": "13",
        "explanation": "Fibonacci: each number = sum of previous two. 5 + 8 = 13"
    },
    {
        "sequence": [2, 3, 5, 8, 12, 17],
        "options": ["22", "23", "24", "21"],
        "answer": "23",
        "explanation": "Increasing differences: +1, +2, +3, +4, +5, +6. 17 + 6 = 23"
    },
    {
        "sequence": [100, 95, 90, 85, 80],
        "options": ["70", "75", "76", "74"],
        "answer": "75",
        "explanation": "Arithmetic: -5 each time. 80 - 5 = 75"
    },
    {
        "sequence": [1, 2, 4, 7, 11, 16],
        "options": ["21", "22", "23", "24"],
        "answer": "22",
        "explanation": "Differences increase by 1: +1, +2, +3, +4, +5, +6. 16 + 6 = 22"
    },
    {
        "sequence": [81, 27, 9, 3],
        "options": ["1", "0", "2", "-1"],
        "answer": "1",
        "explanation": "Geometric: ÷3 each time. 3 ÷ 3 = 1"
    },
    {
        "sequence": [2, 6, 18, 54],
        "options": ["108", "162", "148", "180"],
        "answer": "162",
        "explanation": "Geometric: ×3 each time. 54 × 3 = 162"
    },
    {
        "sequence": [1, 8, 27, 64, 125],
        "options": ["196", "216", "225", "250"],
        "answer": "216",
        "explanation": "Perfect cubes: 1³, 2³, 3³, 4³, 5³, 6³ = 216"
    },
]


# ============================================
# SECTION 2: PERCENTAGES & RATIOS
# ============================================

"""
QUICK MENTAL MATH TRICKS:

10% of X = X ÷ 10
5% of X = half of 10%
1% of X = X ÷ 100
25% of X = X ÷ 4
50% of X = X ÷ 2
20% of X = X ÷ 5

To find X% of Y: (X × Y) ÷ 100

PERCENTAGE INCREASE/DECREASE:
New = Original × (1 + rate) for increase
New = Original × (1 - rate) for decrease

Example: 20% increase on 50 = 50 × 1.2 = 60
"""

PERCENTAGE_QUESTIONS = [
    {
        "question": "What is 15% of 200?",
        "options": ["25", "30", "35", "40"],
        "answer": "30",
        "explanation": "10% of 200 = 20, 5% of 200 = 10, so 15% = 20 + 10 = 30"
    },
    {
        "question": "A shirt costs £40 and is reduced by 25%. What is the new price?",
        "options": ["£30", "£35", "£28", "£32"],
        "answer": "£30",
        "explanation": "25% of 40 = 10. New price = 40 - 10 = £30"
    },
    {
        "question": "If 60 is increased by 20%, what is the result?",
        "options": ["70", "72", "75", "80"],
        "answer": "72",
        "explanation": "20% of 60 = 12. Result = 60 + 12 = 72. Or: 60 × 1.2 = 72"
    },
    {
        "question": "A team has 12 women and 8 men. What percentage are women?",
        "options": ["50%", "55%", "60%", "65%"],
        "answer": "60%",
        "explanation": "Total = 20. Women = 12. Percentage = 12/20 = 0.6 = 60%"
    },
    {
        "question": "If the ratio of cats to dogs is 3:2 and there are 15 cats, how many dogs?",
        "options": ["8", "9", "10", "12"],
        "answer": "10",
        "explanation": "3 parts = 15, so 1 part = 5. Dogs = 2 parts = 10"
    },
    {
        "question": "What is 200 as a percentage of 800?",
        "options": ["20%", "25%", "30%", "40%"],
        "answer": "25%",
        "explanation": "200 ÷ 800 = 0.25 = 25%"
    },
    {
        "question": "A price increased from £80 to £100. What was the percentage increase?",
        "options": ["20%", "25%", "15%", "30%"],
        "answer": "25%",
        "explanation": "Increase = 20. Percentage = 20/80 = 0.25 = 25%"
    },
    {
        "question": "If 3/5 of a class passed, what percentage failed?",
        "options": ["30%", "35%", "40%", "45%"],
        "answer": "40%",
        "explanation": "Passed = 3/5 = 60%. Failed = 100% - 60% = 40%"
    },
]


# ============================================
# SECTION 3: DATA INTERPRETATION
# ============================================

"""
APPROACH FOR DATA QUESTIONS:
1. Read the question carefully - what exactly is being asked?
2. Find the relevant data
3. Do the calculation
4. Check units match the answer options
"""

DATA_QUESTIONS = [
    {
        "context": """
        Monthly Sales (in £1000s):
        Jan: 45, Feb: 52, Mar: 48, Apr: 61, May: 55
        """,
        "question": "What was the total sales for the first quarter (Jan-Mar)?",
        "options": ["£145,000", "£150,000", "£156,000", "£165,000"],
        "answer": "£145,000",
        "explanation": "First quarter = Jan + Feb + Mar = 45 + 52 + 48 = 145 (in £1000s) = £145,000"
    },
    {
        "context": """
        Monthly Sales (in £1000s):
        Jan: 45, Feb: 52, Mar: 48, Apr: 61, May: 55
        """,
        "question": "What was the average monthly sales?",
        "options": ["£50,200", "£52,000", "£52,200", "£54,000"],
        "answer": "£52,200",
        "explanation": "Total = 45+52+48+61+55 = 261. Average = 261/5 = 52.2 (in £1000s) = £52,200"
    },
    {
        "context": """
        Employee Distribution:
        Engineering: 120
        Sales: 80
        Marketing: 45
        HR: 15
        Total: 260
        """,
        "question": "What percentage of employees work in Engineering?",
        "options": ["40%", "42%", "46%", "48%"],
        "answer": "46%",
        "explanation": "120/260 ≈ 0.46 = 46%"
    },
    {
        "context": """
        Project Budget Allocation:
        Development: 40%
        Testing: 25%
        Management: 20%
        Other: 15%
        Total Budget: £500,000
        """,
        "question": "How much is allocated to Testing?",
        "options": ["£100,000", "£125,000", "£150,000", "£175,000"],
        "answer": "£125,000",
        "explanation": "25% of £500,000 = £500,000 × 0.25 = £125,000"
    },
]


# ============================================
# PRACTICE RUNNER
# ============================================

def run_sequence_practice():
    """Practice number sequences."""
    print("\n" + "=" * 60)
    print("NUMBER SEQUENCE PRACTICE")
    print("=" * 60)
    print("Find the next number in each sequence.\n")

    score = 0
    questions = random.sample(SEQUENCE_QUESTIONS, min(5, len(SEQUENCE_QUESTIONS)))

    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['sequence']} -> ?")
        for j, opt in enumerate(q['options'], 1):
            print(f"    {j}. {opt}")

        try:
            choice = input("Your answer (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                selected = q['options'][int(choice) - 1]
                if selected == q['answer']:
                    print("✓ Correct!\n")
                    score += 1
                else:
                    print(f"✗ Incorrect. Answer: {q['answer']}")
                    print(f"  {q['explanation']}\n")
            else:
                print(f"  Skipped. Answer: {q['answer']}")
                print(f"  {q['explanation']}\n")
        except (ValueError, IndexError):
            print(f"  Invalid input. Answer: {q['answer']}\n")

    print(f"\nScore: {score}/{len(questions)}")
    return score


def run_percentage_practice():
    """Practice percentages and ratios."""
    print("\n" + "=" * 60)
    print("PERCENTAGES & RATIOS PRACTICE")
    print("=" * 60)
    print("Answer each question.\n")

    score = 0
    questions = random.sample(PERCENTAGE_QUESTIONS, min(5, len(PERCENTAGE_QUESTIONS)))

    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['question']}")
        for j, opt in enumerate(q['options'], 1):
            print(f"    {j}. {opt}")

        try:
            choice = input("Your answer (1-4): ").strip()
            if choice in ['1', '2', '3', '4']:
                selected = q['options'][int(choice) - 1]
                if selected == q['answer']:
                    print("✓ Correct!\n")
                    score += 1
                else:
                    print(f"✗ Incorrect. Answer: {q['answer']}")
                    print(f"  {q['explanation']}\n")
            else:
                print(f"  Skipped. Answer: {q['answer']}")
                print(f"  {q['explanation']}\n")
        except (ValueError, IndexError):
            print(f"  Invalid input. Answer: {q['answer']}\n")

    print(f"\nScore: {score}/{len(questions)}")
    return score


def run_data_practice():
    """Practice data interpretation."""
    print("\n" + "=" * 60)
    print("DATA INTERPRETATION PRACTICE")
    print("=" * 60)

    score = 0
    for i, q in enumerate(DATA_QUESTIONS, 1):
        print(f"\n{'─' * 40}")
        print(f"Context:{q['context']}")
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
                print(f"  {q['explanation']}")
        except (ValueError, IndexError):
            print(f"  Invalid input. Answer: {q['answer']}")

    print(f"\nScore: {score}/{len(DATA_QUESTIONS)}")
    return score


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("NUMERICAL REASONING PRACTICE")
    print("=" * 60)
    print("""
Choose a section to practice:
1. Number Sequences
2. Percentages & Ratios
3. Data Interpretation
4. All sections
5. Just show me the tips (no practice)
""")

    choice = input("Enter choice (1-5): ").strip()

    if choice == "1":
        run_sequence_practice()
    elif choice == "2":
        run_percentage_practice()
    elif choice == "3":
        run_data_practice()
    elif choice == "4":
        total = 0
        total += run_sequence_practice()
        total += run_percentage_practice()
        total += run_data_practice()
        print(f"\n{'=' * 60}")
        print(f"TOTAL SCORE: {total}")
    else:
        print("""
QUICK TIPS FOR NUMERICAL REASONING:

1. SEQUENCES: Look for +, -, ×, ÷ patterns first
   - Check differences between consecutive numbers
   - Check if numbers are squares, cubes, or primes

2. PERCENTAGES: Use easy benchmarks
   - 10% = divide by 10
   - 50% = divide by 2
   - 25% = divide by 4
   - Build other percentages from these

3. RATIOS: Find the value of "1 part"
   - If 3:2 ratio and first is 15, then 1 part = 15/3 = 5

4. DATA: Read the question twice
   - What units are being used?
   - Is it asking for total, average, or percentage?

5. TIME MANAGEMENT: 10-15 seconds per question
   - Don't get stuck - guess and move on
   - Easier questions are worth the same as hard ones
""")
