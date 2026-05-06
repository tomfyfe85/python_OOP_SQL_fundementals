"""Entry point — small demo of two sorters running through the same API.

The point of this file is the type of `demo`'s parameter:

        def demo(sorter: Sorter, data: list[int]) -> None:

`Sorter` is the interface, not a concrete class. `demo` works with ANY
class that satisfies the Sorter contract — bubble, merge, the stubs you
will implement, or one you write next month. That decoupling is what
"program to an interface, not an implementation" means in practice.

Run:    python main.py
"""

from sorter import Sorter
from bubble_sort import BubbleSort
from merge_sort import MergeSort


def demo(sorter: Sorter, data: list[int]) -> None:
    print(f"  {sorter.name:<14} input  = {data}")
    print(f"  {sorter.name:<14} output = {sorter.sort(data)}\n")


def main() -> None:
    sample = [5, 2, 9, 1, 7, 3, 8, 4, 6]

    print("Two algorithms, one interface:\n")
    demo(BubbleSort(), sample)
    demo(MergeSort(), sample)


if __name__ == "__main__":
    main()
