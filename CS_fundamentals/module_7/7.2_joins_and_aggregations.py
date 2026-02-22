"""
Exercise 7.2: JOINs and Aggregations

JOINS
=====

JOINs combine rows from two or more tables based on a related column.

===================================
TYPES OF JOINS
===================================

    INNER JOIN: Only rows that match in BOTH tables
    LEFT JOIN:  ALL rows from left table, matched rows from right (NULL if no match)
    RIGHT JOIN: ALL rows from right table, matched rows from left (NULL if no match)

    (SQLite doesn't support RIGHT JOIN or FULL OUTER JOIN natively,
     but INNER JOIN and LEFT JOIN cover most real-world needs.)

===================================
EXAMPLE
===================================

    orders table:              customers table:
    id | customer_id | total   id | name
    1  | 1           | 50.00   1  | Alice
    2  | 2           | 30.00   2  | Bob
    3  | 1           | 20.00   3  | Charlie (no orders)

    INNER JOIN (only customers WITH orders):
    SELECT c.name, o.total
    FROM orders o
    INNER JOIN customers c ON o.customer_id = c.id;
    -> Alice 50.00, Bob 30.00, Alice 20.00

    LEFT JOIN customers (ALL customers, even without orders):
    SELECT c.name, o.total
    FROM customers c
    LEFT JOIN orders o ON c.id = o.customer_id;
    -> Alice 50.00, Alice 20.00, Bob 30.00, Charlie NULL

===================================
AGGREGATE FUNCTIONS
===================================

    COUNT(*) - Number of rows
    SUM(col) - Total of column
    AVG(col) - Average of column
    MAX(col) - Maximum value
    MIN(col) - Minimum value

    Used with GROUP BY to get per-group summaries:

    SELECT category, COUNT(*), AVG(price)
    FROM products
    GROUP BY category
    HAVING COUNT(*) > 1;   -- HAVING filters AFTER grouping

===================================
EXERCISE
===================================

The test setup creates three tables:
- customers (id, name, email, city)
- orders (id, customer_id, total, order_date)
- order_items (id, order_id, product_name, quantity, price)

Complete each function with the correct SQL query.

PART 1: Basic JOINs

    get_orders_with_customer_names(cursor) -> list[tuple]:
        Return (customer_name, order_total, order_date) for all orders.
        Use INNER JOIN.

    get_all_customers_with_orders(cursor) -> list[tuple]:
        Return (customer_name, order_total) for ALL customers.
        Customers with no orders should show NULL for total.
        Use LEFT JOIN.

    get_customers_without_orders(cursor) -> list[tuple]:
        Return (customer_name, email) for customers who have NO orders.
        Hint: LEFT JOIN where order id IS NULL.

---

PART 2: Aggregations

    get_total_spent_per_customer(cursor) -> list[tuple]:
        Return (customer_name, total_spent) for each customer.
        Order by total_spent descending.
        Only include customers who have placed orders.

    get_order_count_per_city(cursor) -> list[tuple]:
        Return (city, order_count) ordered by order_count descending.

    get_average_order_value(cursor) -> float:
        Return the average order total across all orders.
        Round to 2 decimal places.

---

PART 3 (HARD): Complex Queries

    get_top_spender(cursor) -> tuple:
        Return (customer_name, total_spent) for the customer who spent the most.

    get_order_details(cursor) -> list[tuple]:
        Return (customer_name, order_date, product_name, quantity, line_total)
        where line_total = quantity * price.
        Order by customer_name, then order_date.

    get_customers_above_average(cursor) -> list[tuple]:
        Return (customer_name, total_spent) for customers whose total spending
        is ABOVE the average total spending per customer.
        Hint: Use a subquery to calculate the average.

ESTIMATED TIME: 30-45 minutes
"""

import sqlite3


def setup_database(cursor):
    """Create tables and insert sample data. DO NOT MODIFY."""
    cursor.executescript("""
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            city TEXT NOT NULL
        );

        CREATE TABLE orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            total REAL NOT NULL,
            order_date TEXT NOT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        );

        CREATE TABLE order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(id)
        );

        INSERT INTO customers (name, email, city) VALUES
            ('Alice', 'alice@mail.com', 'London'),
            ('Bob', 'bob@mail.com', 'Manchester'),
            ('Charlie', 'charlie@mail.com', 'London'),
            ('Diana', 'diana@mail.com', 'Edinburgh'),
            ('Eve', 'eve@mail.com', 'Manchester');

        INSERT INTO orders (customer_id, total, order_date) VALUES
            (1, 150.00, '2024-01-15'),
            (1, 75.50, '2024-02-20'),
            (2, 200.00, '2024-01-20'),
            (3, 50.00, '2024-03-01'),
            (2, 120.00, '2024-03-15');

        INSERT INTO order_items (order_id, product_name, quantity, price) VALUES
            (1, 'Laptop Stand', 1, 100.00),
            (1, 'USB Cable', 2, 25.00),
            (2, 'Mouse Pad', 1, 25.50),
            (2, 'Pen Set', 5, 10.00),
            (3, 'Monitor', 1, 200.00),
            (4, 'Notebook', 10, 5.00),
            (5, 'Keyboard', 1, 80.00),
            (5, 'Webcam', 1, 40.00);
    """)


# ============================================
# PART 1: Basic JOINs
# ============================================

def get_orders_with_customer_names(cursor) -> list[tuple]:
    """Return (customer_name, order_total, order_date) for all orders."""
    # YOUR CODE HERE
    pass


def get_all_customers_with_orders(cursor) -> list[tuple]:
    """Return (customer_name, order_total) for ALL customers (LEFT JOIN)."""
    # YOUR CODE HERE
    pass


def get_customers_without_orders(cursor) -> list[tuple]:
    """Return (customer_name, email) for customers with no orders."""
    # YOUR CODE HERE
    pass


# ============================================
# PART 2: Aggregations
# ============================================

def get_total_spent_per_customer(cursor) -> list[tuple]:
    """Return (customer_name, total_spent) ordered by total desc."""
    # YOUR CODE HERE
    pass


def get_order_count_per_city(cursor) -> list[tuple]:
    """Return (city, order_count) ordered by count desc."""
    # YOUR CODE HERE
    pass


def get_average_order_value(cursor) -> float:
    """Return average order total, rounded to 2 decimal places."""
    # YOUR CODE HERE
    pass


# ============================================
# PART 3 (HARD): Complex Queries
# ============================================

def get_top_spender(cursor) -> tuple:
    """Return (customer_name, total_spent) for highest spender."""
    # YOUR CODE HERE
    pass


def get_order_details(cursor) -> list[tuple]:
    """Return (customer_name, order_date, product_name, quantity, line_total)."""
    # YOUR CODE HERE
    pass


def get_customers_above_average(cursor) -> list[tuple]:
    """Return customers whose total spending is above average."""
    # YOUR CODE HERE
    pass


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    setup_database(cursor)
    conn.commit()

    # ==========================================
    # PART 1 TESTS
    # ==========================================
    print("\n=== Test 1: Orders with Customer Names (INNER JOIN) ===")
    try:
        results = get_orders_with_customer_names(cursor)
        assert len(results) == 5, f"Expected 5 orders, got {len(results)}"
        names = [r[0] for r in results]
        assert 'Alice' in names
        assert 'Bob' in names

        print(f"  {len(results)} orders with customer names")
        for name, total, date in results:
            print(f"    {name}: ${total} on {date}")
        print("Test 1 PASSED!")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")
    except Exception as e:
        print(f"Test 1 ERROR: {e}")

    print("\n=== Test 2: All Customers with Orders (LEFT JOIN) ===")
    try:
        results = get_all_customers_with_orders(cursor)
        names = [r[0] for r in results]
        assert 'Diana' in names, "Diana (no orders) should appear"
        assert 'Eve' in names, "Eve (no orders) should appear"

        # Diana and Eve should have NULL totals
        diana_rows = [r for r in results if r[0] == 'Diana']
        assert diana_rows[0][1] is None, "Diana should have NULL total"

        print(f"  All {len(results)} customer rows (including those without orders)")
        print("Test 2 PASSED!")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 ERROR: {e}")

    print("\n=== Test 3: Customers Without Orders ===")
    try:
        results = get_customers_without_orders(cursor)
        assert len(results) == 2, f"Expected 2, got {len(results)}"
        names = [r[0] for r in results]
        assert 'Diana' in names
        assert 'Eve' in names

        print(f"  {len(results)} customers without orders: {names}")
        print("Test 3 PASSED!")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 ERROR: {e}")

    # ==========================================
    # PART 2 TESTS
    # ==========================================
    print("\n=== Test 4: Total Spent Per Customer ===")
    try:
        results = get_total_spent_per_customer(cursor)
        assert len(results) == 3, f"Expected 3 customers with orders, got {len(results)}"

        # Bob spent most: 200 + 120 = 320
        assert results[0][0] == 'Bob'
        assert abs(results[0][1] - 320.00) < 0.01

        print(f"  Spending per customer:")
        for name, total in results:
            print(f"    {name}: ${total}")
        print("Test 4 PASSED!")
    except AssertionError as e:
        print(f"Test 4 FAILED: {e}")
    except Exception as e:
        print(f"Test 4 ERROR: {e}")

    print("\n=== Test 5: Order Count Per City ===")
    try:
        results = get_order_count_per_city(cursor)
        result_dict = {r[0]: r[1] for r in results}

        # London: Alice (2) + Charlie (1) = 3
        # Manchester: Bob (2)
        assert result_dict.get('London') == 3
        assert result_dict.get('Manchester') == 2

        print(f"  Orders per city: {result_dict}")
        print("Test 5 PASSED!")
    except AssertionError as e:
        print(f"Test 5 FAILED: {e}")
    except Exception as e:
        print(f"Test 5 ERROR: {e}")

    print("\n=== Test 6: Average Order Value ===")
    try:
        avg = get_average_order_value(cursor)
        # (150 + 75.5 + 200 + 50 + 120) / 5 = 119.1
        assert abs(avg - 119.10) < 0.01, f"Expected 119.10, got {avg}"

        print(f"  Average order value: ${avg}")
        print("Test 6 PASSED!")
    except AssertionError as e:
        print(f"Test 6 FAILED: {e}")
    except Exception as e:
        print(f"Test 6 ERROR: {e}")

    # ==========================================
    # PART 3 TESTS (HARD): Uncomment when ready
    # ==========================================

    # print("\n=== Test 7: Top Spender ===")
    # try:
    #     name, total = get_top_spender(cursor)
    #     assert name == 'Bob', f"Expected Bob, got {name}"
    #     assert abs(total - 320.00) < 0.01
    #
    #     print(f"  Top spender: {name} (${total})")
    #     print("Test 7 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 7 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 7 ERROR: {e}")

    # print("\n=== Test 8: Order Details ===")
    # try:
    #     results = get_order_details(cursor)
    #     assert len(results) == 8, f"Expected 8 line items, got {len(results)}"
    #
    #     # Check a line total calculation
    #     usb_cable = [r for r in results if r[2] == 'USB Cable'][0]
    #     assert abs(usb_cable[4] - 50.00) < 0.01, "USB Cable: 2 * 25.00 = 50.00"
    #
    #     print(f"  {len(results)} order detail rows")
    #     print("Test 8 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 8 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 8 ERROR: {e}")

    # print("\n=== Test 9: Customers Above Average Spending ===")
    # try:
    #     results = get_customers_above_average(cursor)
    #     names = [r[0] for r in results]
    #     # Average spending per customer: (225.5 + 320 + 50) / 3 = 198.5
    #     # Bob (320) and Alice (225.5) are above average
    #     assert 'Bob' in names
    #     assert 'Alice' in names
    #     assert 'Charlie' not in names
    #
    #     print(f"  Above-average spenders: {names}")
    #     print("Test 9 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 9 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 9 ERROR: {e}")

    conn.close()

    print("\n" + "=" * 60)
    print("JOINS & AGGREGATIONS KEY LESSONS")
    print("=" * 60)
    print("""
1. INNER JOIN: Only matching rows from both tables
2. LEFT JOIN: All from left table, NULL for non-matching right
3. GROUP BY: Group rows for aggregate calculations
4. HAVING: Filter AFTER grouping (WHERE filters BEFORE)
5. Aggregate functions: COUNT, SUM, AVG, MAX, MIN
6. Foreign keys link tables together
7. Subqueries let you use one query's result in another
""")
    print("=" * 60)
