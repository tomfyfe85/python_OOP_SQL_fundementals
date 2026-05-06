"""Module 01 — Exercises.

Five exercises, progressive difficulty. Every solution must:
  - Use full type annotations on all parameters and return values
  - Live inside a class
  - Pass the tests in test_exercises.py
  - Pass `mypy --strict exercises.py`

Workflow:
    pytest test_exercises.py -v       # run tests, watch them fail then pass
    mypy --strict exercises.py        # check types
    python exercises.py               # optional: run main() for ad-hoc demo
"""

import math
import time


# =============================================================================
# Exercise 1 — Point
# =============================================================================
# Build a `Point` class representing a 2D point.
#
# Requirements:
#   - Constructor takes x: float and y: float
#   - Method `distance_to(other: "Point") -> float` returns Euclidean distance
#   - Method `describe() -> str` returns "Point(x, y)"
#
# In main(): create two points, print each, print distance between them.
#
# Hint: use math.sqrt and math.hypot. The string "Point" in the type hint
#       (as a forward reference) is required because the class isn't fully
#       defined yet at the point the method is being declared.
# =============================================================================

# YOUR CODE HERE


# =============================================================================
# Exercise 2 — Rectangle
# =============================================================================
# Build a `Rectangle` class.
#
# Requirements:
#   - Constructor takes width: float and height: float
#   - Validate: both must be > 0 — raise ValueError otherwise
#   - Method `area() -> float`
#   - Method `perimeter() -> float`
#   - Method `is_square() -> bool`
#
# In main(): create three rectangles (one a square), print their stats.
#
# Engineering note: validate in the constructor, not in area() / perimeter().
# Bad data should never make it into the object in the first place.
# =============================================================================

# YOUR CODE HERE


# =============================================================================
# Exercise 3 — Temperature
# =============================================================================
# Build a `Temperature` class storing temperature in Celsius internally.
#
# Requirements:
#   - Constructor takes celsius: float
#   - Validate: celsius must be >= -273.15 (absolute zero)
#   - Method `to_fahrenheit() -> float`   (F = C * 9/5 + 32)
#   - Method `to_kelvin() -> float`        (K = C + 273.15)
#   - Method `describe() -> str` returns "X°C / Y°F / Z K" formatted to 2dp
#
# In main(): create temperatures for boiling water (100), room temp (21),
#            and absolute zero (-273.15); print each.
#
# Engineering note: storing in ONE canonical unit (Celsius) and computing the
# others on demand is cleaner than storing all three. If you ever need to
# change the value, there's only one source of truth.
# =============================================================================

# YOUR CODE HERE


# =============================================================================
# Exercise 4 — Stopwatch
# =============================================================================
# Build a `Stopwatch` class.
#
# Requirements:
#   - Constructor takes no arguments other than self
#   - Method `start() -> None`         records the current time
#   - Method `stop() -> None`          records the stop time
#   - Method `elapsed() -> float`      returns seconds between start and stop
#   - If elapsed() is called before start() and stop() have both run,
#     raise RuntimeError with a clear message
#
# In main(): start the stopwatch, sleep 0.1s, stop, print elapsed.
#
# Hint: use time.monotonic() — NOT time.time().
#       time.time() can go backwards if the system clock is adjusted (NTP,
#       DST, manual change). time.monotonic() is guaranteed non-decreasing.
#       This is exactly the kind of distinction that separates code that
#       works on your laptop from code that works in production.
#
# Hint: you'll need attributes for start_time and stop_time that may not
#       exist yet. Initialise them to None in __init__ and use Optional[float]
#       in the type hints.
# =============================================================================

# YOUR CODE HERE


# =============================================================================
# Exercise 5 — Counter
# =============================================================================
# Build a `Counter` class — a numeric counter with history tracking.
#
# Requirements:
#   - Constructor takes initial: int = 0
#   - Method `increment(by: int = 1) -> None`
#   - Method `decrement(by: int = 1) -> None`
#   - Method `reset() -> None`           sets value back to initial
#   - Method `value() -> int`            returns current value
#   - Method `history() -> list[int]`    returns every value the counter has
#                                        held, oldest first, including the
#                                        initial value
#
# In main(): create a Counter(5), increment by 1, increment by 3, decrement
#            by 2, reset, increment by 1. Print value() and history() at the
#            end. Expected history: [5, 6, 9, 7, 5, 6].
#
# Engineering note: `history()` should return a COPY of the internal list,
# not the list itself. If a caller mutates what you return, you've leaked
# control of your internal state. (We'll formalise this in Module 02.)
# Hint: `return self._history.copy()` or `return list(self._history)`.
# =============================================================================

# YOUR CODE HERE


def main() -> None:
    # Test your solutions here. Uncomment as you complete each exercise.
    pass


if __name__ == "__main__":
    main()
