"""Module 01 — Capstone: Library Book System.

Two classes that collaborate. This is your first taste of object collaboration —
two classes working together, each owning its own state.

Workflow:
    pytest test_capstone.py -v        # run tests, watch them fail then pass
    mypy --strict capstone.py         # check types
    python capstone.py                # optional: run main() for ad-hoc demo


Requirements
------------

Class `Book`:
  - Constructor: title: str, author: str, isbn: str
  - Attribute `is_borrowed: bool` defaults to False
  - Method `describe() -> str` returns "Title by Author (ISBN: 9781234567890)"

Class `Library`:
  - Constructor takes name: str. Initialise an empty list of books internally.
  - Method `add_book(book: Book) -> None`
        Append the book to the internal list.
  - Method `borrow(isbn: str) -> Book`
        - Find the book by ISBN.
        - If not found: raise ValueError with a message that includes the ISBN.
        - If found but already borrowed: raise ValueError with a message that
          includes the title.
        - Otherwise mark is_borrowed = True and return the book.
  - Method `return_book(isbn: str) -> None`
        - Find the book by ISBN.
        - If not found: raise ValueError.
        - If found but not currently borrowed: raise ValueError.
        - Otherwise mark is_borrowed = False.
  - Method `available() -> list[Book]`
        Returns all books currently not borrowed.
  - Method `describe() -> str`
        Returns: "Library 'Name': X total books, Y available"


main():
  - Create a Library named e.g. "Camden Branch"
  - Add at least 3 books
  - Print library.describe()
  - Borrow one book by ISBN
  - Try to borrow that same book again — wrap in try/except, print the error
  - Return the book
  - Print library.describe() again to confirm the count is back to normal


Engineering notes — read these. They are the point of the exercise.
-------------------------------------------------------------------

  1. The `Library` does not touch `Book` attributes from the outside *except*
     through methods or attributes the Book chooses to expose. `Book` owns
     its own state. We're going to formalise that with `@property` in
     Module 02 — for now, just notice the principle.

  2. Validation lives at the boundary. The Library checks "is this ISBN real?"
     and "is it already borrowed?" *before* mutating anything. If you mutate
     first and check after, you can leave the system in a broken state when
     the check fails.

  3. Error messages are specific. "Book with ISBN '9781234567890' not found
     in Library 'Camden Branch'" beats "not found". You will be the one
     reading these errors at 11pm in three months.

  4. Every method has full type annotations. Run `mypy --strict capstone.py`
     when you're done. It should pass with zero errors.

  5. Note that `borrow` returns a `Book` and `return_book` returns `None`.
     That is a deliberate API design choice: borrow gives the caller back a
     reference to use; returning is a void operation on the library. Pay
     attention to return types — they communicate intent.
"""


# YOUR CODE HERE


def main() -> None:
    pass


if __name__ == "__main__":
    main()
