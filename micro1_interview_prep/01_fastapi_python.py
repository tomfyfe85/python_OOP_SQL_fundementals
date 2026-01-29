"""
Micro1 AI Interview Prep - Module 1: Python & FastAPI
======================================================

VERBAL INTERVIEW QUESTIONS for Python FastAPI Developer role.

HOW TO USE:
1. Read each question aloud (or have someone ask you)
2. Answer OUT LOUD - practice speaking, not just reading
3. Time yourself - aim for 1-2 minute answers
4. Check the key points after to see what you covered
5. Practice until you can answer fluently without notes

TIP: AI interviewers are looking for:
- Clear, structured answers
- Specific examples from experience
- Technical accuracy
- Communication skills
"""


# ============================================
# FASTAPI FUNDAMENTALS
# ============================================

FASTAPI_QUESTIONS = [
    {
        "question": "What is FastAPI and why would you choose it over Flask or Django?",
        "key_points": [
            "FastAPI is a modern, high-performance Python web framework",
            "Built on Starlette (async) and Pydantic (data validation)",
            "Automatic API documentation (Swagger/OpenAPI)",
            "Type hints enable auto-validation and better IDE support",
            "Async/await support for high concurrency",
            "Faster than Flask, more lightweight than Django",
            "Great for microservices and APIs (Django better for full web apps)",
        ],
        "example_answer": """
FastAPI is a modern Python web framework designed specifically for building APIs.
I'd choose it over Flask because it has built-in data validation using Pydantic,
automatic API documentation, and native async support which gives better performance.

Compared to Django, FastAPI is more lightweight - Django is great for full web
applications with its ORM and admin panel, but for pure API development, FastAPI
is faster and has less overhead.

In my experience, FastAPI's type hints catch errors at development time rather
than runtime, which speeds up development significantly.
"""
    },
    {
        "question": "Explain how you would structure a FastAPI project for production.",
        "key_points": [
            "Separate routers by domain/feature (users, products, etc.)",
            "Use dependency injection for database sessions, auth",
            "Keep models, schemas, and routes in separate files",
            "Environment-based configuration (dev/staging/prod)",
            "Alembic for database migrations",
            "Docker for containerization",
            "Tests folder mirroring app structure",
        ],
        "example_answer": """
For a production FastAPI project, I typically structure it like this:

The main app folder contains routers separated by feature - like users, products,
orders. Each router has its own models, schemas, and CRUD operations.

I use a core folder for shared things like configuration, database connection,
and security utilities. Configuration is environment-based using Pydantic Settings.

Dependencies like database sessions and authentication are injected using FastAPI's
Depends system, which keeps the code clean and testable.

For the database, I use SQLAlchemy with Alembic for migrations. Everything runs
in Docker with separate containers for the app and database.

Tests mirror the app structure and use pytest with a test database.
"""
    },
    {
        "question": "How does dependency injection work in FastAPI? Give an example.",
        "key_points": [
            "Depends() function injects dependencies into route handlers",
            "Common uses: database sessions, current user, pagination",
            "Dependencies can be chained (dependency depends on another)",
            "Supports async dependencies",
            "Scoped per-request (cleanup happens automatically)",
        ],
        "example_answer": """
Dependency injection in FastAPI uses the Depends function. You define a function
that provides something - like a database session or the current user - and FastAPI
automatically calls it and passes the result to your route handler.

For example, I'd create a get_db function that yields a database session, then
use Depends(get_db) in my route. FastAPI handles the lifecycle - it creates the
session before the request and closes it after.

For authentication, I might have get_current_user that depends on a token validation
function. Dependencies can chain together, so get_current_admin_user might depend
on get_current_user.

This pattern makes testing easy because you can override dependencies with mocks.
"""
    },
    {
        "question": "How do you handle authentication and authorization in FastAPI?",
        "key_points": [
            "OAuth2 with Password flow or JWT tokens",
            "FastAPI security utilities (OAuth2PasswordBearer)",
            "Dependency for extracting and validating tokens",
            "Role-based access control via dependencies",
            "Password hashing with bcrypt/passlib",
            "Refresh tokens for session management",
        ],
        "example_answer": """
For authentication in FastAPI, I typically use JWT tokens with the OAuth2 password flow.

Users log in with credentials, which are validated against hashed passwords stored
in the database - I use bcrypt for hashing. On successful login, I generate a JWT
access token and optionally a refresh token.

I create a dependency called get_current_user that extracts the token from the
Authorization header, validates it, and returns the user. Routes that need
authentication just include this dependency.

For authorization, I might add another dependency like require_admin that checks
the user's role. This way, protecting a route is just adding Depends(require_admin).

I also implement token refresh endpoints so users don't need to re-login frequently.
"""
    },
    {
        "question": "Explain Pydantic and how you use it with FastAPI.",
        "key_points": [
            "Pydantic handles data validation and serialization",
            "Define schemas using Python type hints",
            "Automatic validation of request bodies",
            "Response models filter what data is returned",
            "Config class for customization (ORM mode, aliases)",
            "Validators for custom validation logic",
        ],
        "example_answer": """
Pydantic is the data validation library that FastAPI uses. You define schemas as
Python classes with type-annotated fields, and Pydantic automatically validates
incoming data against those types.

I typically create separate schemas for different operations - like UserCreate for
registration, UserResponse for API responses, and UserInDB for the database model.

The UserResponse schema would exclude sensitive fields like password hash. FastAPI
uses this as the response_model to automatically filter the output.

Pydantic also lets me add custom validators - for example, ensuring an email is
valid format or a password meets complexity requirements. These run automatically
when data is parsed.

With ORM mode enabled, Pydantic can read data directly from SQLAlchemy models.
"""
    },
    {
        "question": "How do you handle database operations in FastAPI?",
        "key_points": [
            "SQLAlchemy for ORM (or async alternatives like databases/SQLModel)",
            "Session management via dependency injection",
            "Alembic for migrations",
            "Connection pooling for performance",
            "Async database operations with encode/databases or asyncpg",
            "Repository pattern for separating database logic",
        ],
        "example_answer": """
I typically use SQLAlchemy as the ORM with FastAPI. I set up a database session
factory and inject sessions into routes using FastAPI's dependency system.

The session is created at the start of each request and automatically closed after.
I use connection pooling to manage database connections efficiently.

For schema changes, I use Alembic migrations. This lets me version control database
changes and apply them consistently across environments.

I often use a repository or CRUD pattern - separating the database operations into
their own functions rather than putting SQL directly in routes. This makes testing
easier and keeps routes clean.

For high-performance scenarios, I might use async database libraries like
encode/databases or SQLModel, which FastAPI supports natively.
"""
    },
    {
        "question": "How would you implement error handling in a FastAPI application?",
        "key_points": [
            "HTTPException for standard errors (404, 401, etc.)",
            "Custom exception classes for domain-specific errors",
            "Exception handlers for global error handling",
            "Consistent error response format",
            "Logging errors for debugging",
            "Don't expose internal errors to clients",
        ],
        "example_answer": """
FastAPI provides HTTPException for standard HTTP errors. For a 404, I'd raise
HTTPException with status_code=404 and a detail message.

For more complex applications, I create custom exception classes - like
ResourceNotFoundException or ValidationError - that inherit from a base exception.

I then register exception handlers that catch these exceptions and return
consistent JSON responses. This ensures all errors have the same format with
fields like error_code, message, and details.

I also add a catch-all handler for unexpected exceptions that logs the full
traceback for debugging but returns a generic "Internal Server Error" to the
client - never exposing stack traces or internal details.

All errors get logged with context like request ID, user ID, and endpoint for
easier debugging in production.
"""
    },
    {
        "question": "How do you test FastAPI applications?",
        "key_points": [
            "pytest as the test framework",
            "TestClient for integration testing",
            "Dependency overrides for mocking",
            "Separate test database",
            "Fixtures for common setup",
            "Test both happy path and error cases",
        ],
        "example_answer": """
I use pytest with FastAPI's TestClient for testing. TestClient lets you make
requests to your API without running a server.

For unit tests, I override dependencies - for example, replacing the real database
session with a test database, or mocking the current user.

I organize tests by feature, mirroring the app structure. Each test module has
fixtures for common setup like creating test users or seeding data.

I test both successful operations and error cases - like what happens when a
resource isn't found, or when validation fails. I also test authentication by
making requests with and without valid tokens.

For the database, I use a separate test database and run each test in a transaction
that rolls back, keeping tests isolated and fast.
"""
    },
]


# ============================================
# PYTHON SPECIFIC QUESTIONS
# ============================================

PYTHON_QUESTIONS = [
    {
        "question": "Explain async/await in Python. When would you use it?",
        "key_points": [
            "Async allows non-blocking I/O operations",
            "await pauses execution until operation completes",
            "Event loop manages concurrent tasks",
            "Great for I/O-bound tasks (API calls, database)",
            "Not helpful for CPU-bound tasks (use multiprocessing)",
            "FastAPI handles async natively",
        ],
        "example_answer": """
Async/await in Python enables concurrent execution of I/O-bound operations. When
you await something, Python can switch to other tasks while waiting, rather than
blocking.

I'd use async for operations that wait on external resources - database queries,
HTTP requests to other APIs, file operations. For example, if my endpoint needs
to call three external APIs, with async I can make all three calls concurrently
rather than sequentially, significantly reducing response time.

It's not helpful for CPU-intensive work like data processing - for that I'd use
multiprocessing instead.

FastAPI supports async natively, so I can write async route handlers and use
async database libraries. This lets the server handle many concurrent requests
efficiently.
"""
    },
    {
        "question": "What are Python decorators and how do you use them?",
        "key_points": [
            "Functions that modify other functions",
            "Use @ syntax above function definition",
            "Common uses: logging, caching, authentication",
            "Can take arguments",
            "Use functools.wraps to preserve function metadata",
        ],
        "example_answer": """
Decorators are functions that wrap other functions to extend their behavior without
modifying the original code. You apply them with the @ symbol above a function.

In FastAPI, decorators define routes - @app.get('/users') turns a function into
an endpoint. But I also write custom decorators.

For example, I might create a @log_execution_time decorator that logs how long a
function takes, or a @cache_result decorator that caches return values.

A decorator is essentially a function that takes a function as input and returns
a new function that adds behavior before or after the original. I always use
functools.wraps to preserve the original function's name and docstring.
"""
    },
    {
        "question": "How do you manage Python dependencies and virtual environments?",
        "key_points": [
            "Virtual environments isolate project dependencies",
            "venv, virtualenv, or conda for environment management",
            "requirements.txt or poetry/pipenv for dependency specification",
            "Pin versions for reproducibility",
            "Separate dev and production dependencies",
            "Docker can also provide isolation",
        ],
        "example_answer": """
I always use virtual environments to isolate project dependencies. For most projects,
Python's built-in venv is sufficient - I create one per project and activate it
when working on that project.

For dependency management, I typically use either requirements.txt with pip, or
Poetry for more complex projects. Poetry handles dependency resolution better and
separates dev dependencies.

I pin exact versions in production requirements to ensure reproducibility - if it
works in CI, it'll work in production with the same versions.

I maintain separate files for dev dependencies like pytest and linting tools versus
production dependencies. In Docker, I only install production dependencies in the
final image.
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
    print("""
Instructions:
1. Read each question
2. Answer OUT LOUD (practice speaking!)
3. Press Enter to see key points
4. Press Enter again for next question
""")

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

    print(f"\n{'=' * 60}")
    print("Section complete! Practice these until you can answer fluently.")


def show_quick_reference():
    """Show quick reference of all questions."""
    print("\n" + "=" * 60)
    print("QUICK REFERENCE - ALL FASTAPI/PYTHON QUESTIONS")
    print("=" * 60)

    print("\nFASTAPI QUESTIONS:")
    for i, q in enumerate(FASTAPI_QUESTIONS, 1):
        print(f"  {i}. {q['question']}")

    print("\nPYTHON QUESTIONS:")
    for i, q in enumerate(PYTHON_QUESTIONS, 1):
        print(f"  {i}. {q['question']}")


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("FASTAPI & PYTHON INTERVIEW PREP")
    print("=" * 60)
    print("""
Choose an option:
1. Practice FastAPI questions (verbal)
2. Practice Python questions (verbal)
3. Practice all questions
4. Quick reference (list all questions)
5. Show tips for verbal interviews
""")

    choice = input("Enter choice (1-5): ").strip()

    if choice == "1":
        run_practice(FASTAPI_QUESTIONS, "FASTAPI QUESTIONS")
    elif choice == "2":
        run_practice(PYTHON_QUESTIONS, "PYTHON QUESTIONS")
    elif choice == "3":
        run_practice(FASTAPI_QUESTIONS, "FASTAPI QUESTIONS")
        run_practice(PYTHON_QUESTIONS, "PYTHON QUESTIONS")
    elif choice == "4":
        show_quick_reference()
    else:
        print("""
TIPS FOR VERBAL TECHNICAL INTERVIEWS:

1. STRUCTURE YOUR ANSWERS
   - Start with a brief definition/overview
   - Give 2-3 key points
   - Include a specific example from your experience
   - Keep answers 1-2 minutes (don't ramble)

2. USE THE STAR METHOD FOR EXPERIENCE QUESTIONS
   - Situation: Set the context
   - Task: What was your responsibility
   - Action: What you specifically did
   - Result: The outcome

3. IT'S OK TO THINK
   - "That's a good question, let me think..."
   - "I'd approach this by first considering..."
   - Don't rush - a thoughtful answer beats a rushed one

4. BE HONEST ABOUT GAPS
   - "I haven't used X specifically, but I've used Y which is similar..."
   - "I'd need to look up the exact syntax, but conceptually..."

5. ASK FOR CLARIFICATION IF NEEDED
   - "Could you clarify what you mean by...?"
   - "Are you asking about X or Y specifically?"

6. PRACTICE OUT LOUD
   - Actually speak your answers
   - Record yourself and listen back
   - Practice with a friend if possible
""")
