"""
Exercise 7.1: SQL Basics with SQLite

SQL (Structured Query Language)
===============================

SQL is the standard language for interacting with relational databases.
We'll use SQLite (built into Python) so there's no setup needed.

===================================
KEY CONCEPTS
===================================

TABLE: Like a spreadsheet - rows and columns
ROW: A single record (one person, one order, etc.)
COLUMN: A field/attribute (name, age, email, etc.)
PRIMARY KEY: Unique identifier for each row
FOREIGN KEY: Links one table to another

===================================
CORE SQL OPERATIONS (CRUD)
===================================

    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER
    );

    INSERT INTO users (name, email, age) VALUES ('Alice', 'alice@mail.com', 30);

    SELECT * FROM users;
    SELECT name, age FROM users WHERE age > 25;
    SELECT * FROM users ORDER BY name ASC LIMIT 5;

    UPDATE users SET age = 31 WHERE name = 'Alice';

    DELETE FROM users WHERE id = 1;

===================================
COMMON DATA TYPES (SQLite)
===================================

    INTEGER  - Whole numbers
    REAL     - Floating point
    TEXT     - Strings
    BLOB     - Binary data
    NULL     - No value

===================================
EXERCISE
===================================

Complete each function below. Each function receives a cursor object
and should execute the appropriate SQL query.

PART 1: Create and Insert

    create_products_table(cursor):
        Create a table called 'products' with columns:
        - id: INTEGER PRIMARY KEY AUTOINCREMENT
        - name: TEXT NOT NULL
        - price: REAL NOT NULL
        - category: TEXT NOT NULL
        - in_stock: INTEGER NOT NULL DEFAULT 1

    insert_sample_products(cursor):
        Insert these products:
        ('Laptop', 999.99, 'Electronics', 1)
        ('Headphones', 49.99, 'Electronics', 1)
        ('Python Book', 29.99, 'Books', 1)
        ('Desk Lamp', 24.99, 'Home', 1)
        ('Keyboard', 79.99, 'Electronics', 0)
        ('SQL Guide', 34.99, 'Books', 1)
        ('Mouse', 19.99, 'Electronics', 1)
        ('Notebook', 4.99, 'Stationery', 1)

---

PART 2: SELECT Queries

    get_all_products(cursor) -> list[tuple]:
        Return all products, all columns.

    get_electronics(cursor) -> list[tuple]:
        Return all products in the 'Electronics' category.

    get_cheap_products(cursor) -> list[tuple]:
        Return products with price under 30, ordered by price ascending.

    get_product_names_and_prices(cursor) -> list[tuple]:
        Return only name and price columns for all products.

    get_in_stock_count(cursor) -> int:
        Return the number of products that are in stock (in_stock = 1).

---

PART 3: UPDATE and DELETE

    increase_book_prices(cursor) -> None:
        Increase the price of all 'Books' by 5.00.

    mark_out_of_stock(cursor, product_name: str) -> None:
        Set in_stock to 0 for the given product name.

    delete_stationery(cursor) -> None:
        Delete all products in the 'Stationery' category.

---

PART 4 (HARD): More Complex Queries

    get_category_stats(cursor) -> list[tuple]:
        Return (category, count, avg_price) for each category.
        Order by count descending.
        Round avg_price to 2 decimal places.

    get_most_expensive_per_category(cursor) -> list[tuple]:
        Return (category, name, price) for the most expensive product
        in each category.

ESTIMATED TIME: 30-45 minutes
"""

import sqlite3


# ============================================
# PART 1: Create and Insert
# ============================================

def create_products_table(cursor):
    """Create the products table."""
    # YOUR CODE HERE
    pass


def insert_sample_products(cursor):
    """Insert the sample products."""
    # YOUR CODE HERE
    pass


# ============================================
# PART 2: SELECT Queries
# ============================================

def get_all_products(cursor) -> list[tuple]:
    """Return all products."""
    # YOUR CODE HERE
    pass


def get_electronics(cursor) -> list[tuple]:
    """Return all Electronics products."""
    # YOUR CODE HERE
    pass


def get_cheap_products(cursor) -> list[tuple]:
    """Return products under 30, ordered by price ascending."""
    # YOUR CODE HERE
    pass


def get_product_names_and_prices(cursor) -> list[tuple]:
    """Return only name and price for all products."""
    # YOUR CODE HERE
    pass


def get_in_stock_count(cursor) -> int:
    """Return count of in-stock products."""
    # YOUR CODE HERE
    pass


# ============================================
# PART 3: UPDATE and DELETE
# ============================================

def increase_book_prices(cursor) -> None:
    """Increase all Book prices by 5.00."""
    # YOUR CODE HERE
    pass


def mark_out_of_stock(cursor, product_name: str) -> None:
    """Set in_stock to 0 for given product."""
    # YOUR CODE HERE
    pass


def delete_stationery(cursor) -> None:
    """Delete all Stationery products."""
    # YOUR CODE HERE
    pass


# ============================================
# PART 4 (HARD): Complex Queries
# ============================================

def get_category_stats(cursor) -> list[tuple]:
    """Return (category, count, avg_price) ordered by count desc."""
    # YOUR CODE HERE
    pass


def get_most_expensive_per_category(cursor) -> list[tuple]:
    """Return (category, name, price) for most expensive in each category."""
    # YOUR CODE HERE
    pass


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    # Create in-memory database for testing
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # ==========================================
    # PART 1 TESTS
    # ==========================================
    print("\n=== Test 1: Create Table and Insert ===")
    try:
        create_products_table(cursor)
        insert_sample_products(cursor)
        conn.commit()

        cursor.execute("SELECT COUNT(*) FROM products")
        count = cursor.fetchone()[0]
        assert count == 8, f"Expected 8 products, got {count}"

        print("  Table created with 8 products")
        print("Test 1 PASSED!")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")
    except Exception as e:
        print(f"Test 1 ERROR: {e}")

    # ==========================================
    # PART 2 TESTS
    # ==========================================
    print("\n=== Test 2: Get All Products ===")
    try:
        results = get_all_products(cursor)
        assert len(results) == 8

        print(f"  Retrieved {len(results)} products")
        print("Test 2 PASSED!")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 ERROR: {e}")

    print("\n=== Test 3: Get Electronics ===")
    try:
        results = get_electronics(cursor)
        assert len(results) == 4
        assert all(r[3] == 'Electronics' for r in results)

        print(f"  Found {len(results)} electronics")
        print("Test 3 PASSED!")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 ERROR: {e}")

    print("\n=== Test 4: Cheap Products (< 30) ===")
    try:
        results = get_cheap_products(cursor)
        assert all(r[2] < 30 for r in results)
        prices = [r[2] for r in results]
        assert prices == sorted(prices), "Should be ordered by price ascending"

        print(f"  Found {len(results)} cheap products, sorted by price")
        print("Test 4 PASSED!")
    except AssertionError as e:
        print(f"Test 4 FAILED: {e}")
    except Exception as e:
        print(f"Test 4 ERROR: {e}")

    print("\n=== Test 5: Names and Prices Only ===")
    try:
        results = get_product_names_and_prices(cursor)
        assert len(results) == 8
        assert len(results[0]) == 2, "Should only return 2 columns"

        print("  Names and prices returned correctly")
        print("Test 5 PASSED!")
    except AssertionError as e:
        print(f"Test 5 FAILED: {e}")
    except Exception as e:
        print(f"Test 5 ERROR: {e}")

    print("\n=== Test 6: In Stock Count ===")
    try:
        count = get_in_stock_count(cursor)
        assert count == 7, f"Expected 7 in stock, got {count}"

        print(f"  {count} products in stock")
        print("Test 6 PASSED!")
    except AssertionError as e:
        print(f"Test 6 FAILED: {e}")
    except Exception as e:
        print(f"Test 6 ERROR: {e}")

    # ==========================================
    # PART 3 TESTS
    # ==========================================
    print("\n=== Test 7: Increase Book Prices ===")
    try:
        increase_book_prices(cursor)
        conn.commit()

        cursor.execute("SELECT price FROM products WHERE name = 'Python Book'")
        price = cursor.fetchone()[0]
        assert abs(price - 34.99) < 0.01, f"Expected 34.99, got {price}"

        cursor.execute("SELECT price FROM products WHERE name = 'SQL Guide'")
        price = cursor.fetchone()[0]
        assert abs(price - 39.99) < 0.01, f"Expected 39.99, got {price}"

        print("  Book prices increased by 5.00")
        print("Test 7 PASSED!")
    except AssertionError as e:
        print(f"Test 7 FAILED: {e}")
    except Exception as e:
        print(f"Test 7 ERROR: {e}")

    print("\n=== Test 8: Mark Out of Stock ===")
    try:
        mark_out_of_stock(cursor, "Laptop")
        conn.commit()

        cursor.execute("SELECT in_stock FROM products WHERE name = 'Laptop'")
        stock = cursor.fetchone()[0]
        assert stock == 0, f"Expected 0, got {stock}"

        print("  Laptop marked out of stock")
        print("Test 8 PASSED!")
    except AssertionError as e:
        print(f"Test 8 FAILED: {e}")
    except Exception as e:
        print(f"Test 8 ERROR: {e}")

    print("\n=== Test 9: Delete Stationery ===")
    try:
        delete_stationery(cursor)
        conn.commit()

        cursor.execute("SELECT COUNT(*) FROM products WHERE category = 'Stationery'")
        count = cursor.fetchone()[0]
        assert count == 0, f"Expected 0 stationery, got {count}"

        cursor.execute("SELECT COUNT(*) FROM products")
        total = cursor.fetchone()[0]
        assert total == 7, f"Expected 7 total products, got {total}"

        print("  Stationery deleted")
        print("Test 9 PASSED!")
    except AssertionError as e:
        print(f"Test 9 FAILED: {e}")
    except Exception as e:
        print(f"Test 9 ERROR: {e}")

    # ==========================================
    # PART 4 TESTS (HARD): Uncomment when ready
    # ==========================================

    # # Reset data for part 4 tests
    # conn.close()
    # conn = sqlite3.connect(":memory:")
    # cursor = conn.cursor()
    # create_products_table(cursor)
    # insert_sample_products(cursor)
    # conn.commit()

    # print("\n=== Test 10: Category Stats ===")
    # try:
    #     results = get_category_stats(cursor)
    #     # Electronics has 4 products (most)
    #     assert results[0][0] == 'Electronics'
    #     assert results[0][1] == 4
    #
    #     print(f"  Category stats:")
    #     for cat, count, avg in results:
    #         print(f"    {cat}: {count} products, avg ${avg}")
    #     print("Test 10 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 10 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 10 ERROR: {e}")

    # print("\n=== Test 11: Most Expensive Per Category ===")
    # try:
    #     results = get_most_expensive_per_category(cursor)
    #     result_dict = {r[0]: (r[1], r[2]) for r in results}
    #
    #     assert result_dict['Electronics'][0] == 'Laptop'
    #     assert result_dict['Electronics'][1] == 999.99
    #     assert result_dict['Books'][0] == 'SQL Guide'
    #
    #     print(f"  Most expensive per category:")
    #     for cat, name, price in results:
    #         print(f"    {cat}: {name} (${price})")
    #     print("Test 11 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 11 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 11 ERROR: {e}")

    conn.close()

    print("\n" + "=" * 60)
    print("SQL BASICS KEY LESSONS")
    print("=" * 60)
    print("""
1. CRUD: CREATE, READ (SELECT), UPDATE, DELETE
2. WHERE filters rows, ORDER BY sorts, LIMIT caps results
3. PRIMARY KEY uniquely identifies each row
4. NOT NULL, UNIQUE, DEFAULT are column constraints
5. Always use parameterised queries (?) to prevent SQL injection
6. GROUP BY + aggregate functions for summary statistics
7. SQLite is built into Python - great for learning and prototyping
""")
    print("=" * 60)
