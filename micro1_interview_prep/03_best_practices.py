"""
Micro1 AI Interview Prep - Module 3: Clean Code & Best Practices
================================================================

VERBAL INTERVIEW QUESTIONS about writing production-quality code.

This is a big focus for this role - they want clean, maintainable code!
"""


# ============================================
# CODE QUALITY & CLEAN CODE
# ============================================

CODE_QUALITY_QUESTIONS = [
    {
        "question": "What does 'clean code' mean to you? How do you ensure your code is clean?",
        "key_points": [
            "Readable - easy for others (and future you) to understand",
            "Meaningful names for variables, functions, classes",
            "Small, focused functions (single responsibility)",
            "Consistent formatting and style",
            "Self-documenting - comments explain 'why', not 'what'",
            "Easy to modify and extend",
            "DRY - Don't Repeat Yourself",
        ],
        "example_answer": """
Clean code to me means code that's easy to read, understand, and modify. Someone
new to the project should be able to follow the logic without excessive explanation.

I focus on:
- Meaningful names that describe what things do - not 'x' but 'user_count'
- Small functions that do one thing well - if a function is doing multiple things,
  I split it up
- Consistent formatting - I use linters like ESLint for JavaScript and Black for
  Python to enforce style
- Comments that explain WHY, not WHAT - the code shows what's happening, comments
  explain the reasoning

I also follow DRY - if I'm copying and pasting code, that's a sign I should extract
it into a reusable function. But I balance this with readability - sometimes a little
duplication is clearer than over-abstraction.
"""
    },
    {
        "question": "How do you approach code reviews? What do you look for?",
        "key_points": [
            "Focus on logic, architecture, potential bugs",
            "Check for edge cases and error handling",
            "Ensure tests are adequate",
            "Look for readability and maintainability",
            "Be constructive, not critical of the person",
            "Suggest improvements, don't just point out problems",
            "Don't nitpick style if linters handle it",
        ],
        "example_answer": """
When reviewing code, I focus on several areas:

First, correctness - does the code do what it's supposed to? Are edge cases handled?
What happens with invalid input or errors?

Second, architecture - does this fit well with the existing codebase? Is the approach
reasonable or is there a simpler way?

Third, tests - are there adequate tests? Do they cover the happy path and error cases?

Fourth, readability - would someone unfamiliar with this code understand it? Are
names clear? Is the flow logical?

I don't nitpick formatting since linters handle that. My feedback is always
constructive - I explain why something might be an issue and suggest alternatives.
I also highlight what's good, not just what needs changing.

I approach reviews as a learning opportunity for both sides.
"""
    },
    {
        "question": "How do you handle technical debt?",
        "key_points": [
            "Recognize it's inevitable but needs management",
            "Document known debt (TODOs, tech debt tickets)",
            "Balance new features with paying down debt",
            "Refactor incrementally - boy scout rule",
            "Prioritize debt that causes the most friction",
            "Don't let it accumulate unchecked",
        ],
        "example_answer": """
Technical debt is inevitable - sometimes you ship something that works but isn't
ideal, due to time constraints or changing requirements. The key is managing it.

I document known debt as TODO comments or tickets in the backlog with context about
why it exists and what needs to change. This ensures it doesn't get forgotten.

I follow the boy scout rule - leave code cleaner than you found it. When working
on a file, I'll fix small issues along the way.

For larger debt, I advocate for dedicating time in each sprint to pay it down.
I prioritize debt that causes the most friction - slowing down development or
causing bugs.

I also try to prevent unnecessary debt by pushing back on shortcuts that will
cause significant problems later, while being pragmatic about deadlines.
"""
    },
    {
        "question": "Explain the SOLID principles. Which do you find most useful?",
        "key_points": [
            "S - Single Responsibility: one reason to change",
            "O - Open/Closed: open for extension, closed for modification",
            "L - Liskov Substitution: subtypes replaceable for parents",
            "I - Interface Segregation: small, focused interfaces",
            "D - Dependency Inversion: depend on abstractions",
            "SRP and DI are most commonly applicable",
        ],
        "example_answer": """
SOLID principles guide object-oriented design:

Single Responsibility - a class should have one reason to change. I split classes
that do too many things.

Open/Closed - code should be open for extension but closed for modification. I can
add new behavior without changing existing code, often using composition or inheritance.

Liskov Substitution - subclasses should be usable wherever parent classes are expected
without breaking things.

Interface Segregation - better to have small, specific interfaces than large ones
that force implementations to include unused methods.

Dependency Inversion - depend on abstractions, not concrete implementations. This
is where dependency injection comes in.

I find Single Responsibility and Dependency Inversion most useful day-to-day.
Keeping functions and classes focused makes code easier to test and understand.
Dependency injection makes code flexible and testable.
"""
    },
    {
        "question": "How do you approach writing tests? What's your testing strategy?",
        "key_points": [
            "Testing pyramid: many unit, some integration, few E2E",
            "Test behavior, not implementation",
            "Cover happy path and edge cases",
            "Write tests that are fast and reliable",
            "TDD when it makes sense (not always)",
            "Tests as documentation",
            "Don't aim for 100% coverage blindly",
        ],
        "example_answer": """
I follow the testing pyramid - mostly unit tests, supplemented by integration tests,
with a few end-to-end tests for critical flows.

Unit tests are fast and focused. They test individual functions or components in
isolation. I mock external dependencies so tests are reliable and don't depend on
databases or APIs being available.

Integration tests verify that pieces work together - like an API endpoint that hits
the database. These are slower but catch issues unit tests miss.

E2E tests verify complete user flows. They're slow and can be flaky, so I reserve
them for critical paths like login or checkout.

I test behavior, not implementation - my tests verify what the code does, not how
it does it. This way tests don't break when I refactor internals.

I aim for meaningful coverage, not 100%. I prioritize testing complex logic and
edge cases over trivial getters and setters.
"""
    },
]


# ============================================
# API DESIGN
# ============================================

API_DESIGN_QUESTIONS = [
    {
        "question": "What makes a good REST API design?",
        "key_points": [
            "Consistent naming (plural nouns for resources)",
            "Proper HTTP methods (GET, POST, PUT, DELETE)",
            "Appropriate status codes",
            "Versioning strategy",
            "Clear error responses",
            "Pagination for lists",
            "Good documentation (OpenAPI/Swagger)",
        ],
        "example_answer": """
Good REST API design is consistent and intuitive.

Resources are named with plural nouns - /users, /products - and HTTP methods
indicate actions: GET to read, POST to create, PUT/PATCH to update, DELETE to remove.

I use appropriate status codes: 200 for success, 201 for created, 400 for bad
requests, 401 for unauthorized, 404 for not found, 500 for server errors.

I include API versioning - usually in the URL like /api/v1 - so I can evolve the
API without breaking existing clients.

Error responses are consistent JSON with an error code, message, and any relevant
details. Lists support pagination with limit/offset or cursor-based pagination.

I document everything with OpenAPI/Swagger, which FastAPI generates automatically.
Good documentation is as important as good code.
"""
    },
    {
        "question": "How do you handle API versioning?",
        "key_points": [
            "URL versioning (/api/v1/users) - most common",
            "Header versioning (Accept: application/vnd.api+json;version=1)",
            "Query param versioning (?version=1)",
            "Each has tradeoffs",
            "Plan for deprecation and migration",
            "Maintain backwards compatibility where possible",
        ],
        "example_answer": """
I typically use URL versioning - /api/v1/users - because it's explicit and easy
to understand. Clients know exactly which version they're using, and it's easy
to test in a browser or API tool.

Header or query param versioning can be cleaner but requires more documentation
and client awareness.

When introducing a new version, I maintain the old version for a deprecation period,
clearly communicate the timeline to consumers, and document migration steps.

I try to make non-breaking changes when possible - adding fields is fine, removing
or changing them breaks clients. For breaking changes, that's when a new version
is needed.
"""
    },
]


# ============================================
# DEBUGGING & PROBLEM SOLVING
# ============================================

DEBUGGING_QUESTIONS = [
    {
        "question": "Walk me through how you debug a production issue.",
        "key_points": [
            "Gather information - logs, error reports, user reports",
            "Reproduce the issue (if possible)",
            "Check recent changes (deployments, config)",
            "Isolate the problem",
            "Fix and verify",
            "Write tests to prevent regression",
            "Post-mortem for significant issues",
        ],
        "example_answer": """
When a production issue comes in, I first gather information - check logs, error
tracking tools like Sentry, and any user reports. I want to understand the scope:
is it affecting everyone or just some users?

I check for recent changes - was there a deployment? A config change? Often issues
correlate with recent updates.

If possible, I reproduce the issue locally or in a staging environment. This lets
me debug interactively. If I can't reproduce it, I add more logging to gather
additional context.

Once I've identified the cause, I develop a fix and test it thoroughly. For urgent
issues, this might be a quick patch followed by a proper fix later.

After resolving, I write tests to catch this scenario in the future. For significant
outages, I lead or participate in a post-mortem to understand what happened and
prevent similar issues.
"""
    },
    {
        "question": "How do you approach learning a new codebase?",
        "key_points": [
            "Start with documentation and README",
            "Run the application, use it as a user",
            "Trace a simple flow end-to-end",
            "Read tests to understand expected behavior",
            "Use IDE features to navigate code",
            "Ask questions early",
            "Make small changes to verify understanding",
        ],
        "example_answer": """
I start with any available documentation - README, architecture docs, API docs.
This gives me context about the project's purpose and structure.

Then I run the application and use it. Understanding the user experience helps
me understand what the code is trying to accomplish.

I pick a simple feature and trace it through the code end-to-end - from the UI
or API endpoint through to the database. This shows me the architecture and patterns
used in the project.

Tests are valuable documentation. I read tests to understand expected behavior
and edge cases the original developers considered.

I use IDE features like go-to-definition and find-references to navigate. I also
make small changes or add logging to verify my understanding.

I'm not shy about asking questions - it's faster to ask someone who knows than to
spend hours figuring out why something is done a certain way.
"""
    },
]


# ============================================
# PRACTICE RUNNER
# ============================================

def run_practice(questions, section_name):
    """Run through questions interactively."""
    print(f"\n{'=' * 60}")
    print(f"{section_name}")
    print("=" * 60)
    print("Instructions: Read question, answer OUT LOUD, then check key points.\n")

    for i, q in enumerate(questions, 1):
        print(f"\n{'─' * 60}")
        print(f"QUESTION {i}/{len(questions)}:")
        print(f"\n  \"{q['question']}\"")

        input("\n[Answer out loud, then press Enter to see key points...]")

        print("\nKEY POINTS TO MENTION:")
        for point in q['key_points']:
            print(f"  • {point}")

        input("\n[Press Enter to see example answer...]")

        print("\nEXAMPLE ANSWER:")
        print(q['example_answer'])

        input("\n[Press Enter for next question...]")


def show_quick_reference():
    """Show all questions."""
    print("\n" + "=" * 60)
    print("QUICK REFERENCE - BEST PRACTICES QUESTIONS")
    print("=" * 60)

    print("\nCODE QUALITY:")
    for i, q in enumerate(CODE_QUALITY_QUESTIONS, 1):
        print(f"  {i}. {q['question']}")

    print("\nAPI DESIGN:")
    for i, q in enumerate(API_DESIGN_QUESTIONS, 1):
        print(f"  {i}. {q['question']}")

    print("\nDEBUGGING:")
    for i, q in enumerate(DEBUGGING_QUESTIONS, 1):
        print(f"  {i}. {q['question']}")


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("CLEAN CODE & BEST PRACTICES INTERVIEW PREP")
    print("=" * 60)
    print("""
Choose an option:
1. Code Quality & Clean Code
2. API Design
3. Debugging & Problem Solving
4. All questions
5. Quick reference (list all)
""")

    choice = input("Enter choice (1-5): ").strip()

    if choice == "1":
        run_practice(CODE_QUALITY_QUESTIONS, "CODE QUALITY")
    elif choice == "2":
        run_practice(API_DESIGN_QUESTIONS, "API DESIGN")
    elif choice == "3":
        run_practice(DEBUGGING_QUESTIONS, "DEBUGGING")
    elif choice == "4":
        all_q = CODE_QUALITY_QUESTIONS + API_DESIGN_QUESTIONS + DEBUGGING_QUESTIONS
        run_practice(all_q, "ALL BEST PRACTICES")
    else:
        show_quick_reference()
