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