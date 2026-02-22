"""
Exercise 4.5: Dependency Inversion Principle (DIP)

DEPENDENCY INVERSION PRINCIPLE

Definition: High-level modules should not depend on low-level modules.
Both should depend on abstractions.

Additionally: Abstractions should not depend on details.
Details should depend on abstractions.

===================================
What does this actually mean?
===================================

"High-level module" = The class that orchestrates/uses other classes
"Low-level module"  = The class that does the actual work (send email, save to DB, etc.)
"Abstraction"       = An ABC/interface that defines WHAT to do, not HOW

===================================
BAD APPROACH (violates DIP)
===================================

    class EmailSender:
        def send(self, to: str, message: str) -> str:
            return f"Email sent to {to}: {message}"

    class OrderProcessor:
        def __init__(self):
            self.notifier = EmailSender()  # DIRECTLY creates EmailSender!

        def process_order(self, order_id: str) -> str:
            return self.notifier.send("customer", f"Order {order_id} confirmed")

Problems:
1. OrderProcessor is TIGHTLY COUPLED to EmailSender
2. Want to switch to SMS? Must MODIFY OrderProcessor
3. Can't test OrderProcessor without also testing EmailSender
4. Violates OCP too - adding notification types means changing existing code

===================================
GOOD APPROACH (follows DIP)
===================================

    from abc import ABC, abstractmethod

    # The ABSTRACTION - both high and low level depend on this
    class MessageSender(ABC):
        @abstractmethod
        def send(self, to: str, message: str) -> str:
            pass

    # LOW-LEVEL modules implement the abstraction
    class EmailSender(MessageSender):
        def send(self, to: str, message: str) -> str:
            return f"[Email] to {to}: {message}"

    class SMSSender(MessageSender):
        def send(self, to: str, message: str) -> str:
            return f"[SMS] to {to}: {message}"

    # HIGH-LEVEL module depends on the abstraction, NOT the concrete class
    class OrderProcessor:
        def __init__(self, notifier: MessageSender):  # INJECTED!
            self.notifier = notifier

        def process_order(self, order_id: str) -> str:
            return self.notifier.send("customer", f"Order {order_id} confirmed")

    # Now we can swap implementations without changing OrderProcessor:
    processor_email = OrderProcessor(EmailSender())
    processor_sms = OrderProcessor(SMSSender())

Benefits:
1. OrderProcessor doesn't know or care HOW messages are sent
2. Swap implementations by passing a different object
3. Easy to test - pass a mock/fake sender
4. Adding new senders doesn't touch OrderProcessor at all

===================================
THE KEY DIFFERENCE FROM ISP
===================================

ISP: "Split FAT interfaces so classes don't implement what they don't need"
DIP: "Don't create dependencies directly - INJECT them through abstractions"

ISP is about interface DESIGN. DIP is about how classes CONNECT to each other.

===================================
EXERCISE: Notification System
===================================

You're building a notification system for an app. Users can receive
notifications via different channels, and messages can be stored in
different backends.

PART 1: Create the Abstractions

Create two ABCs:

    class NotificationChannel(ABC):
        @abstractmethod
        def send(self, recipient: str, message: str) -> str:
            '''Send a message to a recipient. Return confirmation string.'''

    class MessageStore(ABC):
        @abstractmethod
        def save(self, recipient: str, message: str) -> None:
            '''Save a message for a recipient.'''

        @abstractmethod
        def get_messages(self, recipient: str) -> list[str]:
            '''Return all saved messages for a recipient.'''

---

PART 2: Create Concrete Implementations

Notification channels:

    class EmailChannel(NotificationChannel):
        send() returns: "[Email] to {recipient}: {message}"

    class SMSChannel(NotificationChannel):
        send() returns: "[SMS] to {recipient}: {message}"

    class PushChannel(NotificationChannel):
        send() returns: "[Push] to {recipient}: {message}"

Message stores:

    class InMemoryStore(MessageStore):
        - Uses a dict internally: {recipient: [messages]}
        - save() appends message to that recipient's list
        - get_messages() returns the list (empty list if no messages)

---

PART 3: NotificationService (the high-level module)

This is where DIP matters! NotificationService should NOT create its
own channels or store. They should be INJECTED via the constructor.

Class: NotificationService

    def __init__(self, channel: NotificationChannel, store: MessageStore):
        # Store the injected dependencies

    def notify(self, recipient: str, message: str) -> str:
        # 1. Save the message using the store
        # 2. Send the message using the channel
        # 3. Return the result from send()

    def get_history(self, recipient: str) -> list[str]:
        # Return all messages for a recipient from the store

---

PART 4 (HARD): MultiChannelService

Like NotificationService, but sends to MULTIPLE channels at once.

Class: MultiChannelService

    def __init__(self, channels: list[NotificationChannel], store: MessageStore):
        # Store the injected dependencies

    def notify(self, recipient: str, message: str) -> list[str]:
        # 1. Save the message using the store
        # 2. Send via ALL channels
        # 3. Return list of results from each channel

    def notify_channel(self, recipient: str, message: str, channel_type: type) -> str | None:
        # Send via a SPECIFIC channel type only
        # Use isinstance() to find the matching channel (ISP callback!)
        # Return the result, or None if no matching channel

    def get_history(self, recipient: str) -> list[str]:
        # Return all messages for a recipient from the store

---

LEARNING OBJECTIVES:

1. Understand why tight coupling is problematic
2. Learn to inject dependencies through constructors
3. See how DIP enables swapping implementations
4. Recognise how DIP, OCP, and ISP work together
5. Practice dependency injection in Python

ESTIMATED TIME: 30-45 minutes
"""

from abc import ABC, abstractmethod


# ============================================
# PART 1: Abstractions (ABCs)
# ============================================

# YOUR CODE HERE


# ============================================
# PART 2: Concrete Implementations
# ============================================

# YOUR CODE HERE


# ============================================
# PART 3: NotificationService
# ============================================

# YOUR CODE HERE


# ============================================
# PART 4 (HARD): MultiChannelService
# ============================================

# YOUR CODE HERE


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    # ==========================================
    # PART 1 TESTS: Abstractions exist
    # ==========================================
    print("\n=== Test 1: Abstractions are ABCs ===")
    try:
        assert issubclass(NotificationChannel, ABC)
        assert issubclass(MessageStore, ABC)
        print("  NotificationChannel and MessageStore are ABCs")

        # Can't instantiate ABCs directly
        try:
            NotificationChannel()
            assert False, "Should not be able to instantiate ABC"
        except TypeError:
            print("  Cannot instantiate NotificationChannel directly")

        try:
            MessageStore()
            assert False, "Should not be able to instantiate ABC"
        except TypeError:
            print("  Cannot instantiate MessageStore directly")

        print("All Part 1 tests PASSED!")
    except AssertionError as e:
        print(f"Part 1 FAILED: {e}")
    except Exception as e:
        print(f"Part 1 ERROR: {e}")

    # ==========================================
    # PART 2 TESTS: Concrete implementations
    # ==========================================
    print("\n=== Test 2: Notification Channels ===")
    try:
        email = EmailChannel()
        sms = SMSChannel()
        push = PushChannel()

        assert isinstance(email, NotificationChannel)
        assert isinstance(sms, NotificationChannel)
        assert isinstance(push, NotificationChannel)

        assert email.send("alice", "Hello") == "[Email] to alice: Hello"
        assert sms.send("bob", "Hi") == "[SMS] to bob: Hi"
        assert push.send("charlie", "Hey") == "[Push] to charlie: Hey"

        print("  All channels work correctly")
        print("All Part 2a tests PASSED!")
    except AssertionError as e:
        print(f"Part 2a FAILED: {e}")
    except Exception as e:
        print(f"Part 2a ERROR: {e}")

    print("\n=== Test 3: Message Store ===")
    try:
        store = InMemoryStore()
        assert isinstance(store, MessageStore)

        # Empty at first
        assert store.get_messages("alice") == []

        # Save some messages
        store.save("alice", "Hello")
        store.save("alice", "World")
        store.save("bob", "Hi")

        assert store.get_messages("alice") == ["Hello", "World"]
        assert store.get_messages("bob") == ["Hi"]
        assert store.get_messages("charlie") == []

        print("  InMemoryStore works correctly")
        print("All Part 2b tests PASSED!")
    except AssertionError as e:
        print(f"Part 2b FAILED: {e}")
    except Exception as e:
        print(f"Part 2b ERROR: {e}")

    # ==========================================
    # PART 3 TESTS: NotificationService
    # ==========================================
    print("\n=== Test 4: NotificationService with Email ===")
    try:
        store = InMemoryStore()
        service = NotificationService(EmailChannel(), store)

        result = service.notify("alice", "Your order shipped")
        assert result == "[Email] to alice: Your order shipped"
        assert store.get_messages("alice") == ["Your order shipped"]

        print("  Email notification sent and stored")

        result2 = service.notify("alice", "Your order arrived")
        assert store.get_messages("alice") == ["Your order shipped", "Your order arrived"]

        print("  Multiple notifications stored correctly")
        print("All Part 3a tests PASSED!")
    except AssertionError as e:
        print(f"Part 3a FAILED: {e}")
    except Exception as e:
        print(f"Part 3a ERROR: {e}")

    print("\n=== Test 5: NotificationService with SMS (swap!) ===")
    try:
        store = InMemoryStore()
        service = NotificationService(SMSChannel(), store)

        result = service.notify("bob", "Code: 1234")
        assert result == "[SMS] to bob: Code: 1234"
        assert store.get_messages("bob") == ["Code: 1234"]

        print("  SMS notification - same service, different channel!")
        print("  THIS is DIP: we changed behavior without changing NotificationService")
        print("All Part 3b tests PASSED!")
    except AssertionError as e:
        print(f"Part 3b FAILED: {e}")
    except Exception as e:
        print(f"Part 3b ERROR: {e}")

    print("\n=== Test 6: NotificationService history ===")
    try:
        store = InMemoryStore()
        service = NotificationService(EmailChannel(), store)

        service.notify("alice", "Message 1")
        service.notify("alice", "Message 2")
        service.notify("bob", "Message 3")

        assert service.get_history("alice") == ["Message 1", "Message 2"]
        assert service.get_history("bob") == ["Message 3"]
        assert service.get_history("charlie") == []

        print("  History retrieval works")
        print("All Part 3c tests PASSED!")
    except AssertionError as e:
        print(f"Part 3c FAILED: {e}")
    except Exception as e:
        print(f"Part 3c ERROR: {e}")

    # ==========================================
    # PART 4 TESTS (HARD): MultiChannelService
    # ==========================================

    # Uncomment when ready:

    # print("\n=== Test 7: MultiChannelService - notify all ===")
    # try:
    #     store = InMemoryStore()
    #     multi = MultiChannelService(
    #         [EmailChannel(), SMSChannel(), PushChannel()],
    #         store
    #     )
    #
    #     results = multi.notify("alice", "Big announcement")
    #     assert len(results) == 3
    #     assert "[Email] to alice: Big announcement" in results
    #     assert "[SMS] to alice: Big announcement" in results
    #     assert "[Push] to alice: Big announcement" in results
    #     assert store.get_messages("alice") == ["Big announcement"]
    #
    #     print("  Sent via all 3 channels, stored once")
    #     print("All Part 4a tests PASSED!")
    # except AssertionError as e:
    #     print(f"Part 4a FAILED: {e}")
    # except Exception as e:
    #     print(f"Part 4a ERROR: {e}")

    # print("\n=== Test 8: MultiChannelService - notify specific channel ===")
    # try:
    #     store = InMemoryStore()
    #     multi = MultiChannelService(
    #         [EmailChannel(), SMSChannel()],
    #         store
    #     )
    #
    #     result = multi.notify_channel("bob", "Email only", EmailChannel)
    #     assert result == "[Email] to bob: Email only"
    #
    #     result = multi.notify_channel("bob", "SMS only", SMSChannel)
    #     assert result == "[SMS] to bob: SMS only"
    #
    #     # Channel type not in service
    #     result = multi.notify_channel("bob", "Push?", PushChannel)
    #     assert result is None
    #
    #     print("  Specific channel targeting works")
    #     print("All Part 4b tests PASSED!")
    # except AssertionError as e:
    #     print(f"Part 4b FAILED: {e}")
    # except Exception as e:
    #     print(f"Part 4b ERROR: {e}")

    # print("\n=== Test 9: MultiChannelService - history ===")
    # try:
    #     store = InMemoryStore()
    #     multi = MultiChannelService([EmailChannel(), SMSChannel()], store)
    #
    #     multi.notify("alice", "First")
    #     multi.notify("alice", "Second")
    #
    #     assert multi.get_history("alice") == ["First", "Second"]
    #     assert multi.get_history("bob") == []
    #
    #     print("  History works with multi-channel")
    #     print("All Part 4c tests PASSED!")
    # except AssertionError as e:
    #     print(f"Part 4c FAILED: {e}")
    # except Exception as e:
    #     print(f"Part 4c ERROR: {e}")

    # ==========================================
    # KEY LESSONS
    # ==========================================
    print("\n" + "=" * 60)
    print("DIP KEY LESSONS")
    print("=" * 60)
    print("""
1. HIGH-LEVEL modules should not create their own dependencies
   - NotificationService doesn't create EmailChannel()
   - It receives whatever channel you INJECT

2. BOTH levels depend on ABSTRACTIONS
   - NotificationService depends on NotificationChannel (ABC)
   - EmailChannel implements NotificationChannel (ABC)
   - Neither knows about the other!

3. DIP enables SWAPPING implementations
   - Same NotificationService works with Email, SMS, Push
   - Just pass a different object at construction time

4. DIP + OCP + ISP work together
   - DIP: Inject dependencies through abstractions
   - OCP: Add new channels without modifying existing code
   - ISP: Each abstraction is focused on one capability
""")
    print("=" * 60)
