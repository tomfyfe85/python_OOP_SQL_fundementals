"""Benchmark — run every sorter on the same input and time them.

This file is the payoff for the interface design. Notice the loop: it
iterates over `list[Sorter]` and calls `.sort()` on each. It does NOT
know or care which concrete algorithm it is running. Adding a new sort
means adding it to the list — nothing else changes.

Run:    python benchmark.py
"""

import random
import time

from sorter import Sorter
from bubble_sort import BubbleSort
from insertion_sort import InsertionSort
from selection_sort import SelectionSort
from merge_sort import MergeSort
from quick_sort import QuickSort


def time_sort(sorter: Sorter, data: list[int]) -> tuple[list[int], float]:
    # perf_counter is the right tool for timing short intervals — higher
    # resolution than time.time() and unaffected by wall-clock changes.
    start = time.perf_counter()
    result = sorter.sort(data)
    elapsed = time.perf_counter() - start
    return result, elapsed


def run_benchmark(size: int = 1_000) -> None:
    # Seed so successive runs use the same input — fair comparisons.
    random.seed(42)
    data = [random.randint(0, size) for _ in range(size)]
    expected = sorted(data)  # ground truth (Python's built-in Timsort)

    sorters: list[Sorter] = [
        BubbleSort(),
        InsertionSort(),
        SelectionSort(),
        MergeSort(),
        QuickSort(),
    ]

    print(f"Sorting {size} ints. Times in milliseconds.\n")
    for s in sorters:
        try:
            result, elapsed = time_sort(s, data)
            ok = "OK " if result == expected else "BAD"
            print(f"  {ok}  {s.name:<14} {elapsed * 1000:>9.2f} ms")
        except NotImplementedError:
            print(f"  --   {s.name:<14}  not implemented yet")


def main() -> None:
    run_benchmark(size=1_000)


if __name__ == "__main__":
    main()
