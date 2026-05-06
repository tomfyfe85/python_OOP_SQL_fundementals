"""BubbleSort — the simplest comparison sort.

Idea:
    Walk the list. Whenever two adjacent elements are out of order, swap
    them. Each full pass "bubbles" the largest unsorted element to its
    final position at the end. Repeat until a pass makes zero swaps.

Complexity:
    Time:  O(n^2) average and worst.
           O(n)   best — already sorted, thanks to the early-exit flag.
    Space: O(1) extra. The work happens in-place on a copy.
"""

from sorter import Sorter


class BubbleSort(Sorter):
    @property
    def name(self) -> str:
        return "BubbleSort"

    def sort(self, data: list[int]) -> list[int]:
        # Copy first — the interface contract forbids mutating the input.
        arr = list(data)
        n = len(arr)

        for i in range(n):
            swapped = False
            # After pass i, the last i elements are already in their final
            # positions, so we stop the inner loop early.
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            # If a full pass made no swaps, the list is sorted. Bail out.
            if not swapped:
                break

        return arr
