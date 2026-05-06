"""Module 01 — Tests for exercises.py.

Run from this directory:
    pytest test_exercises.py -v

Tests will fail with ImportError until you define the classes in exercises.py.
That's expected — let the failures guide you. Implement the class, run the
tests, watch them go from red to green.

Install pytest if you don't have it:
    pip install pytest
"""

import math
import time

import pytest

from exercises import Counter, Point, Rectangle, Stopwatch, Temperature


# =============================================================================
# Exercise 1 — Point
# =============================================================================


def test_point_distance_3_4_5() -> None:
    a = Point(0.0, 0.0)
    b = Point(3.0, 4.0)
    assert a.distance_to(b) == pytest.approx(5.0)


def test_point_distance_is_symmetric() -> None:
    a = Point(1.0, 2.0)
    b = Point(4.0, 6.0)
    assert a.distance_to(b) == pytest.approx(b.distance_to(a))


def test_point_distance_to_self_is_zero() -> None:
    p = Point(7.0, -3.0)
    assert p.distance_to(p) == pytest.approx(0.0)


def test_point_describe_format() -> None:
    assert Point(1.0, 2.0).describe() == "Point(1.0, 2.0)"


# =============================================================================
# Exercise 2 — Rectangle
# =============================================================================


def test_rectangle_area() -> None:
    assert Rectangle(3.0, 4.0).area() == pytest.approx(12.0)


def test_rectangle_perimeter() -> None:
    assert Rectangle(3.0, 4.0).perimeter() == pytest.approx(14.0)


def test_rectangle_is_square_true() -> None:
    assert Rectangle(5.0, 5.0).is_square() is True


def test_rectangle_is_square_false() -> None:
    assert Rectangle(5.0, 4.0).is_square() is False


def test_rectangle_zero_width_rejected() -> None:
    with pytest.raises(ValueError):
        Rectangle(0.0, 5.0)


def test_rectangle_negative_height_rejected() -> None:
    with pytest.raises(ValueError):
        Rectangle(5.0, -1.0)


# =============================================================================
# Exercise 3 — Temperature
# =============================================================================


def test_temperature_water_boiling_to_fahrenheit() -> None:
    assert Temperature(100.0).to_fahrenheit() == pytest.approx(212.0)


def test_temperature_water_freezing_to_fahrenheit() -> None:
    assert Temperature(0.0).to_fahrenheit() == pytest.approx(32.0)


def test_temperature_zero_celsius_to_kelvin() -> None:
    assert Temperature(0.0).to_kelvin() == pytest.approx(273.15)


def test_temperature_absolute_zero_allowed() -> None:
    # Exactly -273.15 must be allowed (boundary value).
    t = Temperature(-273.15)
    assert t.to_kelvin() == pytest.approx(0.0)


def test_temperature_below_absolute_zero_rejected() -> None:
    with pytest.raises(ValueError):
        Temperature(-300.0)


def test_temperature_describe_contains_all_three_units() -> None:
    text = Temperature(100.0).describe()
    assert "100" in text
    assert "212" in text
    assert "373" in text


# =============================================================================
# Exercise 4 — Stopwatch
# =============================================================================


def test_stopwatch_elapsed_after_start_and_stop() -> None:
    sw = Stopwatch()
    sw.start()
    time.sleep(0.05)
    sw.stop()
    elapsed = sw.elapsed()
    # Generous bounds — sleep is best-effort, OS scheduler can delay.
    assert 0.04 < elapsed < 1.0


def test_stopwatch_elapsed_before_start_raises() -> None:
    sw = Stopwatch()
    with pytest.raises(RuntimeError):
        sw.elapsed()


def test_stopwatch_elapsed_before_stop_raises() -> None:
    sw = Stopwatch()
    sw.start()
    with pytest.raises(RuntimeError):
        sw.elapsed()


# =============================================================================
# Exercise 5 — Counter
# =============================================================================


def test_counter_default_initial_is_zero() -> None:
    assert Counter().value() == 0


def test_counter_custom_initial() -> None:
    assert Counter(5).value() == 5


def test_counter_increment_default_step() -> None:
    c = Counter()
    c.increment()
    assert c.value() == 1


def test_counter_increment_custom_step() -> None:
    c = Counter(10)
    c.increment(by=3)
    assert c.value() == 13


def test_counter_decrement() -> None:
    c = Counter(10)
    c.decrement(by=4)
    assert c.value() == 6


def test_counter_reset_returns_to_initial() -> None:
    c = Counter(7)
    c.increment(by=10)
    c.reset()
    assert c.value() == 7


def test_counter_history_full_sequence() -> None:
    c = Counter(5)
    c.increment(by=1)   # 6
    c.increment(by=3)   # 9
    c.decrement(by=2)   # 7
    c.reset()           # 5
    c.increment(by=1)   # 6
    assert c.history() == [5, 6, 9, 7, 5, 6]


def test_counter_history_returns_copy_not_internal_list() -> None:
    # Mutating what history() returns must not affect the counter.
    # If this test fails, you returned the internal list directly — leak.
    c = Counter(5)
    c.increment(by=1)
    leaked = c.history()
    leaked.append(9999)
    assert c.history() == [5, 6]
