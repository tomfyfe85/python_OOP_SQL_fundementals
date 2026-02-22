"""
Exercise 7.4: Repository Pattern with Python + SQLite

REPOSITORY PATTERN
==================

The Repository Pattern separates data access logic from business logic.
Instead of scattering SQL all over your code, you put it in one place.

This is DIP in action! Your business logic depends on the repository
abstraction, not on the database directly.

===================================
WHY USE THE REPOSITORY PATTERN?
===================================

BAD: SQL scattered everywhere
    def handle_signup(name, email):
        cursor.execute("INSERT INTO users ...")  # SQL in business logic!
        cursor.execute("SELECT * FROM users ...")
        send_welcome_email(email)

GOOD: Repository handles all data access
    class UserRepository:
        def create(self, name, email): ...
        def find_by_email(self, email): ...

    def handle_signup(repo, name, email):
        repo.create(name, email)        # No SQL here!
        user = repo.find_by_email(email)
        send_welcome_email(email)

Benefits:
1. SQL in one place - easy to find and update
2. Business logic doesn't know about the database
3. Easy to test - swap real repo for a fake one
4. Easy to switch databases - only change the repository

===================================
SQL INJECTION PREVENTION
===================================

NEVER do this (string formatting):
    cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
    # name = "'; DROP TABLE users; --"  <- SQL INJECTION!

ALWAYS do this (parameterised queries):
    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    # The ? placeholder safely escapes the input

===================================
EXERCISE
===================================

PART 1: User Model

    class User:
        def __init__(self, id: int | None, name: str, email: str, age: int):
            Store all attributes.

        def __repr__(self) -> str:
            Return "User(id={id}, name='{name}', email='{email}', age={age})"

        def __eq__(self, other) -> bool:
            Users are equal if all attributes match.

---

PART 2: UserRepository

    class UserRepository:

        def __init__(self, cursor):
            Store the cursor. Call create_table().

        def create_table(self) -> None:
            Create users table if not exists:
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            age INTEGER NOT NULL

        def create(self, user: User) -> User:
            Insert the user. Set user.id to the new row's id.
            Return the user (with id set).
            Use parameterised queries!

        def find_by_id(self, user_id: int) -> User | None:
            Return User if found, None if not.

        def find_by_email(self, email: str) -> User | None:
            Return User if found, None if not.

        def find_all(self) -> list[User]:
            Return all users as User objects.

        def update(self, user: User) -> bool:
            Update name, email, age for the given user (by id).
            Return True if updated, False if user not found.

        def delete(self, user_id: int) -> bool:
            Delete user by id.
            Return True if deleted, False if not found.

---

PART 3 (HARD): Advanced Repository Methods

        def find_by_age_range(self, min_age: int, max_age: int) -> list[User]:
            Return users whose age is between min_age and max_age (inclusive).

        def count(self) -> int:
            Return total number of users.

        def exists(self, email: str) -> bool:
            Return True if a user with this email exists.

ESTIMATED TIME: 30-45 minutes
"""

import sqlite3


# ============================================
# PART 1: User Model
# ============================================

# YOUR CODE HERE


# ============================================
# PART 2: UserRepository
# ============================================

# YOUR CODE HERE


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # ==========================================
    # PART 1 TESTS: User Model
    # ==========================================
    print("\n=== Test 1: User Model ===")
    try:
        user = User(None, "Alice", "alice@mail.com", 30)
        assert user.id is None
        assert user.name == "Alice"
        assert user.email == "alice@mail.com"
        assert user.age == 30
        assert repr(user) == "User(id=None, name='Alice', email='alice@mail.com', age=30)"

        user2 = User(1, "Alice", "alice@mail.com", 30)
        user3 = User(1, "Alice", "alice@mail.com", 30)
        assert user2 == user3

        print("  User model works")
        print("Test 1 PASSED!")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")
    except Exception as e:
        print(f"Test 1 ERROR: {e}")

    # ==========================================
    # PART 2 TESTS: UserRepository
    # ==========================================
    print("\n=== Test 2: Create User ===")
    try:
        repo = UserRepository(cursor)
        conn.commit()

        alice = User(None, "Alice", "alice@mail.com", 30)
        created = repo.create(alice)
        conn.commit()

        assert created.id is not None, "Should have an id after creation"
        assert created.id == 1
        assert created.name == "Alice"

        print(f"  Created: {created}")
        print("Test 2 PASSED!")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 ERROR: {e}")

    print("\n=== Test 3: Find by ID ===")
    try:
        found = repo.find_by_id(1)
        assert found is not None
        assert found.name == "Alice"
        assert found.email == "alice@mail.com"

        not_found = repo.find_by_id(999)
        assert not_found is None

        print(f"  Found: {found}")
        print("Test 3 PASSED!")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 ERROR: {e}")

    print("\n=== Test 4: Find by Email ===")
    try:
        found = repo.find_by_email("alice@mail.com")
        assert found is not None
        assert found.name == "Alice"

        not_found = repo.find_by_email("nobody@mail.com")
        assert not_found is None

        print("  Find by email works")
        print("Test 4 PASSED!")
    except AssertionError as e:
        print(f"Test 4 FAILED: {e}")
    except Exception as e:
        print(f"Test 4 ERROR: {e}")

    print("\n=== Test 5: Find All ===")
    try:
        bob = User(None, "Bob", "bob@mail.com", 25)
        charlie = User(None, "Charlie", "charlie@mail.com", 35)
        repo.create(bob)
        repo.create(charlie)
        conn.commit()

        all_users = repo.find_all()
        assert len(all_users) == 3
        assert all(isinstance(u, User) for u in all_users)

        print(f"  Found {len(all_users)} users")
        print("Test 5 PASSED!")
    except AssertionError as e:
        print(f"Test 5 FAILED: {e}")
    except Exception as e:
        print(f"Test 5 ERROR: {e}")

    print("\n=== Test 6: Update ===")
    try:
        alice = repo.find_by_id(1)
        alice.age = 31
        alice.name = "Alice Smith"

        result = repo.update(alice)
        conn.commit()
        assert result == True

        updated = repo.find_by_id(1)
        assert updated.name == "Alice Smith"
        assert updated.age == 31

        # Update non-existent user
        fake = User(999, "Nobody", "no@mail.com", 0)
        assert repo.update(fake) == False

        print("  Update works")
        print("Test 6 PASSED!")
    except AssertionError as e:
        print(f"Test 6 FAILED: {e}")
    except Exception as e:
        print(f"Test 6 ERROR: {e}")

    print("\n=== Test 7: Delete ===")
    try:
        result = repo.delete(3)  # Delete Charlie
        conn.commit()
        assert result == True
        assert repo.find_by_id(3) is None

        assert repo.delete(999) == False  # Non-existent

        all_users = repo.find_all()
        assert len(all_users) == 2

        print("  Delete works")
        print("Test 7 PASSED!")
    except AssertionError as e:
        print(f"Test 7 FAILED: {e}")
    except Exception as e:
        print(f"Test 7 ERROR: {e}")

    print("\n=== Test 8: Duplicate Email ===")
    try:
        duplicate = User(None, "Fake Alice", "alice@mail.com", 20)
        try:
            repo.create(duplicate)
            conn.commit()
            assert False, "Should raise error for duplicate email"
        except sqlite3.IntegrityError:
            conn.rollback()
            pass  # Expected!

        print("  Duplicate email correctly rejected")
        print("Test 8 PASSED!")
    except AssertionError as e:
        print(f"Test 8 FAILED: {e}")
    except Exception as e:
        print(f"Test 8 ERROR: {e}")

    # ==========================================
    # PART 3 TESTS (HARD): Uncomment when ready
    # ==========================================

    # # Add more users for testing
    # repo.create(User(None, "Diana", "diana@mail.com", 22))
    # repo.create(User(None, "Eve", "eve@mail.com", 28))
    # repo.create(User(None, "Frank", "frank@mail.com", 40))
    # conn.commit()

    # print("\n=== Test 9: Find by Age Range ===")
    # try:
    #     young = repo.find_by_age_range(20, 29)
    #     names = [u.name for u in young]
    #     assert "Bob" in names
    #     assert "Diana" in names
    #     assert "Eve" in names
    #     assert "Frank" not in names
    #
    #     print(f"  Users aged 20-29: {names}")
    #     print("Test 9 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 9 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 9 ERROR: {e}")

    # print("\n=== Test 10: Count and Exists ===")
    # try:
    #     assert repo.count() == 5
    #     assert repo.exists("alice@mail.com") == True
    #     assert repo.exists("nobody@mail.com") == False
    #
    #     print(f"  Count: {repo.count()}")
    #     print("Test 10 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 10 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 10 ERROR: {e}")

    conn.close()

    print("\n" + "=" * 60)
    print("REPOSITORY PATTERN KEY LESSONS")
    print("=" * 60)
    print("""
1. Repository Pattern separates data access from business logic
2. All SQL lives in the repository - one place to maintain
3. ALWAYS use parameterised queries (?) to prevent SQL injection
4. Return domain objects (User), not raw tuples
5. This IS the Dependency Inversion Principle in practice
6. Easy to test: swap the real repository for a fake/mock
7. cursor.lastrowid gives you the auto-generated id after INSERT
""")
    print("=" * 60)
