"""MergeSort — the canonical divide-and-conquer sort.

Idea (the recursion):
    1. If the list has 0 or 1 elements, it is already sorted (base case).
    2. Split it into two halves.
    3. Recursively sort each half.
    4. Merge the two sorted halves into one sorted list.

Why divide-and-conquer wins:
    Merging two already-sorted lists of total length n is O(n) — two
    pointers, one pass. We do that merge work at log2(n) levels of
    recursion (because we halve each time), so the total is O(n log n).
    On 1000 items, n^2 is a million operations; n log n is ~10_000.

Complexity:
    Time:  O(n log n) — best, average, and worst. No worst-case surprise.
    Space: O(n) extra — `_merge` builds new lists.
"""

from sorter import Sorter


class MergeSort(Sorter):
    @property
    def name(self) -> str:
        return "MergeSort"

    def sort(self, data: list[int]) -> list[int]:
        # Public method just kicks off the recursion. Keeping the recursive
        # helper private (`_merge_sort`) means callers see a clean API.
        return self._merge_sort(list(data))

    def _merge_sort(self, arr: list[int]) -> list[int]:
        # Base case: a 0- or 1-element list is sorted by definition.
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self._merge_sort(arr[:mid])
        right = self._merge_sort(arr[mid:])
        return self._merge(left, right)

    def _merge(self, left: list[int], right: list[int]) -> list[int]:
        # Two pointers walking down two already-sorted lists, taking the
        # smaller head each step. This linear merge is the heart of the
        # algorithm — everything else is just recursion bookkeeping.
        merged: list[int] = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # Whichever side still has items left is already sorted on its own,
        # so we can append it wholesale instead of comparing further.
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
