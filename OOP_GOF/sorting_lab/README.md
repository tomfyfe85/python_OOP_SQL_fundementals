# Sorting Lab — One Class Per File, Behind an Interface

A side-lab to practice **modular Python**: each class lives in its own file,
imports its dependencies explicitly, and conforms to a shared interface
(`Sorter`). Same shape as a Java package — and exactly the structure you
will need when we hit the **Strategy pattern** in Module 13 and **abstract
classes** in Module 05.

## Layout

```
sorting_lab/
├── sorter.py            # Sorter ABC — the "interface"
├── bubble_sort.py       # BubbleSort        (worked example)
├── merge_sort.py        # MergeSort         (worked example, divide & conquer)
├── insertion_sort.py    # InsertionSort     (EXERCISE — stub for you)
├── selection_sort.py    # SelectionSort     (EXERCISE — stub for you)
├── quick_sort.py        # QuickSort         (EXERCISE — stub for you, divide & conquer)
├── benchmark.py         # times every sorter on the same input
├── main.py              # demo — two sorters via the same interface
└── README.md            # you are here
```

## Run it

```bash
cd sorting_lab
python main.py        # small demo
python benchmark.py   # times all five (stubs print "not implemented yet")
```

## What an "interface" looks like in Python

Java's `interface` becomes Python's `abc.ABC` plus `@abstractmethod`. See
[`sorter.py`](sorter.py):

```python
class Sorter(ABC):
    @property
    @abstractmethod
    def name(self) -> str: ...

    @abstractmethod
    def sort(self, data: list[int]) -> list[int]: ...
```

Any subclass that does not override BOTH `name` and `sort` will fail at
**instantiation time** — `MyBrokenSorter()` raises `TypeError`. That is
the contract being enforced.

> Aside: Python also has `typing.Protocol` for "duck-typed" interfaces
> (no inheritance required, just structural matching). ABCs vs Protocols
> is a topic for Module 05.

## Why one class per file?

You asked to "think modular." Splitting one class per file gives you:

1. **Clear dependency graph** — every `import` line is a load-bearing
   declaration. You can see at a glance what each file depends on.
2. **No accidental coupling** — classes can only reach each other through
   imports, not by sharing module-local state.
3. **Easier to test in isolation** — `test_bubble_sort.py` only needs to
   import one thing.
4. **Matches the Java/C++/Rust mental model** — useful if you ever read
   one of those codebases.

The downside Python people will warn you about: it is more files than
"idiomatic" Python typically uses. That is fine — for *learning*
modularity, the explicit version is more instructive.

## The five algorithms

All five take `list[int]` and return a new sorted `list[int]`.

| Algorithm     | Best       | Average    | Worst      | Space     | In place? | Stable? |
|---------------|------------|------------|------------|-----------|-----------|---------|
| Bubble        | O(n)       | O(n²)      | O(n²)      | O(1)      | yes       | yes     |
| Insertion     | O(n)       | O(n²)      | O(n²)      | O(1)      | yes       | yes     |
| Selection     | O(n²)      | O(n²)      | O(n²)      | O(1)      | yes       | no      |
| Merge         | O(n log n) | O(n log n) | O(n log n) | O(n)      | no        | yes     |
| Quick         | O(n log n) | O(n log n) | O(n²)      | O(log n)* | yes*      | no      |

\* For an in-place quicksort. The simple list-comprehension version in the
quick_sort.py docstring is O(n) extra space.

### Bubble Sort
Walk the list, swap adjacent pairs that are out of order. After one pass
the largest element has "bubbled" to the end. Repeat. With an early-exit
flag, sorted input takes one pass — O(n).

### Insertion Sort
Like sorting a hand of cards: take the next card and slide it left into
its correct position among the cards you have already arranged. The left
side is sorted at every step. Best-case O(n) on nearly-sorted data.

### Selection Sort
Find the minimum of the unsorted region, swap it to the front of that
region. Repeat. Always O(n²) — no early exit possible. But it makes the
fewest *swaps* of any of the simple sorts (n−1 max).

### Merge Sort — Divide and Conquer
Split the list in half, recursively sort each half, then **merge** the two
sorted halves with two pointers. The merge is O(n); we do log₂(n) levels
of merging; total O(n log n) guaranteed. Python's built-in `sorted()` is
**Timsort** — a heavily optimised mergesort.

### Quick Sort — Divide and Conquer
Pick a pivot. **Partition** so smaller elements go left, larger go right
(the pivot is now in its final place). Recursively quicksort each side.
Same average complexity as merge but usually faster in practice (better
cache behaviour, no merge buffer). Worst case O(n²) on bad pivots —
mitigated by random or median-of-three pivot choice.

## Your turn

Implement the three stubs in any order:

1. `insertion_sort.py` — easiest after bubble. Watch for off-by-one in
   the "slide left" loop.
2. `selection_sort.py` — easiest of all. Two nested loops, one swap per
   outer pass.
3. `quick_sort.py` — start with the list-comprehension version in the
   stub's docstring. Once that works, try an in-place version using two
   indices and a partition step.

Re-run `python benchmark.py` after each one to watch the times update.
On 1 000 ints you should see the O(n²) sorts in the tens of ms and the
O(n log n) sorts under 5 ms — the gap widens fast as `size` grows. Try
bumping `size=1_000` to `10_000` and watch bubble crawl while merge stays
quick.

## When this lab connects to the main course

- **Module 04 (inheritance/polymorphism)** — every concrete sorter IS-A
  `Sorter`. The benchmark loop is polymorphism in action.
- **Module 05 (abstraction)** — `abc.ABC` and `@abstractmethod` get the
  full treatment. We will also meet `Protocol`.
- **Module 13 (behavioral patterns I)** — this lab IS the **Strategy
  pattern**. Different algorithms behind one interface, swappable at
  runtime. You will recognise the shape immediately when we get there.
