"""
Exercise 8.4: Observer Pattern

OBSERVER PATTERN (Behavioural)
==============================

Define a one-to-many relationship between objects so that when one object
(the subject) changes state, all its dependents (observers) are notified
and updated automatically.

===================================
WHY USE OBSERVER?
===================================

Without observer:
    def update_price(product, new_price):
        product.price = new_price
        send_email_alert(product)      # Hardcoded!
        update_dashboard(product)       # Hardcoded!
        log_price_change(product)       # Hardcoded!
        # Adding new reaction = modifying this function

With observer:
    product.add_observer(email_alerter)
    product.add_observer(dashboard_updater)
    product.add_observer(logger)

    product.set_price(new_price)  # All observers notified automatically!
    # Adding new reaction = just add_observer(). No code changes.

===================================
REAL-WORLD EXAMPLES
===================================

- YouTube: Subscribe to a channel -> notified of new videos
- Event listeners: button.addEventListener("click", handler)
- Stock market: Price changes -> all watchers notified
- MVC: Model changes -> View updates automatically

===================================
EXERCISE
===================================

PART 1: Event System

    class EventEmitter:
        A simple event system (like JavaScript's EventEmitter).

        __init__: Set up _listeners as empty dict.
            Key = event name (str), Value = list of callback functions.

        on(event: str, callback: callable) -> None:
            Register a callback for an event.

        off(event: str, callback: callable) -> None:
            Remove a callback for an event. Ignore if not found.

        emit(event: str, *args, **kwargs) -> None:
            Call all callbacks registered for this event,
            passing along any args/kwargs.

        listener_count(event: str) -> int:
            Return number of listeners for an event.

---

PART 2: Stock Price Observer

    class StockObserver(ABC):
        @abstractmethod
        def update(self, stock_name: str, price: float) -> None: ...

    class Stock:
        __init__(self, name: str, price: float):
            Store name, price, and _observers (empty list).

        add_observer(self, observer: StockObserver) -> None:
            Add an observer.

        remove_observer(self, observer: StockObserver) -> None:
            Remove an observer. Ignore if not found.

        set_price(self, price: float) -> None:
            Update the price and notify all observers.
            Only notify if the price actually changed.

        notify(self) -> None:
            Call update(self.name, self.price) on all observers.

    class PriceLogger(StockObserver):
        __init__: Set up _log as empty list.

        update(stock_name, price):
            Append f"{stock_name}: ${price:.2f}" to _log.

        get_log() -> list[str]:
            Return the log.

    class PriceAlertObserver(StockObserver):
        __init__(self, threshold: float):
            Store the threshold and _alerts as empty list.

        update(stock_name, price):
            If price >= threshold, append
            f"ALERT: {stock_name} hit ${price:.2f} (threshold: ${threshold:.2f})"
            to _alerts.

        get_alerts() -> list[str]:
            Return the alerts.

---

PART 3 (HARD): Newsletter System

    class Subscriber(ABC):
        @abstractmethod
        def receive(self, topic: str, message: str) -> None: ...

    class Newsletter:
        __init__(self, name: str):
            Store name and _subscribers as empty dict.
            Key = topic (str), Value = list of Subscriber.

        subscribe(self, topic: str, subscriber: Subscriber) -> None:
            Subscribe to a specific topic.

        unsubscribe(self, topic: str, subscriber: Subscriber) -> None:
            Unsubscribe from a topic. Ignore if not found.

        publish(self, topic: str, message: str) -> None:
            Notify all subscribers of the given topic.

        get_topics(self) -> list[str]:
            Return list of all topics that have subscribers.

    class EmailSubscriber(Subscriber):
        __init__(self, email: str):
            Store email and _inbox as empty list.

        receive(topic, message):
            Append {"topic": topic, "message": message} to _inbox.

        get_inbox() -> list[dict]:
            Return the inbox.

ESTIMATED TIME: 30-45 minutes
"""

from abc import ABC, abstractmethod


# ============================================
# PART 1: Event System
# ============================================

# YOUR CODE HERE


# ============================================
# PART 2: Stock Price Observer
# ============================================

# YOUR CODE HERE


# ============================================
# PART 3 (HARD): Newsletter System
# ============================================

# YOUR CODE HERE


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    # ==========================================
    # PART 1 TESTS: Event System
    # ==========================================
    print("\n=== Test 1: EventEmitter Basic ===")
    try:
        emitter = EventEmitter()
        results = []

        def on_click(x, y):
            results.append(f"Clicked at ({x}, {y})")

        def on_click_log(x, y):
            results.append(f"Logged click at ({x}, {y})")

        emitter.on("click", on_click)
        emitter.on("click", on_click_log)

        assert emitter.listener_count("click") == 2

        emitter.emit("click", 10, 20)
        assert len(results) == 2
        assert results[0] == "Clicked at (10, 20)"
        assert results[1] == "Logged click at (10, 20)"

        print(f"  Emitted 'click' -> {len(results)} listeners fired")
        print("Test 1 PASSED!")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")
    except Exception as e:
        print(f"Test 1 ERROR: {e}")

    print("\n=== Test 2: EventEmitter Off ===")
    try:
        emitter = EventEmitter()
        results = []

        def handler(msg):
            results.append(msg)

        emitter.on("data", handler)
        emitter.emit("data", "first")
        assert len(results) == 1

        emitter.off("data", handler)
        emitter.emit("data", "second")
        assert len(results) == 1, "Handler should have been removed"

        assert emitter.listener_count("data") == 0

        print("  off() correctly removes listeners")
        print("Test 2 PASSED!")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 ERROR: {e}")

    print("\n=== Test 3: EventEmitter Multiple Events ===")
    try:
        emitter = EventEmitter()
        clicks = []
        hovers = []

        emitter.on("click", lambda: clicks.append(1))
        emitter.on("hover", lambda: hovers.append(1))

        emitter.emit("click")
        emitter.emit("click")
        emitter.emit("hover")

        assert len(clicks) == 2
        assert len(hovers) == 1

        # Emitting unknown event should not error
        emitter.emit("unknown_event")

        print("  Multiple events work independently")
        print("Test 3 PASSED!")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 ERROR: {e}")

    # ==========================================
    # PART 2 TESTS: Stock Observer
    # ==========================================
    print("\n=== Test 4: Stock with Logger ===")
    try:
        stock = Stock("AAPL", 150.00)
        logger = PriceLogger()

        stock.add_observer(logger)
        stock.set_price(155.50)
        stock.set_price(160.00)

        log = logger.get_log()
        assert len(log) == 2
        assert log[0] == "AAPL: $155.50"
        assert log[1] == "AAPL: $160.00"

        print(f"  Price log: {log}")
        print("Test 4 PASSED!")
    except AssertionError as e:
        print(f"Test 4 FAILED: {e}")
    except Exception as e:
        print(f"Test 4 ERROR: {e}")

    print("\n=== Test 5: Stock with Alert Observer ===")
    try:
        stock = Stock("TSLA", 200.00)
        alert = PriceAlertObserver(250.00)
        logger = PriceLogger()

        stock.add_observer(alert)
        stock.add_observer(logger)

        stock.set_price(220.00)  # Below threshold - no alert
        stock.set_price(250.00)  # At threshold - alert!
        stock.set_price(280.00)  # Above threshold - alert!

        alerts = alert.get_alerts()
        assert len(alerts) == 2
        assert "250.00" in alerts[0]
        assert "280.00" in alerts[1]

        # Logger should have all 3 changes
        assert len(logger.get_log()) == 3

        print(f"  Alerts triggered: {len(alerts)}")
        print("Test 5 PASSED!")
    except AssertionError as e:
        print(f"Test 5 FAILED: {e}")
    except Exception as e:
        print(f"Test 5 ERROR: {e}")

    print("\n=== Test 6: No Notification on Same Price ===")
    try:
        stock = Stock("GOOG", 100.00)
        logger = PriceLogger()
        stock.add_observer(logger)

        stock.set_price(100.00)  # Same price - should NOT notify
        assert len(logger.get_log()) == 0

        stock.set_price(105.00)  # Different price - should notify
        assert len(logger.get_log()) == 1

        print("  No notification when price unchanged")
        print("Test 6 PASSED!")
    except AssertionError as e:
        print(f"Test 6 FAILED: {e}")
    except Exception as e:
        print(f"Test 6 ERROR: {e}")

    # ==========================================
    # PART 3 TESTS (HARD): Uncomment when ready
    # ==========================================

    # print("\n=== Test 7: Newsletter Subscribe ===")
    # try:
    #     news = Newsletter("Tech Weekly")
    #     alice = EmailSubscriber("alice@mail.com")
    #     bob = EmailSubscriber("bob@mail.com")
    #
    #     news.subscribe("python", alice)
    #     news.subscribe("python", bob)
    #     news.subscribe("javascript", bob)
    #
    #     news.publish("python", "Python 4.0 released!")
    #     news.publish("javascript", "Deno 3.0 is here!")
    #
    #     assert len(alice.get_inbox()) == 1
    #     assert alice.get_inbox()[0] == {"topic": "python", "message": "Python 4.0 released!"}
    #
    #     assert len(bob.get_inbox()) == 2  # Subscribed to both
    #
    #     print(f"  Alice inbox: {len(alice.get_inbox())} messages")
    #     print(f"  Bob inbox: {len(bob.get_inbox())} messages")
    #     print("Test 7 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 7 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 7 ERROR: {e}")

    # print("\n=== Test 8: Newsletter Unsubscribe ===")
    # try:
    #     news = Newsletter("Science Daily")
    #     sub = EmailSubscriber("reader@mail.com")
    #
    #     news.subscribe("physics", sub)
    #     news.publish("physics", "New particle found!")
    #     assert len(sub.get_inbox()) == 1
    #
    #     news.unsubscribe("physics", sub)
    #     news.publish("physics", "Another discovery!")
    #     assert len(sub.get_inbox()) == 1, "Should not receive after unsubscribe"
    #
    #     topics = news.get_topics()
    #     assert "physics" not in topics or len(topics) == 0
    #
    #     print("  Unsubscribe works correctly")
    #     print("Test 8 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 8 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 8 ERROR: {e}")

    print("\n" + "=" * 60)
    print("OBSERVER PATTERN KEY LESSONS")
    print("=" * 60)
    print("""
1. Observer creates a one-to-many relationship
2. Subject maintains a list of observers and notifies them
3. Observers register/unregister themselves
4. Loose coupling: subject doesn't know observer details
5. Adding new reactions = add observer, no code changes (OCP)
6. EventEmitter is a general-purpose observer implementation
7. Real-world: event listeners, pub/sub, MVC, reactive programming
""")
    print("=" * 60)
