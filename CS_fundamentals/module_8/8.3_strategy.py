"""
Exercise 8.3: Strategy Pattern

STRATEGY PATTERN (Behavioural)
==============================

Define a family of algorithms, put each in its own class, and make them
interchangeable. The client picks a strategy at runtime without changing
the code that uses it.

===================================
WHY USE STRATEGY?
===================================

Without strategy:
    def calculate_price(price, discount_type):
        if discount_type == "percentage":
            return price * 0.9
        elif discount_type == "fixed":
            return price - 10
        elif discount_type == "buy_one_get_one":
            return price / 2
        # Adding new discount = modifying this function (violates OCP!)

With strategy:
    class PercentageDiscount:
        def apply(self, price):
            return price * 0.9

    class FixedDiscount:
        def apply(self, price):
            return price - 10

    # Client just uses whichever strategy it's given
    def calculate_price(price, strategy):
        return strategy.apply(price)

    # Adding new discount = new class. Existing code untouched.

===================================
STRATEGY vs IF/ELIF
===================================

If/elif: Logic is INSIDE one function. Adding behaviour = editing it.
Strategy: Logic is in SEPARATE classes. Adding behaviour = new class.

Strategy is perfect when you have multiple ways to do the same thing
and want to switch between them at runtime.

===================================
EXERCISE
===================================

PART 1: Sorting Strategies

Create an ABC and concrete sorting strategies:

    class SortStrategy(ABC):
        @abstractmethod
        def sort(self, data: list) -> list:
            Return a NEW sorted list (don't modify the original).

        @abstractmethod
        def name(self) -> str:
            Return the name of the algorithm.

    class BubbleSortStrategy(SortStrategy):
        Implement bubble sort.
        name: "Bubble Sort"

    class InsertionSortStrategy(SortStrategy):
        Implement insertion sort.
        name: "Insertion Sort"

    class MergeSortStrategy(SortStrategy):
        Implement merge sort.
        name: "Merge Sort"

---

PART 2: Sorter (Context Class)

    class Sorter:
        The "context" that uses a sorting strategy.

        __init__(self, strategy: SortStrategy):
            Store the strategy.

        set_strategy(self, strategy: SortStrategy) -> None:
            Change the strategy at runtime.

        sort(self, data: list) -> list:
            Delegate to the current strategy's sort method.

        get_strategy_name(self) -> str:
            Return the current strategy's name.

---

PART 3 (HARD): Text Formatter Strategies

    class TextFormatter(ABC):
        @abstractmethod
        def format(self, text: str) -> str: ...

    class UpperCaseFormatter(TextFormatter):
        Return text in UPPER CASE.

    class TitleCaseFormatter(TextFormatter):
        Return text in Title Case.

    class SnakeCaseFormatter(TextFormatter):
        Convert "hello world example" -> "hello_world_example"
        (lowercase, spaces replaced with underscores)

    class Document:
        __init__(self, content: str, formatter: TextFormatter)

        set_formatter(self, formatter: TextFormatter) -> None

        render(self) -> str:
            Return content formatted by the current formatter.

ESTIMATED TIME: 30-45 minutes
"""

from abc import ABC, abstractmethod


# ============================================
# PART 1: Sorting Strategies
# ============================================

# YOUR CODE HERE


# ============================================
# PART 2: Sorter (Context Class)
# ============================================

# YOUR CODE HERE


# ============================================
# PART 3 (HARD): Text Formatter Strategies
# ============================================

# YOUR CODE HERE


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    # ==========================================
    # PART 1 TESTS: Sorting Strategies
    # ==========================================
    print("\n=== Test 1: Bubble Sort Strategy ===")
    try:
        bs = BubbleSortStrategy()
        original = [5, 2, 8, 1, 9, 3]
        result = bs.sort(original)

        assert result == [1, 2, 3, 5, 8, 9]
        assert original == [5, 2, 8, 1, 9, 3], "Original should not be modified"
        assert bs.name() == "Bubble Sort"

        print(f"  {bs.name()}: {original} -> {result}")
        print("Test 1 PASSED!")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")
    except Exception as e:
        print(f"Test 1 ERROR: {e}")

    print("\n=== Test 2: Insertion Sort Strategy ===")
    try:
        ins = InsertionSortStrategy()
        original = [7, 3, 5, 1, 4]
        result = ins.sort(original)

        assert result == [1, 3, 4, 5, 7]
        assert original == [7, 3, 5, 1, 4], "Original should not be modified"
        assert ins.name() == "Insertion Sort"

        print(f"  {ins.name()}: {original} -> {result}")
        print("Test 2 PASSED!")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 ERROR: {e}")

    print("\n=== Test 3: Merge Sort Strategy ===")
    try:
        ms = MergeSortStrategy()
        original = [6, 2, 9, 1, 5, 8]
        result = ms.sort(original)

        assert result == [1, 2, 5, 6, 8, 9]
        assert original == [6, 2, 9, 1, 5, 8], "Original should not be modified"
        assert ms.name() == "Merge Sort"

        print(f"  {ms.name()}: {original} -> {result}")
        print("Test 3 PASSED!")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 ERROR: {e}")

    # ==========================================
    # PART 2 TESTS: Sorter Context
    # ==========================================
    print("\n=== Test 4: Sorter with Strategy ===")
    try:
        sorter = Sorter(BubbleSortStrategy())
        assert sorter.get_strategy_name() == "Bubble Sort"

        data = [4, 2, 7, 1]
        result = sorter.sort(data)
        assert result == [1, 2, 4, 7]

        print(f"  Sorted with {sorter.get_strategy_name()}: {result}")
        print("Test 4 PASSED!")
    except AssertionError as e:
        print(f"Test 4 FAILED: {e}")
    except Exception as e:
        print(f"Test 4 ERROR: {e}")

    print("\n=== Test 5: Switch Strategy at Runtime ===")
    try:
        sorter = Sorter(BubbleSortStrategy())
        data = [9, 1, 5, 3]

        # Sort with bubble sort
        result1 = sorter.sort(data)
        assert sorter.get_strategy_name() == "Bubble Sort"

        # Switch to merge sort
        sorter.set_strategy(MergeSortStrategy())
        result2 = sorter.sort(data)
        assert sorter.get_strategy_name() == "Merge Sort"

        # Both should give same result
        assert result1 == result2 == [1, 3, 5, 9]

        print("  Switched strategy at runtime - same result!")
        print("Test 5 PASSED!")
    except AssertionError as e:
        print(f"Test 5 FAILED: {e}")
    except Exception as e:
        print(f"Test 5 ERROR: {e}")

    print("\n=== Test 6: Edge Cases ===")
    try:
        sorter = Sorter(InsertionSortStrategy())

        assert sorter.sort([]) == []
        assert sorter.sort([1]) == [1]
        assert sorter.sort([1, 1, 1]) == [1, 1, 1]
        assert sorter.sort([1, 2, 3]) == [1, 2, 3]  # Already sorted

        print("  Edge cases handled correctly")
        print("Test 6 PASSED!")
    except AssertionError as e:
        print(f"Test 6 FAILED: {e}")
    except Exception as e:
        print(f"Test 6 ERROR: {e}")

    # ==========================================
    # PART 3 TESTS (HARD): Uncomment when ready
    # ==========================================

    # print("\n=== Test 7: Text Formatters ===")
    # try:
    #     upper = UpperCaseFormatter()
    #     assert upper.format("hello world") == "HELLO WORLD"
    #
    #     title = TitleCaseFormatter()
    #     assert title.format("hello world example") == "Hello World Example"
    #
    #     snake = SnakeCaseFormatter()
    #     assert snake.format("Hello World Example") == "hello_world_example"
    #
    #     print("  All formatters work correctly")
    #     print("Test 7 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 7 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 7 ERROR: {e}")

    # print("\n=== Test 8: Document with Formatter ===")
    # try:
    #     doc = Document("hello world example", UpperCaseFormatter())
    #     assert doc.render() == "HELLO WORLD EXAMPLE"
    #
    #     doc.set_formatter(TitleCaseFormatter())
    #     assert doc.render() == "Hello World Example"
    #
    #     doc.set_formatter(SnakeCaseFormatter())
    #     assert doc.render() == "hello_world_example"
    #
    #     print("  Document renders with different formatters")
    #     print("  THIS is Strategy: same content, different behaviour!")
    #     print("Test 8 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 8 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 8 ERROR: {e}")

    print("\n" + "=" * 60)
    print("STRATEGY PATTERN KEY LESSONS")
    print("=" * 60)
    print("""
1. Strategy encapsulates algorithms in separate classes
2. The context class delegates to whatever strategy it holds
3. Strategies can be swapped at runtime (set_strategy)
4. All strategies share the same interface (ABC)
5. Eliminates if/elif chains for choosing behaviour
6. New behaviours = new classes, no existing code changes (OCP)
7. Strategy + Factory = powerful combo (factory picks the strategy)
""")
    print("=" * 60)
