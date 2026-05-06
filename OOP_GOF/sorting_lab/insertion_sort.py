"""InsertionSort — EXERCISE.

Idea (how a card player sorts a hand):
    Walk left to right. For each element, slide it leftward past every
    larger element until it sits in the right spot among the elements
    already seen. The left side stays sorted at every step.

    Visual:
        [5, 2, 9, 1, 7]   start
        [2, 5, 9, 1, 7]   insert 2 into [5]
        [2, 5, 9, 1, 7]   9 stays — already in place
        [1, 2, 5, 9, 7]   insert 1 — slides past 9, 5, 2
        [1, 2, 5, 7, 9]   insert 7 — slides past 9

Complexity:
    Time:  O(n^2) worst/average, O(n) best (already sorted).
    Space: O(1) — in place.

Why this beats bubble in practice:
    On nearly-sorted data, each element shifts very few times — close to
    linear. Bubble does the same comparisons either way (no early gain
    inside a pass). Insertion is the standard "small-input" sort that
    library sorts (Timsort, Introsort) fall back to for tiny sub-arrays.

TODO:
    Implement `sort`. Do not mutate `data` — copy first, then work on the
    copy. Look at BubbleSort if you want a template for the "copy then
    return" pattern.
"""

from sorter import Sorter


class InsertionSort(Sorter):
    @property
    def name(self) -> str:
        return "InsertionSort"

    def sort(self, data: list[int]) -> list[int]:
        # TODO: your implementation here.
        raise NotImplementedError("write me")
