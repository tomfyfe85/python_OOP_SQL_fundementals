"""Module 01 — Worked Example: BankAccount.

Read this file top to bottom. The comments explain WHY decisions were made,
not WHAT the code does (the code already shows that).

Run:        python example.py
Type-check: mypy --strict example.py
"""


class BankAccount:
    # __init__ runs when you write `BankAccount(...)`. It sets up state.
    # `self` is the new instance — Python's explicit `this`.
    # `balance: float = 0.0` makes the second argument optional.
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        # Validate at the boundary: a negative starting balance is a bug,
        # not a feature. Refuse it loudly, where the bug is.
        if balance < 0:
            raise ValueError(
                f"starting balance must be non-negative, got {balance}"
            )
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError(
                f"deposit amount must be non-negative, got {amount}"
            )
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount < 0:
            raise ValueError(
                f"withdraw amount must be non-negative, got {amount}"
            )
        # Specific error message — "insufficient funds" alone is useless when
        # debugging. Telling the caller what the balance was and what they
        # tried to take saves time later.
        if amount > self.balance:
            raise ValueError(
                f"insufficient funds: balance={self.balance:.2f}, "
                f"requested={amount:.2f}"
            )
        self.balance -= amount

    def describe(self) -> str:
        return f"{self.owner}'s account: £{self.balance:.2f}"


def main() -> None:
    alice = BankAccount("Alice", 100.0)
    bob = BankAccount("Bob")  # default balance 0.0

    alice.deposit(50.0)
    alice.withdraw(30.0)
    bob.deposit(200.0)

    print(alice.describe())
    print(bob.describe())

    # Show that validation works. We expect this to raise.
    try:
        alice.withdraw(10_000.0)
    except ValueError as err:
        print(f"caught expected error: {err}")


if __name__ == "__main__":
    main()
