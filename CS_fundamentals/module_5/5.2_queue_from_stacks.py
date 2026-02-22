"""
Exercise 5.2: Queue (and Queue from Two Stacks)

QUEUES
======

A queue is a First-In, First-Out (FIFO) data structure.

Think of a queue at a shop:
- People JOIN at the BACK (enqueue)
- People LEAVE from the FRONT (dequeue)
- First person in line is served first

===================================
KEY OPERATIONS
===================================

    enqueue(item)  - Add item to back      O(1)
    dequeue()      - Remove & return front  O(1)
    front()        - Return front without removing  O(1)
    is_empty()     - Check if queue is empty  O(1)
    size()         - Return number of items   O(1)

===================================
STACK vs QUEUE
===================================

    Stack (LIFO):  Last in, first out   [1, 2, 3] -> pop() = 3
    Queue (FIFO):  First in, first out  [1, 2, 3] -> dequeue() = 1

===================================
REAL-WORLD USE CASES
===================================

1. Print job queue
2. Task scheduling (CPU processes)
3. Breadth-first search (BFS)
4. Message queues (RabbitMQ, SQS)
5. Buffering (streaming data)

===================================
EXERCISE
===================================

PART 1: Implement a Queue class

Class: Queue

Attributes:
- _items: list (internal storage)

Methods:
- __init__(): Initialize empty queue
- enqueue(item) -> None: Add item to back of queue
- dequeue() -> any: Remove and return front item. Raise IndexError("Queue is empty") if empty.
- front() -> any: Return front item without removing. Raise IndexError("Queue is empty") if empty.
- is_empty() -> bool: Return True if queue has no items
- size() -> int: Return number of items
- __str__() -> str: Return string like "Queue([1, 2, 3])" (front to back)

---

PART 2: Queue from Two Stacks (the classic interview question!)

Implement a queue using ONLY two stacks (lists with append/pop only).
You may NOT use deque, indexing, or pop(0).

The trick: One stack for incoming items, one for outgoing items.
When you need to dequeue, move everything from inbox to outbox (reversing the order).

Class: QueueFromStacks

Attributes:
- _inbox: list  (push stack)
- _outbox: list (pop stack)

Methods:
- __init__(): Initialize two empty stacks
- enqueue(item) -> None: Push to inbox
- dequeue() -> any: Pop from outbox. If outbox empty, move all from inbox first.
    Raise IndexError("Queue is empty") if both stacks empty.
- front() -> any: Like dequeue but don't remove.
    Raise IndexError("Queue is empty") if both stacks empty.
- is_empty() -> bool
- size() -> int

WHY THIS WORKS:
    enqueue(1), enqueue(2), enqueue(3)
    inbox: [1, 2, 3]   outbox: []

    dequeue():
    1. Outbox empty -> move all from inbox to outbox
       inbox: []  outbox: [3, 2, 1]  (reversed!)
    2. Pop from outbox -> 1 (correct! FIFO)
       inbox: []  outbox: [3, 2]

    dequeue():
    1. Outbox not empty -> just pop
    2. Pop from outbox -> 2 (correct!)

AMORTISED O(1): Each element is moved at most once from inbox to outbox.

ESTIMATED TIME: 30-45 minutes
"""


# ============================================
# PART 1: Queue Class
# ============================================

# YOUR CODE HERE


# ============================================
# PART 2: Queue from Two Stacks
# ============================================

# YOUR CODE HERE


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    # ==========================================
    # PART 1 TESTS: Queue
    # ==========================================
    print("\n=== Test 1: Queue - Basic Operations ===")
    try:
        q = Queue()
        assert q.is_empty() == True
        assert q.size() == 0

        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        assert q.is_empty() == False
        assert q.size() == 3
        assert q.front() == 1  # First in
        assert q.size() == 3   # front doesn't remove

        print("  Basic operations work")
        print("Test 1 PASSED!")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")
    except Exception as e:
        print(f"Test 1 ERROR: {e}")

    print("\n=== Test 2: Queue - FIFO Order ===")
    try:
        q = Queue()
        q.enqueue("a")
        q.enqueue("b")
        q.enqueue("c")

        assert q.dequeue() == "a"  # First in, first out
        assert q.dequeue() == "b"
        assert q.dequeue() == "c"
        assert q.is_empty() == True

        print("  FIFO order confirmed")
        print("Test 2 PASSED!")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 ERROR: {e}")

    print("\n=== Test 3: Queue - Error Handling ===")
    try:
        q = Queue()

        try:
            q.dequeue()
            assert False, "Should raise IndexError"
        except IndexError as e:
            assert "empty" in str(e).lower()

        try:
            q.front()
            assert False, "Should raise IndexError"
        except IndexError as e:
            assert "empty" in str(e).lower()

        print("  Empty queue errors handled correctly")
        print("Test 3 PASSED!")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 ERROR: {e}")

    print("\n=== Test 4: Queue - __str__ ===")
    try:
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        assert str(q) == "Queue([1, 2, 3])"

        print("  String representation correct")
        print("Test 4 PASSED!")
    except AssertionError as e:
        print(f"Test 4 FAILED: {e}")
    except Exception as e:
        print(f"Test 4 ERROR: {e}")

    print("\n=== Test 5: Queue - Interleaved Operations ===")
    try:
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        assert q.dequeue() == 1
        q.enqueue(3)
        assert q.dequeue() == 2
        assert q.dequeue() == 3
        assert q.is_empty() == True

        print("  Interleaved enqueue/dequeue works")
        print("Test 5 PASSED!")
    except AssertionError as e:
        print(f"Test 5 FAILED: {e}")
    except Exception as e:
        print(f"Test 5 ERROR: {e}")

    # ==========================================
    # PART 2 TESTS: Queue from Two Stacks
    # ==========================================
    print("\n=== Test 6: QueueFromStacks - FIFO ===")
    try:
        q = QueueFromStacks()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        assert q.dequeue() == 1
        assert q.dequeue() == 2
        assert q.dequeue() == 3

        print("  FIFO order using two stacks!")
        print("Test 6 PASSED!")
    except AssertionError as e:
        print(f"Test 6 FAILED: {e}")
    except Exception as e:
        print(f"Test 6 ERROR: {e}")

    print("\n=== Test 7: QueueFromStacks - Interleaved ===")
    try:
        q = QueueFromStacks()
        q.enqueue(1)
        q.enqueue(2)
        assert q.dequeue() == 1

        q.enqueue(3)
        q.enqueue(4)
        assert q.dequeue() == 2
        assert q.dequeue() == 3
        assert q.dequeue() == 4

        print("  Interleaved operations work with two stacks")
        print("Test 7 PASSED!")
    except AssertionError as e:
        print(f"Test 7 FAILED: {e}")
    except Exception as e:
        print(f"Test 7 ERROR: {e}")

    print("\n=== Test 8: QueueFromStacks - Error Handling ===")
    try:
        q = QueueFromStacks()
        try:
            q.dequeue()
            assert False, "Should raise IndexError"
        except IndexError as e:
            assert "empty" in str(e).lower()

        print("  Empty queue error handled")
        print("Test 8 PASSED!")
    except AssertionError as e:
        print(f"Test 8 FAILED: {e}")
    except Exception as e:
        print(f"Test 8 ERROR: {e}")

    print("\n=== Test 9: QueueFromStacks - Front ===")
    try:
        q = QueueFromStacks()
        q.enqueue(10)
        q.enqueue(20)

        assert q.front() == 10
        assert q.size() == 2  # front doesn't remove
        assert q.front() == 10  # still 10

        print("  Front works without removing")
        print("Test 9 PASSED!")
    except AssertionError as e:
        print(f"Test 9 FAILED: {e}")
    except Exception as e:
        print(f"Test 9 ERROR: {e}")

    print("\n" + "=" * 60)
    print("QUEUE KEY LESSONS")
    print("=" * 60)
    print("""
1. FIFO: First In, First Out
2. Queue from two stacks is a classic interview question
3. The trick: inbox stack + outbox stack = reversed order = FIFO
4. Amortised O(1): each element moves between stacks at most once
5. Real queues are everywhere: task scheduling, BFS, message queues
""")
    print("=" * 60)
