"""
Exercise 8.6: Builder Pattern

BUILDER PATTERN (Creational)
============================

Separate the construction of a complex object from its representation,
so the same construction process can create different representations.

===================================
WHY USE BUILDER?
===================================

Without builder (telescoping constructor):
    pizza = Pizza("large", True, True, False, True, False, True, "thin")
    # What do all these booleans mean?!

With builder (readable step-by-step):
    pizza = (PizzaBuilder()
        .set_size("large")
        .add_cheese()
        .add_pepperoni()
        .add_mushrooms()
        .set_crust("thin")
        .build())
    # Crystal clear what we're building!

===================================
METHOD CHAINING
===================================

Each builder method returns `self`, so you can chain calls:

    class Builder:
        def set_x(self, x):
            self.x = x
            return self     # <- This enables chaining!

        def set_y(self, y):
            self.y = y
            return self

    result = Builder().set_x(1).set_y(2)  # Chained!

===================================
EXERCISE
===================================

PART 1: Pizza Builder

    class Pizza:
        __init__(self, size, crust, toppings, cheese, sauce):
            Store all attributes.

        __repr__(self) -> str:
            Return a multi-line string:
            "Pizza(size='{size}', crust='{crust}', sauce='{sauce}',
             cheese={cheese}, toppings={toppings})"

    class PizzaBuilder:
        __init__:
            Set defaults: size="medium", crust="regular",
            toppings=[], cheese=True, sauce="tomato"

        set_size(self, size: str) -> 'PizzaBuilder':
            Set size. Return self.

        set_crust(self, crust: str) -> 'PizzaBuilder':
            Set crust. Return self.

        add_topping(self, topping: str) -> 'PizzaBuilder':
            Append topping to list. Return self.

        set_cheese(self, cheese: bool) -> 'PizzaBuilder':
            Set cheese. Return self.

        set_sauce(self, sauce: str) -> 'PizzaBuilder':
            Set sauce. Return self.

        build(self) -> Pizza:
            Create and return a Pizza with the current settings.
            IMPORTANT: Pass a COPY of the toppings list.

---

PART 2: Query Builder

    class Query:
        __init__(self, sql: str):
            Store the SQL string.

        __repr__(self) -> str:
            Return the SQL string.

    class QueryBuilder:
        Build a SQL SELECT query step by step.

        __init__:
            Set _table=None, _columns=["*"], _conditions=[],
            _order_by=None, _limit=None

        table(self, table_name: str) -> 'QueryBuilder':
            Set the table. Return self.

        select(self, *columns: str) -> 'QueryBuilder':
            Set the columns to select. Return self.

        where(self, condition: str) -> 'QueryBuilder':
            Add a WHERE condition. Return self.

        order_by(self, column: str, direction: str = "ASC") -> 'QueryBuilder':
            Set ORDER BY. Return self.

        limit(self, count: int) -> 'QueryBuilder':
            Set LIMIT. Return self.

        build(self) -> Query:
            Build and return the Query.
            Raise ValueError if no table set.

            Format: "SELECT {columns} FROM {table}"
            Add " WHERE {cond1} AND {cond2}" if conditions exist.
            Add " ORDER BY {column} {direction}" if set.
            Add " LIMIT {count}" if set.

---

PART 3 (HARD): HTML Builder

    class HTMLElement:
        __init__(self, tag: str, content: str = "", children: list = None,
                 attributes: dict = None):
            Store all. Default children to [], attributes to {}.

        render(self, indent: int = 0) -> str:
            Render the element as HTML string with indentation.
            - If has children, render each child indented by (indent + 2).
            - If has content (no children), render inline: <tag>content</tag>
            - Include attributes in opening tag: <tag key="value">

    class HTMLBuilder:
        __init__(self, root_tag: str):
            Set _tag=root_tag, _content="", _children=[], _attributes={}

        content(self, text: str) -> 'HTMLBuilder':
            Set content. Return self.

        attribute(self, key: str, value: str) -> 'HTMLBuilder':
            Add an attribute. Return self.

        child(self, element: HTMLElement) -> 'HTMLBuilder':
            Add a child element. Return self.

        build(self) -> HTMLElement:
            Return the HTMLElement.

ESTIMATED TIME: 30-45 minutes
"""


# ============================================
# PART 1: Pizza Builder
# ============================================

# YOUR CODE HERE


# ============================================
# PART 2: Query Builder
# ============================================

# YOUR CODE HERE


# ============================================
# PART 3 (HARD): HTML Builder
# ============================================

# YOUR CODE HERE


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    # ==========================================
    # PART 1 TESTS: Pizza Builder
    # ==========================================
    print("\n=== Test 1: Default Pizza ===")
    try:
        pizza = PizzaBuilder().build()
        assert pizza.size == "medium"
        assert pizza.crust == "regular"
        assert pizza.toppings == []
        assert pizza.cheese == True
        assert pizza.sauce == "tomato"

        print(f"  Default: size={pizza.size}, crust={pizza.crust}")
        print("Test 1 PASSED!")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")
    except Exception as e:
        print(f"Test 1 ERROR: {e}")

    print("\n=== Test 2: Custom Pizza with Chaining ===")
    try:
        pizza = (PizzaBuilder()
            .set_size("large")
            .set_crust("thin")
            .add_topping("pepperoni")
            .add_topping("mushrooms")
            .add_topping("olives")
            .set_sauce("bbq")
            .build())

        assert pizza.size == "large"
        assert pizza.crust == "thin"
        assert pizza.toppings == ["pepperoni", "mushrooms", "olives"]
        assert pizza.sauce == "bbq"
        assert pizza.cheese == True  # Default

        print(f"  {pizza}")
        print("Test 2 PASSED!")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 ERROR: {e}")

    print("\n=== Test 3: Builder Independence ===")
    try:
        # Two pizzas from different builders should be independent
        pizza1 = (PizzaBuilder()
            .add_topping("ham")
            .build())

        pizza2 = (PizzaBuilder()
            .add_topping("pineapple")
            .build())

        assert pizza1.toppings == ["ham"]
        assert pizza2.toppings == ["pineapple"]
        assert pizza1.toppings is not pizza2.toppings

        print("  Builders are independent - no shared state")
        print("Test 3 PASSED!")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 ERROR: {e}")

    # ==========================================
    # PART 2 TESTS: Query Builder
    # ==========================================
    print("\n=== Test 4: Simple Query ===")
    try:
        query = (QueryBuilder()
            .table("users")
            .build())

        assert str(query) == "SELECT * FROM users"

        print(f"  {query}")
        print("Test 4 PASSED!")
    except AssertionError as e:
        print(f"Test 4 FAILED: {e}")
    except Exception as e:
        print(f"Test 4 ERROR: {e}")

    print("\n=== Test 5: Complex Query ===")
    try:
        query = (QueryBuilder()
            .table("products")
            .select("name", "price")
            .where("price > 10")
            .where("category = 'electronics'")
            .order_by("price", "DESC")
            .limit(5)
            .build())

        expected = ("SELECT name, price FROM products "
                    "WHERE price > 10 AND category = 'electronics' "
                    "ORDER BY price DESC LIMIT 5")
        assert str(query) == expected, f"Got: {query}"

        print(f"  {query}")
        print("Test 5 PASSED!")
    except AssertionError as e:
        print(f"Test 5 FAILED: {e}")
    except Exception as e:
        print(f"Test 5 ERROR: {e}")

    print("\n=== Test 6: Query Builder Validation ===")
    try:
        try:
            QueryBuilder().select("name").build()
            assert False, "Should raise ValueError"
        except ValueError:
            pass

        print("  No table -> ValueError raised correctly")
        print("Test 6 PASSED!")
    except AssertionError as e:
        print(f"Test 6 FAILED: {e}")
    except Exception as e:
        print(f"Test 6 ERROR: {e}")

    # ==========================================
    # PART 3 TESTS (HARD): Uncomment when ready
    # ==========================================

    # print("\n=== Test 7: HTML Element ===")
    # try:
    #     p = HTMLElement("p", "Hello World")
    #     assert p.render() == "<p>Hello World</p>"
    #
    #     link = HTMLElement("a", "Click me", attributes={"href": "https://example.com"})
    #     assert link.render() == '<a href="https://example.com">Click me</a>'
    #
    #     print(f"  {p.render()}")
    #     print(f"  {link.render()}")
    #     print("Test 7 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 7 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 7 ERROR: {e}")

    # print("\n=== Test 8: HTML Builder with Nesting ===")
    # try:
    #     heading = HTMLBuilder("h1").content("My Page").build()
    #     para = HTMLBuilder("p").content("Welcome!").build()
    #
    #     div = (HTMLBuilder("div")
    #         .attribute("class", "container")
    #         .child(heading)
    #         .child(para)
    #         .build())
    #
    #     expected = (
    #         '<div class="container">\n'
    #         '  <h1>My Page</h1>\n'
    #         '  <p>Welcome!</p>\n'
    #         '</div>'
    #     )
    #     result = div.render()
    #     assert result == expected, f"Got:\n{result}"
    #
    #     print(f"  Rendered:\n{result}")
    #     print("Test 8 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 8 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 8 ERROR: {e}")

    print("\n" + "=" * 60)
    print("BUILDER PATTERN KEY LESSONS")
    print("=" * 60)
    print("""
1. Builder separates construction from representation
2. Method chaining (return self) makes code readable
3. build() creates the final object - validates and returns
4. Avoids "telescoping constructor" with many parameters
5. Each build() call should produce an independent object
6. Builder is great for objects with many optional parameters
7. Real-world: SQL query builders, HTTP request builders, UI builders
""")
    print("=" * 60)
