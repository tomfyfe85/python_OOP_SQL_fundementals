"""QuickSort — EXERCISE (the second classic divide-and-conquer sort).

Idea:
    1. Pick a "pivot" element from the list.
    2. PARTITION: rearrange so everything <= pivot is on its left and
       everything > pivot is on its right. The pivot is now in its final
       position.
    3. Recursively quicksort the left chunk and the right chunk.

Complexity:
    Time:  O(n log n) average — like mergesort.
           O(n^2)     worst   — happens when the pivot is repeatedly the
                                smallest or largest element. Classic
                                trigger: always picking arr[0] on an
                                already-sorted input.
    Space: O(log n) average for the recursion stack (no merge buffer).

QuickSort vs MergeSort:
    Same average complexity, but quicksort is usually FASTER in practice:
    it partitions in place (cache-friendly, no allocation) while mergesort
    copies into new lists. That is why most language standard-library
    sorts are quicksort variants — Introsort (C++) switches to heapsort
    on bad pivots; Timsort (Python, Java) is mergesort tuned for
    real-world partly-sorted data.

TODO:
    Implement `sort`. Easiest first version (the "Lomuto" style):

        def _quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[0]                       # or random.choice(arr) — better
            less    = [x for x in arr[1:] if x <= pivot]
            greater = [x for x in arr[1:] if x >  pivot]
            return _quicksort(less) + [pivot] + _quicksort(greater)

    This builds new lists (so it's not strictly O(log n) space), but it's
    the cleanest way to see the algorithm. You can do an in-place version
    later if you want.
"""

from sorter import Sorter


class QuickSort(Sorter):
    @property
    def name(self) -> str:
        return "QuickSort"

    def sort(self, data: list[int]) -> list[int]:
        # TODO: your implementation here.
        raise NotImplementedError("write me")
