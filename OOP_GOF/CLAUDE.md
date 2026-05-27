# OOP_GOF — Python OOP / GoF / Data Pipelines Course

> Context handoff for any Claude session working in this folder.
> Read this top-to-bottom before doing anything in this directory.

## What this project is

A self-built, **17-module Python course** taking the user from class basics
through every Gang-of-Four design pattern and into NumPy / Pandas data
pipelines. The user is building it one module at a time and working through
each module before the next is created.

**Engineering rigor target: PPP (Stroustrup) level.** Translation: this is
*not* "casual Python" — every signature is fully typed, every program has
an explicit `main()` entry point, comments explain WHY (not WHAT), and
encapsulation discipline is enforced. The user wants C++-style discipline
*inside* Python.

## The user

- Building this course to become a stronger engineer.
- Background: working through CS50 → C++ as a parallel track. Comfortable
  with class basics; goal is depth, modularity, and design-pattern fluency.
- Career target: junior Java role (UK, finance/enterprise), long-term
  IBM-type companies.
- **Java parallel notes are PAUSED** (since 2026-05-06). Do NOT proactively
  offer "here's how this looks in Java" — the user is concentrating on
  Python only.
- Wants to UNDERSTAND, not just get answers. Don't hand over solutions
  unless explicitly asked.

## Course structure (17 modules)

| Part | Modules |
|---|---|
| I  — OOP Foundations | 01_classes_and_main, 02_encapsulation, 03_dunder_methods, 04_inheritance_polymorphism, 05_abstraction, 06_composition_over_inheritance |
| II — Pythonic Engineering | 07_decorators, 08_typing_strict, 09_errors_and_logging |
| III — SOLID | 10_solid_principles |
| IV — Gang of Four | 11_creational, 12_structural, 13_behavioral_1, 14_behavioral_2 |
| V  — Data Pipelines | 15_numpy, 16_pandas, 17_data_pipeline_capstone |

## Progress

- **Module 01 (`01_classes_and_main/`)** — in progress. This is the style
  sample: every later module follows its layout. User is currently working
  through the 5 exercises and the capstone.
- **Modules 02–17** — not started. Build them ONE AT A TIME when the user
  signals they are ready. Do not pre-build modules.
- **`sorting_lab/` side-lab** — built. NOT part of the 17 modules. It is
  hands-on practice of one-class-per-file modularity + ABCs (interfaces)
  + sorting algorithms. Previews material from Module 05 (abstraction)
  and Module 13 (Strategy pattern). Two algorithms are worked examples
  (BubbleSort, MergeSort); three are stubs the user implements
  (InsertionSort, SelectionSort, QuickSort).

## Per-module file pattern (REQUIRED)

Every numbered module must contain exactly these files:

| File | Purpose |
|---|---|
| `README.md` | Chapter-style explanation in PPP voice. Teach the WHY. |
| `example.py` | Worked example with engineering-commentary comments. |
| `exercises.py` | 5 progressive exercises, simple → harder. No solutions. |
| `capstone.py` | Integrative mini-project after the 5 exercises. |
| `test_exercises.py` | pytest tests — these are the user's spec. |
| `test_capstone.py` | pytest tests for the capstone. |
| `revision.py` | Quick callback to prior module. **Skip for Module 01.** |

## Code style — non-negotiable

Every `.py` file in this course MUST:

1. **Have full type annotations** on every parameter and return value,
   including `-> None`. The user runs `mypy --strict` on everything.
2. **Use the `main()` entry-point pattern**:
   ```python
   def main() -> None:
       ...

   if __name__ == "__main__":
       main()
   ```
   No code at module level. Module-level code runs as a side effect of
   `import`, which is a bug.
3. **Comment sparingly, explain WHY only.** Never explain WHAT the code
   does — well-named identifiers do that. Comments justify non-obvious
   decisions, hidden constraints, or things that would surprise a reader.
4. **Validate at the boundary.** Constructor / public-method arguments
   get checked. Bad data should raise immediately, with a specific
   error message including the offending value.
5. **No solutions files** unless the user explicitly requests them.

Style sample to match: [01_classes_and_main/example.py](01_classes_and_main/example.py).
If your output doesn't look like that, it's wrong.

## How to interact with the user

- **Build one module at a time.** Wait for "ready for module N" before
  scaffolding it.
- **Do not give solutions unsolicited.** If they're stuck, hint or ask
  diagnostic questions first.
- **Do not write Java translations / parallels.** That track is paused.
- **Do not pad responses.** Short, direct, no trailing summaries the
  user can read from the diff.
- **For exploratory questions** ("what should we do here?"), give a 2–3
  sentence recommendation with a tradeoff, then wait for the user to
  decide. Don't barrel into implementation.
- **Suggest edge cases** when reviewing exercises — the user values
  catching subtle bugs over passing the obvious cases. Example:
  `[2, 1, 0]` for two-pointer code catches off-by-one bugs that
  `[0, 1, 0, 3, 12]` misses.

## How to interact with the sorting_lab

It's a polymorphism / interface demo. Layout:

```
sorting_lab/
├── sorter.py            # Sorter ABC (the "interface")
├── bubble_sort.py       # worked example, O(n^2) with early-exit
├── merge_sort.py        # worked example, divide & conquer, O(n log n)
├── insertion_sort.py    # STUB — user implements
├── selection_sort.py    # STUB — user implements
├── quick_sort.py        # STUB — user implements
├── benchmark.py         # times all five against the same input
├── main.py              # demo of two sorters via the interface
└── README.md            # Big-O table + algorithm intuitions
```

Run from inside `sorting_lab/`:
```bash
python main.py
python benchmark.py
```

Stubs raise `NotImplementedError` — the benchmark catches that and prints
"not implemented yet" so the user can run it any time.

When the user implements a stub, **do not refactor or "improve" their
working code** — they're learning the algorithm shape. Only flag bugs
or correctness issues. Style nits can wait.

## Adjacent context

- The user has a separate DSA course at `../python_cs/` (arrays, hash
  maps, two pointers, etc.) — that course follows a different structure
  (Example → Practice Questions → LeetCode Capstone → Revision). Don't
  conflate the two.
- The user keeps memory in `~/.claude/projects/-Users-tomfyfe-codes-python-cs/memory/`.
  Reading it gives broader context (career goals, role research, debugging
  insights). MEMORY.md is the index.

## When in doubt

Match the style of [01_classes_and_main/](01_classes_and_main/). Ask the
user before adding anything that isn't already in the per-module file
pattern. Build less, not more.
