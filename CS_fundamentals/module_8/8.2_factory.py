"""
Exercise 8.2: Factory Method Pattern

FACTORY METHOD PATTERN (Creational)
====================================

Define an interface for creating objects, but let subclasses decide
which class to instantiate. The factory method lets a class defer
instantiation to subclasses.

===================================
WHY USE FACTORY?
===================================

Without factory:
    def create_document(doc_type):
        if doc_type == "pdf":
            return PDFDocument()
        elif doc_type == "word":
            return WordDocument()
        elif doc_type == "html":
            return HTMLDocument()
        # Adding new type = modifying this function (violates OCP!)

With factory:
    class DocumentFactory:
        _creators = {}

        @classmethod
        def register(cls, doc_type, creator):
            cls._creators[doc_type] = creator

        @classmethod
        def create(cls, doc_type):
            creator = cls._creators.get(doc_type)
            if not creator:
                raise ValueError(f"Unknown type: {doc_type}")
            return creator()

    # Register types - no if/elif chain!
    DocumentFactory.register("pdf", PDFDocument)
    DocumentFactory.register("word", WordDocument)

    # Adding new type = just register it. Existing code untouched.
    DocumentFactory.register("html", HTMLDocument)

===================================
FACTORY vs CONSTRUCTOR
===================================

Constructor: You decide exactly which class to create.
    doc = PDFDocument()  # Must know the specific class

Factory: You describe WHAT you want, factory decides HOW.
    doc = DocumentFactory.create("pdf")  # Just say what type

===================================
EXERCISE
===================================

PART 1: Shape Classes

Create an ABC and concrete shapes:

    class Shape(ABC):
        @abstractmethod
        def area(self) -> float: ...

        @abstractmethod
        def perimeter(self) -> float: ...

        @abstractmethod
        def describe(self) -> str: ...

    class Circle(Shape):
        __init__(self, radius: float)
        area: pi * r^2
        perimeter: 2 * pi * r
        describe: "Circle with radius {radius}"

    class Rectangle(Shape):
        __init__(self, width: float, height: float)
        area: width * height
        perimeter: 2 * (width + height)
        describe: "Rectangle {width}x{height}"

    class Triangle(Shape):
        __init__(self, base: float, height: float)
        area: 0.5 * base * height
        perimeter: base + height + hypotenuse (use math.sqrt)
        describe: "Triangle with base {base} and height {height}"

---

PART 2: ShapeFactory

    class ShapeFactory:
        A factory that creates shapes from a type string and parameters.

        @staticmethod
        def create(shape_type: str, **kwargs) -> Shape:
            Create and return the appropriate Shape.

            shape_type: "circle", "rectangle", or "triangle"
            kwargs: the parameters for that shape
                circle: radius
                rectangle: width, height
                triangle: base, height

            Raise ValueError for unknown shape_type.

        Examples:
            ShapeFactory.create("circle", radius=5)
            ShapeFactory.create("rectangle", width=4, height=6)
            ShapeFactory.create("triangle", base=3, height=4)

---

PART 3 (HARD): Extensible Factory with Registration

    class ExtensibleShapeFactory:
        A factory where new shapes can be REGISTERED without modifying
        the factory code (OCP!).

        _registry: dict = {}  (class-level)

        @classmethod
        def register(cls, shape_type: str, shape_class: type) -> None:
            Register a new shape type.

        @classmethod
        def create(cls, shape_type: str, **kwargs) -> Shape:
            Create a registered shape. Raise ValueError if unknown.

        @classmethod
        def get_available_types(cls) -> list[str]:
            Return list of registered type names.

ESTIMATED TIME: 30-45 minutes
"""

from abc import ABC, abstractmethod
import math


# ============================================
# PART 1: Shape Classes
# ============================================

# YOUR CODE HERE


# ============================================
# PART 2: ShapeFactory
# ============================================

# YOUR CODE HERE


# ============================================
# PART 3 (HARD): Extensible Factory
# ============================================

# YOUR CODE HERE


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    # ==========================================
    # PART 1 TESTS: Shape Classes
    # ==========================================
    print("\n=== Test 1: Circle ===")
    try:
        c = Circle(5)
        assert isinstance(c, Shape)
        assert abs(c.area() - 78.5398) < 0.01
        assert abs(c.perimeter() - 31.4159) < 0.01
        assert c.describe() == "Circle with radius 5"

        print(f"  {c.describe()}: area={c.area():.2f}, perimeter={c.perimeter():.2f}")
        print("Test 1 PASSED!")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")
    except Exception as e:
        print(f"Test 1 ERROR: {e}")

    print("\n=== Test 2: Rectangle ===")
    try:
        r = Rectangle(4, 6)
        assert isinstance(r, Shape)
        assert r.area() == 24
        assert r.perimeter() == 20
        assert r.describe() == "Rectangle 4x6"

        print(f"  {r.describe()}: area={r.area()}, perimeter={r.perimeter()}")
        print("Test 2 PASSED!")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 ERROR: {e}")

    print("\n=== Test 3: Triangle ===")
    try:
        t = Triangle(3, 4)
        assert isinstance(t, Shape)
        assert t.area() == 6.0
        # Hypotenuse of 3-4-5 triangle = 5, perimeter = 12
        assert t.perimeter() == 12.0

        print(f"  {t.describe()}: area={t.area()}, perimeter={t.perimeter()}")
        print("Test 3 PASSED!")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 ERROR: {e}")

    # ==========================================
    # PART 2 TESTS: ShapeFactory
    # ==========================================
    print("\n=== Test 4: ShapeFactory ===")
    try:
        circle = ShapeFactory.create("circle", radius=5)
        assert isinstance(circle, Circle)
        assert abs(circle.area() - 78.5398) < 0.01

        rect = ShapeFactory.create("rectangle", width=4, height=6)
        assert isinstance(rect, Rectangle)
        assert rect.area() == 24

        tri = ShapeFactory.create("triangle", base=3, height=4)
        assert isinstance(tri, Triangle)
        assert tri.area() == 6.0

        print("  Factory creates all shape types")
        print("Test 4 PASSED!")
    except AssertionError as e:
        print(f"Test 4 FAILED: {e}")
    except Exception as e:
        print(f"Test 4 ERROR: {e}")

    print("\n=== Test 5: Factory Unknown Type ===")
    try:
        try:
            ShapeFactory.create("hexagon", sides=6)
            assert False, "Should raise ValueError"
        except ValueError:
            pass

        print("  Unknown type raises ValueError")
        print("Test 5 PASSED!")
    except AssertionError as e:
        print(f"Test 5 FAILED: {e}")
    except Exception as e:
        print(f"Test 5 ERROR: {e}")

    print("\n=== Test 6: Factory Polymorphism ===")
    try:
        shapes = [
            ShapeFactory.create("circle", radius=3),
            ShapeFactory.create("rectangle", width=2, height=5),
            ShapeFactory.create("triangle", base=6, height=8),
        ]

        # All shapes can be treated the same way
        for shape in shapes:
            assert isinstance(shape, Shape)
            assert shape.area() > 0
            assert shape.perimeter() > 0
            print(f"  {shape.describe()}: area={shape.area():.2f}")

        print("Test 6 PASSED!")
    except AssertionError as e:
        print(f"Test 6 FAILED: {e}")
    except Exception as e:
        print(f"Test 6 ERROR: {e}")

    # ==========================================
    # PART 3 TESTS (HARD): Uncomment when ready
    # ==========================================

    # print("\n=== Test 7: Extensible Factory - Registration ===")
    # try:
    #     ExtensibleShapeFactory.register("circle", Circle)
    #     ExtensibleShapeFactory.register("rectangle", Rectangle)
    #     ExtensibleShapeFactory.register("triangle", Triangle)
    #
    #     c = ExtensibleShapeFactory.create("circle", radius=10)
    #     assert isinstance(c, Circle)
    #     assert abs(c.area() - 314.159) < 0.1
    #
    #     types = ExtensibleShapeFactory.get_available_types()
    #     assert "circle" in types
    #     assert "rectangle" in types
    #     assert "triangle" in types
    #
    #     print(f"  Available types: {types}")
    #     print("Test 7 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 7 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 7 ERROR: {e}")

    # print("\n=== Test 8: Extensible Factory - Add New Shape ===")
    # try:
    #     # Create a new shape class
    #     class Square(Shape):
    #         def __init__(self, side):
    #             self.side = side
    #         def area(self):
    #             return self.side ** 2
    #         def perimeter(self):
    #             return 4 * self.side
    #         def describe(self):
    #             return f"Square with side {self.side}"
    #
    #     # Register it - NO changes to factory code!
    #     ExtensibleShapeFactory.register("square", Square)
    #
    #     sq = ExtensibleShapeFactory.create("square", side=5)
    #     assert sq.area() == 25
    #     assert sq.perimeter() == 20
    #
    #     print(f"  Added Square: {sq.describe()}, area={sq.area()}")
    #     print("  THIS is OCP: extended without modifying factory!")
    #     print("Test 8 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 8 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 8 ERROR: {e}")

    print("\n" + "=" * 60)
    print("FACTORY PATTERN KEY LESSONS")
    print("=" * 60)
    print("""
1. Factory creates objects without exposing creation logic
2. Client says WHAT it wants, factory decides HOW to make it
3. Eliminates if/elif chains for object creation
4. Extensible factory with registration follows OCP
5. All created objects share a common interface (ABC)
6. Enables polymorphism - treat all shapes the same way
""")
    print("=" * 60)
