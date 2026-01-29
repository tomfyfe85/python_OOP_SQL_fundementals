"""
TestGorilla Prep - Module 5: Attention to Detail
=================================================

WHAT IT TESTS:
- Spotting differences
- Matching information accurately
- Data comparison and verification
- Error detection

TIPS:
- Work systematically (left to right, top to bottom)
- Check character by character for codes/numbers
- Don't rush - accuracy over speed
- Use your finger or cursor to track position
"""

import random


# ============================================
# SECTION 1: SPOT THE DIFFERENCE
# ============================================

SPOT_DIFFERENCE_QUESTIONS = [
    {
        "original": "ABC123XYZ",
        "compare":  "ABC123XVZ",
        "question": "Are these two codes identical?",
        "answer": "No",
        "difference": "Position 7: Y vs V"
    },
    {
        "original": "john.smith@company.com",
        "compare":  "john.smith@company.com",
        "question": "Are these two email addresses identical?",
        "answer": "Yes",
        "difference": "No difference"
    },
    {
        "original": "Invoice #INV-2024-00847",
        "compare":  "Invoice #INV-2024-00847",
        "question": "Are these two invoice numbers identical?",
        "answer": "Yes",
        "difference": "No difference"
    },
    {
        "original": "Tel: +44 7700 900123",
        "compare":  "Tel: +44 7700 900132",
        "question": "Are these two phone numbers identical?",
        "answer": "No",
        "difference": "Last digits: 123 vs 132"
    },
    {
        "original": "www.example-site.co.uk",
        "compare":  "www.example_site.co.uk",
        "question": "Are these two URLs identical?",
        "answer": "No",
        "difference": "Hyphen (-) vs Underscore (_)"
    },
    {
        "original": "Reference: RF/2024/MAR/0042",
        "compare":  "Reference: RF/2024/MAR/0042",
        "question": "Are these two references identical?",
        "answer": "Yes",
        "difference": "No difference"
    },
    {
        "original": "ProductID: SKU-8847-BLU-L",
        "compare":  "ProductID: SKU-8847-BLU-1",
        "question": "Are these two product IDs identical?",
        "answer": "No",
        "difference": "L (letter) vs 1 (number) at end"
    },
    {
        "original": "Amount: £1,234.56",
        "compare":  "Amount: £1,234.65",
        "question": "Are these two amounts identical?",
        "answer": "No",
        "difference": "Pence: 56 vs 65"
    },
]


# ============================================
# SECTION 2: DATA MATCHING
# ============================================

DATA_MATCHING_QUESTIONS = [
    {
        "context": """
        Employee Record:
        Name: Sarah J. Thompson
        Employee ID: EMP-004521
        Department: Marketing
        Start Date: 15/03/2021
        """,
        "statement": "Employee ID: EMP-004521, Department: Marketing, Start: 15/03/2021",
        "question": "Does this statement match the record?",
        "answer": "Yes",
        "explanation": "All details match the record."
    },
    {
        "context": """
        Order Details:
        Order #: ORD-99821
        Customer: James Wilson
        Total: £459.99
        Shipping: Express
        """,
        "statement": "Order ORD-99821 for James Wilson, Total £459.00, Express shipping",
        "question": "Does this statement match the record?",
        "answer": "No",
        "explanation": "Total is £459.99, not £459.00"
    },
    {
        "context": """
        Meeting Schedule:
        Date: Tuesday, 14th November
        Time: 2:30 PM - 4:00 PM
        Room: Conference Room B
        Attendees: 8
        """,
        "statement": "Meeting on Tuesday 14th November, 2:30-4:00 PM in Conference Room B",
        "question": "Does this statement match the record?",
        "answer": "Yes",
        "explanation": "All details match (attendee count wasn't mentioned in statement, but what was stated is correct)."
    },
    {
        "context": """
        Product Information:
        Name: Wireless Headphones Pro
        Price: £129.99
        Color: Midnight Black
        Stock: 47 units
        """,
        "statement": "Wireless Headphones Pro in Midnight Blue, £129.99, 47 in stock",
        "question": "Does this statement match the record?",
        "answer": "No",
        "explanation": "Color is Midnight Black, not Midnight Blue"
    },
]


# ============================================
# SECTION 3: ERROR DETECTION
# ============================================

ERROR_DETECTION_QUESTIONS = [
    {
        "text": """
        Thank you for your order. Your items will be shiped within
        3-5 business days. Please contact us if you have any questions.
        """,
        "question": "Is there a spelling error?",
        "options": ["No errors", "Yes - 'shiped' should be 'shipped'", "Yes - 'business' is wrong", "Yes - 'contact' is wrong"],
        "answer": "Yes - 'shiped' should be 'shipped'",
        "explanation": "The word 'shipped' is misspelled as 'shiped' (missing a 'p')."
    },
    {
        "text": """
        The meeting has been rescheduled to Wenesday at 3 PM.
        Please confirm your attendance by end of day.
        """,
        "question": "Is there a spelling error?",
        "options": ["No errors", "Yes - 'rescheduled' is wrong", "Yes - 'Wenesday' should be 'Wednesday'", "Yes - 'attendance' is wrong"],
        "answer": "Yes - 'Wenesday' should be 'Wednesday'",
        "explanation": "Wednesday is misspelled as 'Wenesday' (missing 'd')."
    },
    {
        "text": """
        Our new office is located at 42 High Street, London.
        The building is accessible by public transport.
        """,
        "question": "Is there a spelling error?",
        "options": ["No errors", "Yes - 'located' is wrong", "Yes - 'accessible' is wrong", "Yes - 'transport' is wrong"],
        "answer": "No errors",
        "explanation": "All words are spelled correctly."
    },
    {
        "text": """
        Please ensure all documents are submited before the deadline.
        Late submissions will not be accepted.
        """,
        "question": "Is there a spelling error?",
        "options": ["No errors", "Yes - 'submited' should be 'submitted'", "Yes - 'deadline' is wrong", "Yes - 'accepted' is wrong"],
        "answer": "Yes - 'submited' should be 'submitted'",
        "explanation": "The word 'submitted' is misspelled as 'submited' (missing a 't')."
    },
]


# ============================================
# SECTION 4: NUMBER VERIFICATION
# ============================================

NUMBER_VERIFICATION_QUESTIONS = [
    {
        "data": """
        Budget Report Q3:
        Marketing: £45,200
        Sales: £62,800
        Operations: £38,500
        IT: £29,400
        """,
        "question": "What is the total budget?",
        "options": ["£175,900", "£176,900", "£175,800", "£174,900"],
        "answer": "£175,900",
        "explanation": "45,200 + 62,800 + 38,500 + 29,400 = 175,900"
    },
    {
        "data": """
        Inventory Count:
        Warehouse A: 1,245 units
        Warehouse B: 892 units
        Warehouse C: 1,103 units
        """,
        "question": "What is the total inventory?",
        "options": ["3,140 units", "3,240 units", "3,340 units", "3,040 units"],
        "answer": "3,240 units",
        "explanation": "1,245 + 892 + 1,103 = 3,240"
    },
    {
        "data": """
        Sales Team Performance:
        Alice: 47 sales
        Bob: 52 sales
        Carol: 38 sales
        Dan: 61 sales
        """,
        "question": "Who had the highest sales?",
        "options": ["Alice", "Bob", "Carol", "Dan"],
        "answer": "Dan",
        "explanation": "Dan has 61 sales, the highest among all."
    },
    {
        "data": """
        Monthly Expenses:
        Rent: £2,400
        Utilities: £340
        Insurance: £180
        Supplies: £275
        """,
        "question": "Which expense is the second highest?",
        "options": ["Rent", "Utilities", "Insurance", "Supplies"],
        "answer": "Utilities",
        "explanation": "Rank: Rent (2,400), Utilities (340), Supplies (275), Insurance (180)"
    },
]


# ============================================
# PRACTICE RUNNER
# ============================================

def run_spot_difference_practice():
    """Practice spotting differences."""
    print("\n" + "=" * 60)
    print("SPOT THE DIFFERENCE PRACTICE")
    print("=" * 60)
    print("Compare the two items carefully.\n")

    score = 0
    questions = random.sample(SPOT_DIFFERENCE_QUESTIONS, min(5, len(SPOT_DIFFERENCE_QUESTIONS)))

    for i, q in enumerate(questions, 1):
        print(f"\n{'─' * 50}")
        print(f"Q{i}:")
        print(f"Original: {q['original']}")
        print(f"Compare:  {q['compare']}")
        print(f"\n{q['question']}")
        print("    1. Yes (identical)")
        print("    2. No (different)")

        try:
            choice = input("Your answer (1-2): ").strip()
            answers = {"1": "Yes", "2": "No"}
            if choice in answers:
                selected = answers[choice]
                if selected == q['answer']:
                    print("✓ Correct!")
                    score += 1
                else:
                    print(f"✗ Incorrect. Answer: {q['answer']}")
                    print(f"  Difference: {q['difference']}")
            else:
                print(f"  Skipped. Answer: {q['answer']}")
        except:
            print(f"  Invalid. Answer: {q['answer']}")

    print(f"\nScore: {score}/{len(questions)}")
    return score


def run_data_matching_practice():
    """Practice data matching."""
    print("\n" + "=" * 60)
    print("DATA MATCHING PRACTICE")
    print("=" * 60)

    score = 0
    for i, q in enumerate(DATA_MATCHING_QUESTIONS, 1):
        print(f"\n{'─' * 50}")
        print(f"Record:{q['context']}")
        print(f"Statement: {q['statement']}")
        print(f"\nQ{i}: {q['question']}")
        print("    1. Yes")
        print("    2. No")

        try:
            choice = input("Your answer (1-2): ").strip()
            answers = {"1": "Yes", "2": "No"}
            if choice in answers:
                selected = answers[choice]
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

    print(f"\nScore: {score}/{len(DATA_MATCHING_QUESTIONS)}")
    return score


def run_error_detection_practice():
    """Practice error detection."""
    print("\n" + "=" * 60)
    print("ERROR DETECTION PRACTICE")
    print("=" * 60)

    score = 0
    for i, q in enumerate(ERROR_DETECTION_QUESTIONS, 1):
        print(f"\n{'─' * 50}")
        print(f"Text:{q['text']}")
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

    print(f"\nScore: {score}/{len(ERROR_DETECTION_QUESTIONS)}")
    return score


def run_number_verification_practice():
    """Practice number verification."""
    print("\n" + "=" * 60)
    print("NUMBER VERIFICATION PRACTICE")
    print("=" * 60)

    score = 0
    for i, q in enumerate(NUMBER_VERIFICATION_QUESTIONS, 1):
        print(f"\n{'─' * 50}")
        print(f"Data:{q['data']}")
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

    print(f"\nScore: {score}/{len(NUMBER_VERIFICATION_QUESTIONS)}")
    return score


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("ATTENTION TO DETAIL PRACTICE")
    print("=" * 60)
    print("""
Choose a section:
1. Spot the Difference
2. Data Matching
3. Error Detection (Spelling)
4. Number Verification
5. All sections
6. Just show me the tips
""")

    choice = input("Enter choice (1-6): ").strip()

    if choice == "1":
        run_spot_difference_practice()
    elif choice == "2":
        run_data_matching_practice()
    elif choice == "3":
        run_error_detection_practice()
    elif choice == "4":
        run_number_verification_practice()
    elif choice == "5":
        total = 0
        total += run_spot_difference_practice()
        total += run_data_matching_practice()
        total += run_error_detection_practice()
        total += run_number_verification_practice()
        print(f"\n{'=' * 60}")
        print(f"TOTAL SCORE: {total}")
    else:
        print("""
QUICK TIPS FOR ATTENTION TO DETAIL:

1. COMPARING CODES/NUMBERS:
   - Go character by character
   - Watch for similar-looking characters: 0/O, 1/l/I, 5/S
   - Check length first - different lengths = different
   - Use your finger or cursor to track position

2. DATA MATCHING:
   - Read the original FIRST, thoroughly
   - Then read the comparison
   - Check each fact systematically
   - Partial matches are still wrong

3. ERROR DETECTION:
   - Read slowly, not at normal reading speed
   - Watch for doubled letters (shipped, submitted)
   - Watch for missing letters
   - Common errors: -ed endings, silent letters

4. NUMBER VERIFICATION:
   - Add numbers twice to confirm
   - Check for transposed digits (123 vs 132)
   - Verify decimal points and currency symbols
   - Double-check commas in large numbers

5. GENERAL:
   - Don't rush - accuracy matters more
   - Take a systematic approach (left→right, top→bottom)
   - Trust your process, not your "feeling"
   - When in doubt, compare again
""")
