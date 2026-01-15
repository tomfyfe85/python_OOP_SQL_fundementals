"""
Exercise 4.3: Liskov Substitution Principle (LSP)

LISKOV SUBSTITUTION PRINCIPLE (LSP)

Definition: Objects of a superclass should be replaceable with objects of a subclass
WITHOUT breaking the application or changing expected behavior.

KEY INSIGHT: LSP is about BEHAVIORAL compatibility, not just method signatures!

===================================
LSP vs ABC (What you already know)
===================================

ABC: "Does the child implement all required methods?" ✓
LSP: "Does the child BEHAVE correctly when substituted?" ✓

You can satisfy ABC but still violate LSP!

Example - Violates LSP but satisfies ABC:

    class Bird(ABC):
        @abstractmethod
        def fly(self) -> str:
            pass

    class Sparrow(Bird):
        def fly(self) -> str:
            return "Flying!"  # ✓ Works

    class Penguin(Bird):
        def fly(self) -> str:
            raise Exception("Can't fly!")  # ABC ✓, LSP ✗

    def migrate(bird: Bird):
        print(bird.fly())  # Expects to work for ANY Bird!

    migrate(Sparrow())  # ✓ Works
    migrate(Penguin())  # ✗ CRASHES! LSP violated!

Problem: Penguin HAS fly() method (ABC satisfied) but BEHAVIOR is broken.

Solution: Don't make Penguin inherit fly() if it can't actually fly!

    class Bird(ABC):
        @abstractmethod
        def eat(self) -> str:
            pass

    class FlyingBird(Bird):
        @abstractmethod
        def fly(self) -> str:
            pass

    class Penguin(Bird):  # Just Bird, not FlyingBird
        def eat(self) -> str:
            return "Eating fish"
        # No fly() - penguins don't fly!

===================================
LSP VIOLATION PATTERNS
===================================

1. THROWING UNEXPECTED EXCEPTIONS
   Parent: method works
   Child: method throws exception

2. STRENGTHENING PRECONDITIONS
   Parent: accepts 0-100
   Child: only accepts 50-100

3. WEAKENING POSTCONDITIONS
   Parent: always returns positive
   Child: sometimes returns negative

4. CHANGING SIDE EFFECTS
   Parent: set_width() only changes width
   Child: set_width() changes width AND height (Square inheriting Rectangle!)

===================================
EXERCISE: Document Processing System
===================================

You're building a document processing system. Different document types have
different capabilities - some are editable, some are read-only.

THE LSP CHALLENGE:
- All documents can be read
- Only some documents can be edited
- Don't force read-only documents to implement edit methods they can't support!

Step 4: Document Processor (THE CHALLENGE - like StackedDiscount)

Class: DocumentProcessor

This processes documents through multiple transformation functions in sequence.

Methods:
- __init__(*transformers): Accept variable number of transformer functions
  - Each transformer is: Callable[[str], str] (function that takes string, returns string)
  - Store them in a list

- process(document: Document) -> str:
  - Start with document.read()
  - Apply each transformer function in sequence to the content
  - Return the final transformed content
  - Example transformers:
    - uppercase: lambda s: s.upper()
    - remove_spaces: lambda s: s.replace(" ", "")
    - reverse: lambda s: s[::-1]

Example:
    processor = DocumentProcessor(
        lambda s: s.upper(),
        lambda s: s.replace(" ", "_")
    )

    doc = Document("Test", "hello world")
    result = processor.process(doc)  # "HELLO_WORLD"
    # First transformer: "hello world" -> "HELLO WORLD"
    # Second transformer: "HELLO WORLD" -> "HELLO_WORLD"

This is like StackedDiscount where you applied multiple discount strategies
in sequence. Here you're applying multiple transformers in sequence!

---

PART 2: Smart Document Library (HARD - Beyond StackedDiscount)

Create a library that manages documents safely using LSP principles.

Class: DocumentLibrary

Attributes:
- documents: list of Documents (mixed types)

Methods:
- __init__(): Initialize empty list

- add_document(document: Document) -> None:
  Add document to library

- read_document(title: str) -> str | None:
  Find document by title and return its content
  Return None if not found

- edit_document(title: str, new_content: str) -> bool:
  Find document by title
  Check if it's EditableDocument using isinstance()
  If editable: call edit() and return True
  If read-only or not found: return False
  THIS IS THE LSP PATTERN - safely check capabilities!

- bulk_edit(updates: dict[str, str]) -> dict[str, bool]:
  Takes dictionary of {title: new_content}
  Try to edit each document
  Return dictionary of {title: success_bool}
  Example: {"doc1": True, "doc2": False} means doc1 edited, doc2 failed

- get_editable_documents() -> list[EditableDocument]:
  Return list of only editable documents
  Use isinstance() to filter

- get_readonly_documents() -> list[Document]:
  Return list of documents that are NOT EditableDocument
  Use isinstance() with not

- process_all_documents(processor: DocumentProcessor) -> dict[str, str]:
  Process ALL documents (both editable and read-only) through processor
  Return dictionary of {title: processed_content}
  THIS DEMONSTRATES LSP - processor works with ANY Document type!

- get_statistics() -> dict:
  Return:
  {
    "total_documents": int,
    "editable_count": int,
    "readonly_count": int,
    "total_words": int (sum of word counts from all docs),
    "average_words": float (total_words / total_documents)
  }

THE HARD CHALLENGES:
1. isinstance() checks to safely handle different document types
2. bulk_edit processing multiple documents with mixed success
3. Filtering documents by capability (editable vs read-only)
4. process_all_documents demonstrating LSP - works with ANY Document
5. Calculating statistics across mixed document types

This is harder than StackedDiscount because:
- StackedDiscount: Apply strategies to ONE price
- DocumentLibrary: Manage MANY documents of DIFFERENT types
- More isinstance() checks, more edge cases, more complex return types

---

LEARNING OBJECTIVES:

1. LSP is about BEHAVIOR, not just method signatures
2. Don't force child classes to implement methods they can't support
3. Use isinstance() to safely check for specific capabilities
4. Design classes so substitution doesn't break expectations
5. Separate capabilities (editable vs read-only) into different class hierarchies

ESTIMATED TIME: 45-60 minutes
"""

from typing import Callable

# ==========================================
# YOUR CODE GOES BELOW
# ==========================================

class Document():
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def read(self):
        return self.content
    
    def get_word_count(self):
        return len(self.content.split())
    
    def get_info(self):
        return {"title": self.title, "content": self.content, "word_count": self.get_word_count()}


class EditableDocument(Document):
    def edit(self, new_content:str):
        self.content = new_content

    def append(self, text:str):
        self.content = self.content + " " + text



class PDFDocument(Document):
    def __init__(self, title: str, content: str, file_size_kb: float):
        self.title = title
        self.content = content
        self.file_size_kb = file_size_kb

    def get_file_size(self):
        return self.file_size_kb
    
    def get_info(self):
        current_info_dict = super().get_info()
        current_info_dict.update({"file_size_kb": self.file_size_kb, "read_only": True})
        return current_info_dict

class DocumentProcessor:
    pass


class DocumentLibrary:
    pass


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":
    print("\n=== Test 1: Basic Document ===")
    doc = Document("Hello", "hello world test")
    assert doc.read() == "hello world test"
    assert doc.get_word_count() == 3
    info = doc.get_info()
    assert info["title"] == "Hello"
    assert info["word_count"] == 3
    print(f"✓ Document created: {info}")

    print("\n=== Test 2: EditableDocument ===")
    editable = EditableDocument("Editable", "original content")
    assert editable.read() == "original content"

    editable.edit("new content")
    assert editable.read() == "new content"
    print("✓ Edit successful")

    editable.append("more text")
    assert editable.read() == "new content more text"
    print("✓ Append successful")

    print("\n=== Test 3: PDFDocument (Read-only) ===")
    pdf = PDFDocument("Report", "quarterly report data", 125.5)
    assert pdf.read() == "quarterly report data"
    assert pdf.get_file_size() == 125.5
    assert not hasattr(pdf, 'edit'), "PDF should not have edit method"
    assert not hasattr(pdf, 'append'), "PDF should not have append method"
    info = pdf.get_info()
    assert info["read_only"] == True
    assert info["file_size_kb"] == 125.5
    print(f"✓ PDFDocument (read-only): {info}")

    # print("\n=== Test 4: DocumentProcessor - Single Transformer ===")
    # uppercase_processor = DocumentProcessor(lambda s: s.upper())
    # doc1 = Document("Test", "hello world")
    # result = uppercase_processor.process(doc1)
    # assert result == "HELLO WORLD"
    # print(f"✓ Single transformer: '{doc1.read()}' -> '{result}'")

    # print("\n=== Test 5: DocumentProcessor - Multiple Transformers (LIKE STACKED DISCOUNT!) ===")
    # multi_processor = DocumentProcessor(
    #     lambda s: s.upper(),           # First: uppercase
    #     lambda s: s.replace(" ", "_")  # Second: replace spaces
    # )
    # result = multi_processor.process(doc1)
    # assert result == "HELLO_WORLD"
    # print(f"✓ Multiple transformers: '{doc1.read()}' -> '{result}'")

    # print("\n=== Test 6: DocumentProcessor - Three Transformers ===")
    # complex_processor = DocumentProcessor(
    #     lambda s: s.upper(),
    #     lambda s: s.replace(" ", "_"),
    #     lambda s: s + "!!!"
    # )
    # result = complex_processor.process(doc1)
    # assert result == "HELLO_WORLD!!!"
    # print(f"✓ Three transformers: '{doc1.read()}' -> '{result}'")

    # print("\n=== Test 7: DocumentProcessor works with ALL document types (LSP!) ===")
    # processor = DocumentProcessor(lambda s: s.upper())

    # regular = Document("Regular", "test content")
    # editable = EditableDocument("Editable", "test content")
    # pdf = PDFDocument("PDF", "test content", 50.0)

    # # Processor works with ANY Document type - demonstrates LSP!
    # assert processor.process(regular) == "TEST CONTENT"
    # assert processor.process(editable) == "TEST CONTENT"
    # assert processor.process(pdf) == "TEST CONTENT"
    # print("✓ Processor works with all document types (LSP compliant!)")

    # print("\n=== Test 8: DocumentLibrary - Adding Documents ===")
    # library = DocumentLibrary()

    # doc1 = Document("Doc1", "content one")
    # doc2 = EditableDocument("Doc2", "content two")
    # pdf1 = PDFDocument("PDF1", "content three", 100.0)

    # library.add_document(doc1)
    # library.add_document(doc2)
    # library.add_document(pdf1)
    # print("✓ Added 3 documents (1 regular, 1 editable, 1 PDF)")

    # print("\n=== Test 9: DocumentLibrary - Reading ===")
    # content = library.read_document("Doc1")
    # assert content == "content one"
    # print("✓ Read document successfully")

    # assert library.read_document("NonExistent") is None
    # print("✓ Returns None for non-existent document")

    # print("\n=== Test 10: DocumentLibrary - Safe Editing (LSP PATTERN!) ===")
    # # Can edit EditableDocument
    # assert library.edit_document("Doc2", "updated content") == True
    # assert library.read_document("Doc2") == "updated content"
    # print("✓ Successfully edited EditableDocument")

    # # Cannot edit regular Document
    # assert library.edit_document("Doc1", "new content") == False
    # assert library.read_document("Doc1") == "content one"  # Unchanged
    # print("✓ Correctly rejected editing regular Document")

    # # Cannot edit PDFDocument
    # assert library.edit_document("PDF1", "hacked") == False
    # assert library.read_document("PDF1") == "content three"  # Unchanged
    # print("✓ Correctly rejected editing PDF")

    # print("\n=== Test 11: DocumentLibrary - Bulk Edit ===")
    # library2 = DocumentLibrary()
    # library2.add_document(EditableDocument("Edit1", "content"))
    # library2.add_document(EditableDocument("Edit2", "content"))
    # library2.add_document(Document("Regular", "content"))
    # library2.add_document(PDFDocument("PDF", "content", 50.0))

    # results = library2.bulk_edit({
    #     "Edit1": "new1",
    #     "Edit2": "new2",
    #     "Regular": "should fail",
    #     "PDF": "should fail",
    #     "NotFound": "should fail"
    # })

    # assert results["Edit1"] == True
    # assert results["Edit2"] == True
    # assert results["Regular"] == False
    # assert results["PDF"] == False
    # assert results["NotFound"] == False
    # print(f"✓ Bulk edit results: {results}")

    # print("\n=== Test 12: DocumentLibrary - Filtering by Type ===")
    # editable_docs = library2.get_editable_documents()
    # assert len(editable_docs) == 2
    # assert all(isinstance(d, EditableDocument) for d in editable_docs)
    # print(f"✓ Found {len(editable_docs)} editable documents")

    # readonly_docs = library2.get_readonly_documents()
    # assert len(readonly_docs) == 2  # Regular Document + PDFDocument
    # assert all(not isinstance(d, EditableDocument) for d in readonly_docs)
    # print(f"✓ Found {len(readonly_docs)} read-only documents")

    # print("\n=== Test 13: DocumentLibrary - Process All (LSP DEMO!) ===")
    # processor = DocumentProcessor(
    #     lambda s: s.upper(),
    #     lambda s: s[::-1]  # Reverse
    # )

    # results = library2.process_all_documents(processor)
    # assert len(results) == 4
    # assert results["Edit1"] == "1WEN"  # "new1" -> "NEW1" -> "1WEN"
    # assert results["Edit2"] == "2WEN"
    # print(f"✓ Processed all documents (both editable and read-only): {results}")
    # print("  ^ This demonstrates LSP - processor works with ANY document type!")

    # print("\n=== Test 14: DocumentLibrary - Statistics ===")
    # library3 = DocumentLibrary()
    # library3.add_document(Document("D1", "one two three"))  # 3 words
    # library3.add_document(EditableDocument("D2", "four five"))  # 2 words
    # library3.add_document(PDFDocument("D3", "six", 50.0))  # 1 word

    # stats = library3.get_statistics()
    # assert stats["total_documents"] == 3
    # assert stats["editable_count"] == 1
    # assert stats["readonly_count"] == 2
    # assert stats["total_words"] == 6
    # assert stats["average_words"] == 2.0
    # print(f"✓ Statistics: {stats}")

    # print("\n=== Test 15: isinstance() Safety Checks ===")
    # doc = Document("Test", "content")
    # editable = EditableDocument("Test", "content")
    # pdf = PDFDocument("Test", "content", 50.0)

    # assert isinstance(doc, Document)
    # assert not isinstance(doc, EditableDocument)

    # assert isinstance(editable, Document)  # Inherits from Document
    # assert isinstance(editable, EditableDocument)

    # assert isinstance(pdf, Document)  # Inherits from Document
    # assert not isinstance(pdf, EditableDocument)

    # print("✓ All isinstance() checks passed")

    # print("\n✓✓✓ All tests passed! ✓✓✓")

    # print("\n" + "="*60)
    # print("LSP KEY LESSONS")
    # print("="*60)
    # print("\n1. PART 1 (DocumentProcessor):")
    # print("   - Like StackedDiscount: applies multiple transformers in sequence")
    # print("   - Works with ANY Document type (LSP compliant)")
    # print("   - Process: content -> transformer1 -> transformer2 -> result")

    # print("\n2. PART 2 (DocumentLibrary):")
    # print("   - Manages mixed document types safely")
    # print("   - Uses isinstance() to check capabilities before acting")
    # print("   - edit_document: only edits if isinstance(EditableDocument)")
    # print("   - process_all_documents: works with ALL types (LSP!)")

    # print("\n3. LSP vs ABC:")
    # print("   - ABC: 'Does child have required methods?' ✓")
    # print("   - LSP: 'Does child BEHAVE correctly when substituted?' ✓")
    # print("   - PDFDocument doesn't inherit edit() because it can't support it")
    # print("   - This prevents LSP violations (no unexpected exceptions)")

    # print("\n4. The Liskov Substitution Principle:")
    # print("   'Objects of a superclass should be replaceable with objects")
    # print("    of a subclass WITHOUT breaking the application'")
    # print("   - DocumentProcessor.process() works with any Document")
    # print("   - Library safely checks capabilities using isinstance()")
    # print("   - No forced inheritance of unsupported methods")

    # print("="*60)