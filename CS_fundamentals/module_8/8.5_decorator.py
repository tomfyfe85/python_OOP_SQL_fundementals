"""
Exercise 8.5: Decorator Pattern

DECORATOR PATTERN (Structural)
==============================

Attach additional responsibilities to an object dynamically. Decorators
provide a flexible alternative to subclassing for extending functionality.

===================================
WHY USE DECORATOR?
===================================

Problem: You have a base object and want to add optional features.

Without decorator (subclass explosion):
    class Coffee
    class CoffeeWithMilk(Coffee)
    class CoffeeWithSugar(Coffee)
    class CoffeeWithMilkAndSugar(Coffee)
    class CoffeeWithMilkAndSugarAndWhip(Coffee)
    # Every combination = new class!

With decorator (wrap and extend):
    coffee = Coffee()
    coffee = MilkDecorator(coffee)       # Wrap with milk
    coffee = SugarDecorator(coffee)      # Wrap with sugar
    coffee = WhipDecorator(coffee)       # Wrap with whip
    # Any combination, just by wrapping!

===================================
HOW IT WORKS
===================================

    class Component(ABC):
        @abstractmethod
        def operation(self): ...

    class ConcreteComponent(Component):
        def operation(self):
            return "base"

    class Decorator(Component):
        def __init__(self, component: Component):
            self._component = component  # Wraps another component

        def operation(self):
            return self._component.operation()  # Delegates to wrapped

    class ExtraDecorator(Decorator):
        def operation(self):
            return super().operation() + " + extra"

The key insight: a decorator IS-A component AND HAS-A component.
It wraps one and acts like one, so decorators can wrap decorators!

===================================
EXERCISE
===================================

PART 1: Coffee Shop

    class Coffee(ABC):
        @abstractmethod
        def cost(self) -> float: ...

        @abstractmethod
        def description(self) -> str: ...

    class SimpleCoffee(Coffee):
        cost: 2.00
        description: "Simple coffee"

    class CoffeeDecorator(Coffee):
        __init__(self, coffee: Coffee):
            Store the wrapped coffee.

        cost(self) -> float:
            Delegate to the wrapped coffee's cost.

        description(self) -> str:
            Delegate to the wrapped coffee's description.

    class MilkDecorator(CoffeeDecorator):
        cost: wrapped cost + 0.50
        description: wrapped description + ", milk"

    class SugarDecorator(CoffeeDecorator):
        cost: wrapped cost + 0.25
        description: wrapped description + ", sugar"

    class WhipCreamDecorator(CoffeeDecorator):
        cost: wrapped cost + 0.75
        description: wrapped description + ", whip cream"

---

PART 2: Text Processing Pipeline

    class TextProcessor(ABC):
        @abstractmethod
        def process(self, text: str) -> str: ...

    class PlainText(TextProcessor):
        process: Return the text unchanged.

    class TextDecorator(TextProcessor):
        __init__(self, processor: TextProcessor):
            Store the wrapped processor.

        process(self, text: str) -> str:
            Delegate to the wrapped processor.

    class TrimDecorator(TextDecorator):
        process: Trim whitespace from the wrapped result.

    class LowerCaseDecorator(TextDecorator):
        process: Lowercase the wrapped result.

    class CensorDecorator(TextDecorator):
        __init__(self, processor: TextProcessor, bad_words: list[str]):
            Store the processor and bad_words.

        process: Replace each bad word with "***" in the wrapped result.
            (Case-insensitive replacement)

---

PART 3 (HARD): Logger Decorator

    class DataSource(ABC):
        @abstractmethod
        def read(self) -> str: ...

        @abstractmethod
        def write(self, data: str) -> None: ...

    class StringDataSource(DataSource):
        __init__: Set up _data as empty string.
        read: Return _data.
        write: Set _data to the given string.

    class DataSourceDecorator(DataSource):
        __init__(self, source: DataSource): Store the wrapped source.
        read: Delegate to wrapped.
        write: Delegate to wrapped.

    class EncryptionDecorator(DataSourceDecorator):
        Simple "encryption": shift each character's ord by +1.
        write: Encrypt data, then pass to wrapped write.
        read: Read from wrapped, then decrypt (shift by -1).

    class LoggingDecorator(DataSourceDecorator):
        __init__(self, source: DataSource):
            Store source and _log as empty list.

        write: Append f"WRITE: {data}" to _log, then delegate.
        read: Delegate, then append f"READ: {result}" to _log. Return result.
        get_log() -> list[str]: Return the log.

ESTIMATED TIME: 30-45 minutes
"""

from abc import ABC, abstractmethod


# ============================================
# PART 1: Coffee Shop
# ============================================

# YOUR CODE HERE


# ============================================
# PART 2: Text Processing Pipeline
# ============================================

# YOUR CODE HERE


# ============================================
# PART 3 (HARD): Logger Decorator
# ============================================

# YOUR CODE HERE


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    # ==========================================
    # PART 1 TESTS: Coffee Shop
    # ==========================================
    print("\n=== Test 1: Simple Coffee ===")
    try:
        coffee = SimpleCoffee()
        assert coffee.cost() == 2.00
        assert coffee.description() == "Simple coffee"

        print(f"  {coffee.description()}: ${coffee.cost():.2f}")
        print("Test 1 PASSED!")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")
    except Exception as e:
        print(f"Test 1 ERROR: {e}")

    print("\n=== Test 2: Decorated Coffee ===")
    try:
        coffee = SimpleCoffee()
        coffee = MilkDecorator(coffee)
        assert coffee.cost() == 2.50
        assert coffee.description() == "Simple coffee, milk"

        coffee = SugarDecorator(coffee)
        assert coffee.cost() == 2.75
        assert coffee.description() == "Simple coffee, milk, sugar"

        print(f"  {coffee.description()}: ${coffee.cost():.2f}")
        print("Test 2 PASSED!")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 ERROR: {e}")

    print("\n=== Test 3: Fully Loaded Coffee ===")
    try:
        coffee = SimpleCoffee()
        coffee = MilkDecorator(coffee)
        coffee = SugarDecorator(coffee)
        coffee = SugarDecorator(coffee)  # Double sugar!
        coffee = WhipCreamDecorator(coffee)

        assert coffee.cost() == 2.00 + 0.50 + 0.25 + 0.25 + 0.75
        assert coffee.description() == "Simple coffee, milk, sugar, sugar, whip cream"

        print(f"  {coffee.description()}: ${coffee.cost():.2f}")
        print("  Double sugar works - decorators can stack!")
        print("Test 3 PASSED!")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 ERROR: {e}")

    # ==========================================
    # PART 2 TESTS: Text Processing
    # ==========================================
    print("\n=== Test 4: Text Processing Pipeline ===")
    try:
        processor = PlainText()
        processor = TrimDecorator(processor)
        processor = LowerCaseDecorator(processor)

        result = processor.process("  Hello WORLD  ")
        assert result == "hello world"

        print(f"  '  Hello WORLD  ' -> '{result}'")
        print("Test 4 PASSED!")
    except AssertionError as e:
        print(f"Test 4 FAILED: {e}")
    except Exception as e:
        print(f"Test 4 ERROR: {e}")

    print("\n=== Test 5: Censor Decorator ===")
    try:
        processor = PlainText()
        processor = CensorDecorator(processor, ["bad", "ugly"])

        result = processor.process("This is a bad and ugly sentence")
        assert result == "This is a *** and *** sentence"

        # Case insensitive
        result2 = processor.process("BAD words are BAD")
        assert result2 == "*** words are ***"

        print(f"  Censored: '{result}'")
        print("Test 5 PASSED!")
    except AssertionError as e:
        print(f"Test 5 FAILED: {e}")
    except Exception as e:
        print(f"Test 5 ERROR: {e}")

    print("\n=== Test 6: Combined Text Pipeline ===")
    try:
        processor = PlainText()
        processor = TrimDecorator(processor)
        processor = LowerCaseDecorator(processor)
        processor = CensorDecorator(processor, ["spam"])

        result = processor.process("   SPAM is annoying SPAM   ")
        assert result == "*** is annoying ***"

        print(f"  Full pipeline: '{result}'")
        print("Test 6 PASSED!")
    except AssertionError as e:
        print(f"Test 6 FAILED: {e}")
    except Exception as e:
        print(f"Test 6 ERROR: {e}")

    # ==========================================
    # PART 3 TESTS (HARD): Uncomment when ready
    # ==========================================

    # print("\n=== Test 7: Encryption Decorator ===")
    # try:
    #     source = StringDataSource()
    #     encrypted = EncryptionDecorator(source)
    #
    #     encrypted.write("Hello")
    #     # The raw data should be encrypted (shifted)
    #     raw = source.read()
    #     assert raw != "Hello", "Raw data should be encrypted"
    #     assert raw == "Ifmmp"  # Each char shifted +1
    #
    #     # Reading through decorator should decrypt
    #     result = encrypted.read()
    #     assert result == "Hello"
    #
    #     print(f"  Encrypted storage: '{raw}', Decrypted read: '{result}'")
    #     print("Test 7 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 7 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 7 ERROR: {e}")

    # print("\n=== Test 8: Logging + Encryption ===")
    # try:
    #     source = StringDataSource()
    #     encrypted = EncryptionDecorator(source)
    #     logged = LoggingDecorator(encrypted)
    #
    #     logged.write("Secret")
    #     result = logged.read()
    #     assert result == "Secret"
    #
    #     log = logged.get_log()
    #     assert len(log) == 2
    #     assert log[0] == "WRITE: Secret"
    #     assert log[1] == "READ: Secret"
    #
    #     print(f"  Log: {log}")
    #     print("  Logging wraps Encryption wraps Storage - decorators compose!")
    #     print("Test 8 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 8 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 8 ERROR: {e}")

    print("\n" + "=" * 60)
    print("DECORATOR PATTERN KEY LESSONS")
    print("=" * 60)
    print("""
1. Decorator wraps an object to add behaviour
2. A decorator IS-A component AND HAS-A component
3. Decorators can stack - wrap a wrapper!
4. Avoids subclass explosion for combinations
5. Each decorator adds ONE responsibility (SRP)
6. Order matters: Trim -> Lower -> Censor != Censor -> Lower -> Trim
7. Python's @decorator syntax is related but different from this pattern
""")
    print("=" * 60)
