"""Sorter — the abstract interface every sorting algorithm implements.

Python's equivalent of a Java `interface` is `abc.ABC` plus `@abstractmethod`.
Subclasses MUST override every abstract method or instantiation fails at
runtime. That is the contract.

Why an interface here?
    Sorting is a perfect example of the Strategy pattern: many different
    algorithms, one common shape (`sort(list) -> list`). By depending on
    `Sorter` instead of any concrete class, the rest of the program does
    not care whether it is bubble-sorting or quick-sorting — it just calls
    `.sort(...)`. Swap the strategy without touching the caller.
"""

from abc import ABC, abstractmethod


class Sorter(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable name. Used by benchmarks and demos."""

    @abstractmethod
    def sort(self, data: list[int]) -> list[int]:
        """Return a NEW sorted list. Implementations must not mutate `data`.

        The non-mutation rule lets us run every sorter against the same
        input in the benchmark without each one stepping on the next.
        """
