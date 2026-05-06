"""SelectionSort — EXERCISE.

Idea:
    Repeatedly find the smallest remaining element and put it at the front
    of the unsorted region.

        Pass 1: find min of arr[0:],   swap it into arr[0].
        Pass 2: find min of arr[1:],   swap it into arr[1].
        Pass 3: find min of arr[2:],   swap it into arr[2].
        ...

Complexity:
    Time:  O(n^2) in EVERY case — best, average, worst.
           Even on already-sorted input it scans the whole tail each pass
           to "confirm" the minimum. There is no early-exit possible.
    Space: O(1) — in place.

Selection vs bubble:
    Both are O(n^2), but selection makes far fewer SWAPS — at most n-1
    total, vs bubble's O(n^2). If write-cost dominates (e.g. flash memory)
    selection wins. If reads dominate, bubble's early-exit on sorted data
    wins.

TODO:
    Implement `sort`. Hint: use a nested loop. The inner loop tracks the
    INDEX of the current minimum (not the value), then swap once at the
    end of each outer pass.
"""

from sorter import Sorter


class SelectionSort(Sorter):
    @property
    def name(self) -> str:
        return "SelectionSort"

    def sort(self, data: list[int]) -> list[int]:
        # TODO: your implementation here.
        raise NotImplementedError("write me")
