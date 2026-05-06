# Module 01 — Classes and the `main()` Pattern

## Why this module exists

You can write Python like a script: variables at the top, statements flowing down,
no structure. It works for ten lines. It collapses for anything real.

This course teaches you to write Python the way a working engineer writes it:
with explicit types, encapsulated data, a clear program entry point, and the
discipline of a compiled-language mindset.

This first module establishes the three habits everything else rests on:

1. **A class is the unit of organization** — not a function, not a script.
2. **Every signature is typed** — strict, like C++.
3. **Every program has one entry point** — `main()`, the production-Python convention.

If you skip these, the rest of the course doesn't help you.

---

## What an object is

An object is **state plus the operations on that state, bundled together**.

A bank account holds a balance (state) and supports `deposit` and `withdraw`
(operations). The whole *point* of OOP is: keep state and the code that touches
it in one place. If the representation of the state ever changes — if you
decide to track balance in pennies instead of pounds, or store it in a database
instead of a variable — only the inside of the class changes. Everything that
*uses* a `BankAccount` keeps working.

That property is called **encapsulation**, and it is the whole reason classes
exist. Everything else (inheritance, polymorphism, design patterns) is built
on top of it.

A **class** is the blueprint. An **instance** (or "object") is what you get
when you build one from the blueprint:

```python
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance


alice = BankAccount("Alice", 100.0)   # alice is an instance of BankAccount
```

`__init__` is the **constructor**. It runs automatically when you create an
instance. It's where you set up the object's initial state.

`self` is the instance being constructed — Python's equivalent of `this` in
C++. The difference: in C++ `this` is implicit; in Python `self` is explicit.
You must write it as the first parameter of every instance method. The Python
designers chose explicit over implicit on purpose. Get used to it.

---

## Strict typing — the C++ discipline in Python

Python lets you skip type annotations. **Don't.**

Compare:

```python
def deposit(self, amount):           # weak — what is amount? what is returned?
    self.balance += amount

def deposit(self, amount: float) -> None:    # strict — contract is explicit
    self.balance += amount
```

The annotated version:

- **Documents intent.** A reader knows exactly what type to pass and what to
  expect back.
- **Is checkable.** Run `mypy --strict file.py` and the type checker will
  catch bugs before you ever run the code. (`mypy` is the de-facto static type
  checker for Python. Install with `pip install mypy`.)
- **Forces you to think.** You can't write `amount: float` without first
  deciding what `amount` actually is. C++ forces this on you. Python lets you
  skip it — which is exactly why undisciplined Python rots so fast.

**Rule for this course: every parameter and every return value gets a type
annotation, including `-> None` for functions that return nothing.** No
exceptions.

Common types you'll use immediately:

| Annotation | Meaning |
|---|---|
| `int`, `float`, `str`, `bool` | the obvious primitives |
| `list[int]` | a list of ints (Python 3.9+) |
| `dict[str, int]` | a dict mapping strings to ints |
| `tuple[int, str]` | a fixed 2-tuple of (int, str) |
| `Optional[int]` or `int \| None` | int *or* None — for "maybe missing" values |
| `-> None` | function returns nothing |

We'll go deeper into types in Module 08. For now: annotate everything.

---

## The `main()` pattern

In C and C++, every program has exactly one entry point: `main`. The compiler
enforces it. Execution starts there. It is a single, known anchor.

Python has no required entry point. You can put code at module level — and
most beginner Python tutorials do exactly that. **Don't.** Code at module
level runs as a side effect of *importing*. So if you write:

```python
# bad_script.py
account = BankAccount("Alice")
account.deposit(100.0)
print(account.balance)
```

…then the moment another file does `import bad_script`, the account gets
created, the deposit happens, and `100.0` is printed. The import system runs
your "program" as a side effect. That is a bug waiting to ambush you.

The correct pattern:

```python
def main() -> None:
    account = BankAccount("Alice")
    account.deposit(100.0)
    print(account.balance)


if __name__ == "__main__":
    main()
```

Two pieces:

**1. Wrap the program in `def main() -> None:`.** Now the program is a
function, not floating module-level code. Variables inside `main()` are
local — they don't pollute the module namespace. The function is callable
from tests. And when you eventually package this as a CLI tool, your
`pyproject.toml`'s `[project.scripts]` entry will point straight at this
function.

**2. The `if __name__ == "__main__":` guard.** `__name__` is a built-in
variable Python sets for you. When you run a file directly with
`python my_file.py`, Python sets `__name__` to the string `"__main__"`. When
the same file is imported by something else, Python sets `__name__` to the
module's name (e.g. `"my_file"`). So the guard means:

> *"Only call `main()` if this file is being run as the program — not if it's
> being imported as a library."*

That gives you a single, clear entry point.

The guard alone is non-negotiable Python (it prevents the import side-effect
bug). The `def main():` wrapper is a *convention* — but it's the convention
production Python follows, and this course follows it without exception.

---

## What you'll do in this module

Five files, three you'll edit, two you only run:

| File | Role |
|---|---|
| `README.md` | this file |
| `example.py` | **read** — fully worked `BankAccount` showing the patterns |
| `exercises.py` | **edit** — five progressive exercises |
| `capstone.py` | **edit** — Library + Book mini-system |
| `test_exercises.py` | **run** — pytest tests for the exercises |
| `test_capstone.py` | **run** — pytest tests for the capstone |

### One-time setup

```bash
pip install pytest mypy
```

### The workflow

1. Read `example.py` top to bottom.
2. Open `exercises.py` and `test_exercises.py` side by side.
3. Implement an exercise, then run:

   ```bash
   pytest test_exercises.py -v
   mypy --strict exercises.py
   ```

4. Watch failing tests turn green. Watch `mypy` go from errors to silence.
5. When all 5 exercises pass, move to `capstone.py` and `test_capstone.py`.

The tests are your spec. If a test is unclear, the test name and the
exercise's docstring should agree on what's expected. If they disagree, that's
a bug — flag it.

If `mypy --strict` complains, your types are wrong. Fix them before moving on.
The whole point of this discipline is *the type checker catches your bugs
before you do*. Tests verify behaviour; types verify shape. You want both.

---

## Engineering principles introduced in this module

You will see these recur throughout the course. Internalize them now.

- **Validate at the boundary.** When data enters an object (constructor
  arguments, method parameters), check that it makes sense. A negative deposit
  is a bug; raise an exception immediately, where the bug is, instead of
  letting bad state propagate.

- **Specific error messages.** `"insufficient funds: balance=50.00, requested=100.00"`
  is useful. `"error"` is not. Future-you will be debugging this at 11pm.
  Be kind to future-you.

- **State and operations live together.** If you find yourself reaching into
  an object's attributes from the outside to "fix them up," the operation
  belongs on the object as a method. (This rule will sharpen into Module 02's
  encapsulation discipline.)
