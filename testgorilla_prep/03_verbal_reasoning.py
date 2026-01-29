"""
TestGorilla Prep - Module 3: Verbal Reasoning
==============================================

WHAT IT TESTS:
- Word analogies (A is to B as C is to ?)
- Reading comprehension (true/false/cannot say)
- Word relationships (synonyms, antonyms)
- Understanding written information

TIPS:
- Read carefully - the answer is in the text
- "Cannot say" means the info isn't provided
- Don't use outside knowledge for comprehension
- Analogies: identify the relationship first
"""

import random


# ============================================
# SECTION 1: WORD ANALOGIES
# ============================================

"""
COMMON ANALOGY RELATIONSHIPS:

1. SYNONYMS: Happy is to Joyful as Sad is to Miserable
2. ANTONYMS: Hot is to Cold as Light is to Dark
3. PART TO WHOLE: Wheel is to Car as Key is to Keyboard
4. OBJECT TO FUNCTION: Pen is to Write as Knife is to Cut
5. DEGREE/INTENSITY: Warm is to Hot as Cool is to Cold
6. CATEGORY: Dog is to Animal as Rose is to Flower
7. WORKER TO TOOL: Carpenter is to Hammer as Painter is to Brush
8. CAUSE TO EFFECT: Fire is to Smoke as Rain is to Flood

STRATEGY:
1. Identify the relationship in the first pair
2. Apply the same relationship to find the answer
"""

ANALOGY_QUESTIONS = [
    {
        "analogy": "Book is to Reading as Fork is to ?",
        "options": ["Knife", "Eating", "Kitchen", "Metal"],
        "answer": "Eating",
        "explanation": "Object to function: Book is used for reading, fork is used for eating."
    },
    {
        "analogy": "Doctor is to Hospital as Teacher is to ?",
        "options": ["Student", "School", "Classroom", "Education"],
        "answer": "School",
        "explanation": "Worker to workplace: Doctor works in hospital, teacher works in school."
    },
    {
        "analogy": "Finger is to Hand as Toe is to ?",
        "options": ["Leg", "Foot", "Shoe", "Walk"],
        "answer": "Foot",
        "explanation": "Part to whole: Finger is part of hand, toe is part of foot."
    },
    {
        "analogy": "Puppy is to Dog as Kitten is to ?",
        "options": ["Pet", "Cat", "Animal", "Fur"],
        "answer": "Cat",
        "explanation": "Young to adult: Puppy grows into dog, kitten grows into cat."
    },
    {
        "analogy": "Whisper is to Shout as Walk is to ?",
        "options": ["Run", "Move", "Slow", "Quiet"],
        "answer": "Run",
        "explanation": "Degree/intensity: Whisper is quiet speech, shout is loud. Walk is slow, run is fast."
    },
    {
        "analogy": "Bird is to Nest as Bee is to ?",
        "options": ["Honey", "Flower", "Hive", "Sting"],
        "answer": "Hive",
        "explanation": "Animal to home: Bird lives in nest, bee lives in hive."
    },
    {
        "analogy": "Chapter is to Book as Scene is to ?",
        "options": ["Movie", "Play", "Actor", "Stage"],
        "answer": "Play",
        "explanation": "Part to whole: Chapter is part of book, scene is part of play/movie."
    },
    {
        "analogy": "Hot is to Cold as Wet is to ?",
        "options": ["Water", "Dry", "Rain", "Warm"],
        "answer": "Dry",
        "explanation": "Antonyms: Hot is opposite of cold, wet is opposite of dry."
    },
    {
        "analogy": "Painter is to Brush as Writer is to ?",
        "options": ["Book", "Pen", "Paper", "Story"],
        "answer": "Pen",
        "explanation": "Worker to tool: Painter uses brush, writer uses pen."
    },
    {
        "analogy": "Ocean is to Water as Desert is to ?",
        "options": ["Hot", "Dry", "Sand", "Cactus"],
        "answer": "Sand",
        "explanation": "Place to main feature: Ocean is full of water, desert is full of sand."
    },
]


# ============================================
# SECTION 2: READING COMPREHENSION
# ============================================

"""
THREE POSSIBLE ANSWERS:
- TRUE: The statement follows logically from the passage
- FALSE: The statement contradicts the passage
- CANNOT SAY: Not enough information in the passage

IMPORTANT:
- Only use information IN the passage
- Don't use your own knowledge
- "Cannot say" is not the same as "don't know"
"""

COMPREHENSION_PASSAGES = [
    {
        "passage": """
        The company reported a 15% increase in revenue for the third quarter,
        reaching £2.3 million. This growth was primarily driven by strong
        performance in the European market, which saw a 25% increase compared
        to the same period last year. The North American market remained stable.
        """,
        "questions": [
            {
                "statement": "The company's revenue exceeded £2 million in Q3.",
                "answer": "TRUE",
                "explanation": "The passage states revenue reached £2.3 million, which exceeds £2 million."
            },
            {
                "statement": "The European market performed better than the North American market.",
                "answer": "TRUE",
                "explanation": "Europe had 25% growth while North America was 'stable' (no growth)."
            },
            {
                "statement": "The company is profitable.",
                "answer": "CANNOT SAY",
                "explanation": "Revenue is mentioned, but profit is not discussed. High revenue doesn't guarantee profit."
            },
            {
                "statement": "Q3 revenue was higher than Q2 revenue.",
                "answer": "CANNOT SAY",
                "explanation": "The passage mentions Q3 compared to last year's Q3, not to Q2."
            },
        ]
    },
    {
        "passage": """
        All employees must complete the new cybersecurity training by the end
        of the month. The training takes approximately 2 hours and can be
        completed online. Employees who fail to complete the training will
        have their system access temporarily suspended until completion.
        """,
        "questions": [
            {
                "statement": "The training is mandatory for all employees.",
                "answer": "TRUE",
                "explanation": "'All employees must complete' indicates it's mandatory."
            },
            {
                "statement": "The training must be completed in one sitting.",
                "answer": "CANNOT SAY",
                "explanation": "The passage says it takes 2 hours but doesn't specify if breaks are allowed."
            },
            {
                "statement": "Employees who don't complete training will be fired.",
                "answer": "FALSE",
                "explanation": "The passage says access will be 'temporarily suspended', not that they'll be fired."
            },
            {
                "statement": "The training can be done from home.",
                "answer": "CANNOT SAY",
                "explanation": "'Online' doesn't necessarily mean from home - could be office computer."
            },
        ]
    },
    {
        "passage": """
        The study found that participants who exercised for at least 30 minutes
        daily reported higher levels of satisfaction with their sleep quality.
        However, exercising within 2 hours of bedtime was associated with
        difficulty falling asleep. The study included 500 adults aged 25-45.
        """,
        "questions": [
            {
                "statement": "Daily exercise improves sleep quality.",
                "answer": "TRUE",
                "explanation": "Those who exercised daily reported higher sleep quality satisfaction."
            },
            {
                "statement": "You should not exercise in the evening.",
                "answer": "CANNOT SAY",
                "explanation": "The passage says within 2 hours of bedtime is problematic, not evening generally."
            },
            {
                "statement": "The findings apply to people over 45.",
                "answer": "CANNOT SAY",
                "explanation": "The study only included ages 25-45, so we can't extend findings to older adults."
            },
            {
                "statement": "Exercising just before bed helps you sleep.",
                "answer": "FALSE",
                "explanation": "The passage says exercising within 2 hours of bedtime causes difficulty falling asleep."
            },
        ]
    },
]


# ============================================
# SECTION 3: WORD RELATIONSHIPS
# ============================================

SYNONYM_QUESTIONS = [
    {
        "word": "ABUNDANT",
        "question": "Which word is most similar in meaning?",
        "options": ["Scarce", "Plentiful", "Absent", "Sparse"],
        "answer": "Plentiful",
        "explanation": "Abundant means existing in large quantities, same as plentiful."
    },
    {
        "word": "CONCISE",
        "question": "Which word is most similar in meaning?",
        "options": ["Lengthy", "Brief", "Vague", "Detailed"],
        "answer": "Brief",
        "explanation": "Concise means expressing much in few words, similar to brief."
    },
    {
        "word": "DILIGENT",
        "question": "Which word is most similar in meaning?",
        "options": ["Lazy", "Careless", "Hardworking", "Quick"],
        "answer": "Hardworking",
        "explanation": "Diligent means showing care and effort, same as hardworking."
    },
    {
        "word": "OBSOLETE",
        "question": "Which word is most similar in meaning?",
        "options": ["Modern", "Outdated", "Useful", "Popular"],
        "answer": "Outdated",
        "explanation": "Obsolete means no longer used, same as outdated."
    },
]

ANTONYM_QUESTIONS = [
    {
        "word": "EXPAND",
        "question": "Which word is most opposite in meaning?",
        "options": ["Grow", "Contract", "Spread", "Increase"],
        "answer": "Contract",
        "explanation": "Expand means to grow larger, contract means to shrink."
    },
    {
        "word": "TEMPORARY",
        "question": "Which word is most opposite in meaning?",
        "options": ["Brief", "Permanent", "Short", "Fleeting"],
        "answer": "Permanent",
        "explanation": "Temporary means lasting for a limited time, permanent means lasting forever."
    },
    {
        "word": "TRANSPARENT",
        "question": "Which word is most opposite in meaning?",
        "options": ["Clear", "Opaque", "Visible", "Obvious"],
        "answer": "Opaque",
        "explanation": "Transparent means see-through, opaque means not transparent."
    },
    {
        "word": "ACCELERATE",
        "question": "Which word is most opposite in meaning?",
        "options": ["Speed up", "Decelerate", "Rush", "Hurry"],
        "answer": "Decelerate",
        "explanation": "Accelerate means speed up, decelerate means slow down."
    },
]


# ============================================
# PRACTICE RUNNER
# ============================================

def run_analogy_practice():
    """Practice word analogies."""
    print("\n" + "=" * 60)
    print("WORD ANALOGY PRACTICE")
    print("=" * 60)
    print("Complete each analogy.\n")

    score = 0
    questions = random.sample(ANALOGY_QUESTIONS, min(5, len(ANALOGY_QUESTIONS)))

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['analogy']}")
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


def run_comprehension_practice():
    """Practice reading comprehension."""
    print("\n" + "=" * 60)
    print("READING COMPREHENSION PRACTICE")
    print("=" * 60)
    print("Answer TRUE, FALSE, or CANNOT SAY based only on the passage.\n")

    score = 0
    total = 0

    for passage_data in COMPREHENSION_PASSAGES:
        print(f"\n{'─' * 60}")
        print("PASSAGE:")
        print(passage_data['passage'])
        print(f"{'─' * 60}")

        for q in passage_data['questions']:
            total += 1
            print(f"\nStatement: \"{q['statement']}\"")
            print("    1. TRUE")
            print("    2. FALSE")
            print("    3. CANNOT SAY")

            try:
                choice = input("Your answer (1-3): ").strip()
                answers = {"1": "TRUE", "2": "FALSE", "3": "CANNOT SAY"}
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

    print(f"\nScore: {score}/{total}")
    return score


def run_vocabulary_practice():
    """Practice synonyms and antonyms."""
    print("\n" + "=" * 60)
    print("VOCABULARY PRACTICE")
    print("=" * 60)

    score = 0
    all_questions = SYNONYM_QUESTIONS + ANTONYM_QUESTIONS
    questions = random.sample(all_questions, min(6, len(all_questions)))

    for i, q in enumerate(questions, 1):
        print(f"\n{'─' * 40}")
        print(f"Word: {q['word']}")
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

    print(f"\nScore: {score}/{len(questions)}")
    return score


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("VERBAL REASONING PRACTICE")
    print("=" * 60)
    print("""
Choose a section:
1. Word Analogies
2. Reading Comprehension
3. Vocabulary (Synonyms/Antonyms)
4. All sections
5. Just show me the tips
""")

    choice = input("Enter choice (1-5): ").strip()

    if choice == "1":
        run_analogy_practice()
    elif choice == "2":
        run_comprehension_practice()
    elif choice == "3":
        run_vocabulary_practice()
    elif choice == "4":
        total = 0
        total += run_analogy_practice()
        total += run_comprehension_practice()
        total += run_vocabulary_practice()
        print(f"\n{'=' * 60}")
        print(f"TOTAL SCORE: {total}")
    else:
        print("""
QUICK TIPS FOR VERBAL REASONING:

1. ANALOGIES:
   - Identify the relationship FIRST
   - Common relationships: synonym, antonym, part-whole,
     function, degree, category, worker-tool
   - Test your answer: "X is to Y as A is to B" should work both ways

2. READING COMPREHENSION:
   - Only use information IN the passage
   - Don't use outside knowledge!
   - TRUE = directly supported by text
   - FALSE = contradicts the text
   - CANNOT SAY = not mentioned or not enough info

3. VOCABULARY:
   - If stuck, try using the word in a sentence
   - Eliminate options that are clearly wrong
   - Watch for words that sound similar but have different meanings

4. COMMON TRAPS:
   - "Cannot say" vs "False" - they're different!
   - Assumptions based on common knowledge
   - Words with multiple meanings

5. TIME MANAGEMENT:
   - Don't spend too long on any one question
   - For comprehension, skim passage first for structure
""")
