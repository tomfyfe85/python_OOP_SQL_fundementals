"""Module 01 — Tests for capstone.py.

Run from this directory:
    pytest test_capstone.py -v

Tests will fail with ImportError until you define Book and Library in
capstone.py. Implement, run, watch the red turn green.
"""

import pytest

from capstone import Book, Library


# =============================================================================
# Book
# =============================================================================


def test_book_describe_format() -> None:
    b = Book("The Pragmatic Programmer", "Hunt & Thomas", "9780201616224")
    text = b.describe()
    assert "The Pragmatic Programmer" in text
    assert "Hunt & Thomas" in text
    assert "9780201616224" in text


def test_book_starts_not_borrowed() -> None:
    b = Book("Clean Code", "Robert Martin", "9780132350884")
    assert b.is_borrowed is False


# =============================================================================
# Library — adding and describing
# =============================================================================


def _sample_books() -> list[Book]:
    return [
        Book("The Pragmatic Programmer", "Hunt & Thomas", "9780201616224"),
        Book("Clean Code", "Robert Martin", "9780132350884"),
        Book("Design Patterns", "Gamma et al.", "9780201633610"),
    ]


def test_library_describe_empty() -> None:
    lib = Library("Camden Branch")
    text = lib.describe()
    assert "Camden Branch" in text
    assert "0 total" in text


def test_library_describe_after_adding() -> None:
    lib = Library("Camden Branch")
    for book in _sample_books():
        lib.add_book(book)
    text = lib.describe()
    assert "3 total" in text
    assert "3 available" in text


# =============================================================================
# Library — borrowing
# =============================================================================


def test_library_borrow_returns_the_book() -> None:
    lib = Library("Camden Branch")
    books = _sample_books()
    for b in books:
        lib.add_book(b)
    borrowed = lib.borrow("9780132350884")
    assert borrowed.describe() == books[1].describe()


def test_library_borrow_marks_book_as_borrowed() -> None:
    lib = Library("Camden Branch")
    books = _sample_books()
    for b in books:
        lib.add_book(b)
    lib.borrow("9780132350884")
    assert books[1].is_borrowed is True


def test_library_borrow_unknown_isbn_raises() -> None:
    lib = Library("Camden Branch")
    for b in _sample_books():
        lib.add_book(b)
    with pytest.raises(ValueError):
        lib.borrow("0000000000000")


def test_library_borrow_already_borrowed_raises() -> None:
    lib = Library("Camden Branch")
    for b in _sample_books():
        lib.add_book(b)
    lib.borrow("9780132350884")
    with pytest.raises(ValueError):
        lib.borrow("9780132350884")


# =============================================================================
# Library — returning
# =============================================================================


def test_library_return_book_clears_borrowed_flag() -> None:
    lib = Library("Camden Branch")
    books = _sample_books()
    for b in books:
        lib.add_book(b)
    lib.borrow("9780132350884")
    lib.return_book("9780132350884")
    assert books[1].is_borrowed is False


def test_library_return_unknown_isbn_raises() -> None:
    lib = Library("Camden Branch")
    for b in _sample_books():
        lib.add_book(b)
    with pytest.raises(ValueError):
        lib.return_book("0000000000000")


def test_library_return_book_not_currently_borrowed_raises() -> None:
    lib = Library("Camden Branch")
    for b in _sample_books():
        lib.add_book(b)
    with pytest.raises(ValueError):
        lib.return_book("9780132350884")


# =============================================================================
# Library — available()
# =============================================================================


def test_library_available_excludes_borrowed_book() -> None:
    lib = Library("Camden Branch")
    for b in _sample_books():
        lib.add_book(b)
    lib.borrow("9780132350884")
    available = lib.available()
    assert len(available) == 2
    isbns = [b.describe() for b in available]
    assert all("9780132350884" not in d for d in isbns)


def test_library_available_includes_returned_book() -> None:
    lib = Library("Camden Branch")
    for b in _sample_books():
        lib.add_book(b)
    lib.borrow("9780132350884")
    lib.return_book("9780132350884")
    assert len(lib.available()) == 3
