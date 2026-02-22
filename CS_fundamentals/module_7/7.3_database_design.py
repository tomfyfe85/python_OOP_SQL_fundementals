"""
Exercise 7.3: Database Design and Normalisation

DATABASE DESIGN
===============

Good database design prevents:
- Data duplication (same info stored in multiple places)
- Update anomalies (changing data in one place but not another)
- Deletion anomalies (losing data when deleting a record)

===================================
NORMALISATION
===================================

1NF (First Normal Form):
    - Each cell contains a single value (no lists or sets)
    - Each row is unique (has a primary key)
    BAD:  | name  | phones              |
          | Alice | 123-4567, 890-1234  |  <- multiple values!
    GOOD: | name  | phone    |
          | Alice | 123-4567 |
          | Alice | 890-1234 |

2NF (Second Normal Form):
    - Is in 1NF
    - Every non-key column depends on the ENTIRE primary key
    BAD:  | student_id | course_id | student_name | grade |
          student_name depends only on student_id, not course_id!
    GOOD: Separate into students table and enrollments table.

3NF (Third Normal Form):
    - Is in 2NF
    - No non-key column depends on another non-key column
    BAD:  | id | city       | postcode |
          postcode depends on city, not on id!
    GOOD: Separate into addresses and postcodes tables.

===================================
RELATIONSHIPS
===================================

ONE-TO-MANY: One customer has many orders
    customers (id, name)
    orders (id, customer_id REFERENCES customers)

MANY-TO-MANY: Students take many courses, courses have many students
    students (id, name)
    courses (id, title)
    enrollments (student_id, course_id)  <- JUNCTION TABLE

ONE-TO-ONE: One user has one profile
    users (id, username)
    profiles (id, user_id UNIQUE REFERENCES users)

===================================
EXERCISE: Design a Library Database
===================================

Design and implement a database for a library system.

PART 1: Create the Schema

Create these tables with appropriate constraints:

    authors
    - id: INTEGER PRIMARY KEY AUTOINCREMENT
    - name: TEXT NOT NULL
    - country: TEXT

    books
    - id: INTEGER PRIMARY KEY AUTOINCREMENT
    - title: TEXT NOT NULL
    - isbn: TEXT UNIQUE NOT NULL
    - published_year: INTEGER
    - author_id: INTEGER (FOREIGN KEY -> authors)

    members
    - id: INTEGER PRIMARY KEY AUTOINCREMENT
    - name: TEXT NOT NULL
    - email: TEXT UNIQUE NOT NULL
    - join_date: TEXT NOT NULL

    loans
    - id: INTEGER PRIMARY KEY AUTOINCREMENT
    - book_id: INTEGER NOT NULL (FOREIGN KEY -> books)
    - member_id: INTEGER NOT NULL (FOREIGN KEY -> members)
    - loan_date: TEXT NOT NULL
    - return_date: TEXT (NULL if not yet returned)

---

PART 2: Insert Sample Data

    insert_sample_data(cursor):
        Insert at least:
        - 3 authors
        - 5 books (across the authors)
        - 3 members
        - 4 loans (some returned, some not)

---

PART 3: Library Queries

    get_books_by_author(cursor, author_name: str) -> list[tuple]:
        Return (title, published_year) for all books by the given author.

    get_available_books(cursor) -> list[tuple]:
        Return (title, author_name) for books not currently on loan.
        A book is "on loan" if it has a loan with return_date IS NULL.

    get_member_loans(cursor, member_name: str) -> list[tuple]:
        Return (book_title, loan_date, return_date) for all loans by the member.
        Order by loan_date descending.

    get_overdue_summary(cursor) -> list[tuple]:
        Return (member_name, book_title, loan_date) for all books
        currently on loan (return_date IS NULL).

---

PART 4 (HARD): Advanced Queries

    get_most_borrowed_books(cursor) -> list[tuple]:
        Return (title, loan_count) for all books, ordered by loan_count desc.

    get_author_stats(cursor) -> list[tuple]:
        Return (author_name, book_count, total_loans) for each author.
        Order by total_loans descending.

ESTIMATED TIME: 45-60 minutes
"""

import sqlite3


# ============================================
# PART 1: Create Schema
# ============================================

def create_library_schema(cursor):
    """Create the library database tables."""
    # YOUR CODE HERE
    pass


# ============================================
# PART 2: Insert Sample Data
# ============================================

def insert_sample_data(cursor):
    """Insert sample authors, books, members, and loans."""
    # YOUR CODE HERE
    pass


# ============================================
# PART 3: Library Queries
# ============================================

def get_books_by_author(cursor, author_name: str) -> list[tuple]:
    """Return (title, published_year) for books by the given author."""
    # YOUR CODE HERE
    pass


def get_available_books(cursor) -> list[tuple]:
    """Return (title, author_name) for books not currently on loan."""
    # YOUR CODE HERE
    pass


def get_member_loans(cursor, member_name: str) -> list[tuple]:
    """Return (book_title, loan_date, return_date) for member's loans."""
    # YOUR CODE HERE
    pass


def get_overdue_summary(cursor) -> list[tuple]:
    """Return (member_name, book_title, loan_date) for current loans."""
    # YOUR CODE HERE
    pass


# ============================================
# PART 4 (HARD): Advanced Queries
# ============================================

def get_most_borrowed_books(cursor) -> list[tuple]:
    """Return (title, loan_count) ordered by count desc."""
    # YOUR CODE HERE
    pass


def get_author_stats(cursor) -> list[tuple]:
    """Return (author_name, book_count, total_loans) ordered by loans desc."""
    # YOUR CODE HERE
    pass


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    print("\n=== Test 1: Create Schema ===")
    try:
        create_library_schema(cursor)
        conn.commit()

        # Verify tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [r[0] for r in cursor.fetchall()]
        assert 'authors' in tables, "Missing authors table"
        assert 'books' in tables, "Missing books table"
        assert 'members' in tables, "Missing members table"
        assert 'loans' in tables, "Missing loans table"

        print("  All 4 tables created")
        print("Test 1 PASSED!")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")
    except Exception as e:
        print(f"Test 1 ERROR: {e}")

    print("\n=== Test 2: Insert Sample Data ===")
    try:
        insert_sample_data(cursor)
        conn.commit()

        cursor.execute("SELECT COUNT(*) FROM authors")
        assert cursor.fetchone()[0] >= 3, "Need at least 3 authors"

        cursor.execute("SELECT COUNT(*) FROM books")
        assert cursor.fetchone()[0] >= 5, "Need at least 5 books"

        cursor.execute("SELECT COUNT(*) FROM members")
        assert cursor.fetchone()[0] >= 3, "Need at least 3 members"

        cursor.execute("SELECT COUNT(*) FROM loans")
        assert cursor.fetchone()[0] >= 4, "Need at least 4 loans"

        # Check some loans have return_date and some don't
        cursor.execute("SELECT COUNT(*) FROM loans WHERE return_date IS NULL")
        unreturned = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM loans WHERE return_date IS NOT NULL")
        returned = cursor.fetchone()[0]
        assert unreturned > 0, "Need some unreturned loans"
        assert returned > 0, "Need some returned loans"

        print("  Sample data inserted correctly")
        print("Test 2 PASSED!")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 ERROR: {e}")

    print("\n=== Test 3: Books by Author ===")
    try:
        # Get first author name from the database
        cursor.execute("SELECT name FROM authors LIMIT 1")
        author_name = cursor.fetchone()[0]

        results = get_books_by_author(cursor, author_name)
        assert len(results) > 0, f"No books found for {author_name}"
        assert len(results[0]) == 2, "Should return (title, published_year)"

        print(f"  Books by {author_name}:")
        for title, year in results:
            print(f"    {title} ({year})")
        print("Test 3 PASSED!")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 ERROR: {e}")

    print("\n=== Test 4: Available Books ===")
    try:
        results = get_available_books(cursor)
        assert len(results) > 0, "Should have some available books"
        assert len(results[0]) == 2, "Should return (title, author_name)"

        print(f"  {len(results)} books available:")
        for title, author in results:
            print(f"    {title} by {author}")
        print("Test 4 PASSED!")
    except AssertionError as e:
        print(f"Test 4 FAILED: {e}")
    except Exception as e:
        print(f"Test 4 ERROR: {e}")

    print("\n=== Test 5: Member Loans ===")
    try:
        cursor.execute("SELECT name FROM members LIMIT 1")
        member_name = cursor.fetchone()[0]

        results = get_member_loans(cursor, member_name)
        assert len(results[0]) == 3, "Should return (title, loan_date, return_date)"

        print(f"  Loans for {member_name}:")
        for title, loan_date, return_date in results:
            status = return_date if return_date else "ON LOAN"
            print(f"    {title}: borrowed {loan_date}, returned: {status}")
        print("Test 5 PASSED!")
    except AssertionError as e:
        print(f"Test 5 FAILED: {e}")
    except Exception as e:
        print(f"Test 5 ERROR: {e}")

    print("\n=== Test 6: Overdue Summary ===")
    try:
        results = get_overdue_summary(cursor)
        assert len(results) > 0, "Should have unreturned loans"
        assert len(results[0]) == 3, "Should return (member, title, loan_date)"

        print(f"  Currently on loan:")
        for member, title, date in results:
            print(f"    {member}: {title} (since {date})")
        print("Test 6 PASSED!")
    except AssertionError as e:
        print(f"Test 6 FAILED: {e}")
    except Exception as e:
        print(f"Test 6 ERROR: {e}")

    # ==========================================
    # PART 4 TESTS (HARD): Uncomment when ready
    # ==========================================

    # print("\n=== Test 7: Most Borrowed Books ===")
    # try:
    #     results = get_most_borrowed_books(cursor)
    #     assert len(results) > 0
    #     assert results[0][1] >= results[-1][1], "Should be ordered by count desc"
    #
    #     print("  Most borrowed:")
    #     for title, count in results:
    #         print(f"    {title}: {count} loans")
    #     print("Test 7 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 7 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 7 ERROR: {e}")

    # print("\n=== Test 8: Author Stats ===")
    # try:
    #     results = get_author_stats(cursor)
    #     assert len(results) > 0
    #     assert len(results[0]) == 3, "Should return (author, book_count, total_loans)"
    #
    #     print("  Author stats:")
    #     for author, books, loans in results:
    #         print(f"    {author}: {books} books, {loans} total loans")
    #     print("Test 8 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 8 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 8 ERROR: {e}")

    conn.close()

    print("\n" + "=" * 60)
    print("DATABASE DESIGN KEY LESSONS")
    print("=" * 60)
    print("""
1. Normalisation prevents data duplication and anomalies
2. 1NF: No multi-valued columns
3. 2NF: Non-key columns depend on the WHOLE key
4. 3NF: No non-key column depends on another non-key column
5. Foreign keys enforce relationships between tables
6. Junction tables handle many-to-many relationships
7. NULL in return_date = "currently on loan" pattern
""")
    print("=" * 60)
