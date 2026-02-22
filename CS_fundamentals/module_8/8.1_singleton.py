"""
Exercise 8.1: Singleton Pattern

SINGLETON PATTERN (Creational)
==============================

Ensure a class has only ONE instance, and provide a global point of access to it.

===================================
WHY USE SINGLETON?
===================================

Some things should only exist once:
- Database connection pool
- Logger
- Configuration manager
- Cache

If you create multiple database connections accidentally, you waste resources
and risk data inconsistency.

===================================
HOW IT WORKS
===================================

    class Singleton:
        _instance = None     # Class-level storage for the single instance

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

    a = Singleton()
    b = Singleton()
    assert a is b  # Same object!

__new__ is called BEFORE __init__. By overriding __new__, we control
object creation itself - returning the existing instance instead of
creating a new one.

===================================
COMMON PITFALL
===================================

__init__ runs EVERY time you call the class, even when __new__ returns
the existing instance. So use a flag to only initialise once:

    class Singleton:
        _instance = None
        _initialised = False

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

        def __init__(self):
            if not self._initialised:
                # Do actual setup here
                self._initialised = True

===================================
EXERCISE
===================================

PART 1: Logger Singleton

Create a Logger that only exists once. Multiple calls to Logger()
should return the same instance.

Class: Logger

    __new__: Ensure only one instance exists.
    __init__: Only initialise once. Set up:
        - _logs: empty list
        - _level: "INFO" (default log level)

    log(message: str, level: str = "INFO") -> None:
        Append a dict to _logs: {"message": message, "level": level}

    get_logs() -> list[dict]:
        Return all logged messages.

    get_logs_by_level(level: str) -> list[dict]:
        Return only logs matching the given level.

    clear() -> None:
        Clear all logs.

    set_level(level: str) -> None:
        Set the default log level.

---

PART 2: Configuration Singleton

Create a Config singleton that holds application settings.

Class: Config

    __new__: Singleton pattern.
    __init__: Only initialise once. Set up:
        - _settings: empty dict

    set(key: str, value) -> None:
        Set a configuration value.

    get(key: str, default=None):
        Return the value for key, or default if not found.

    get_all() -> dict:
        Return a copy of all settings.

    reset() -> None:
        Clear all settings.

---

PART 3 (HARD): Database Connection Singleton

Create a fake database connection that demonstrates why Singleton matters.

Class: DatabaseConnection

    __new__: Singleton pattern.
    __init__: Only initialise once. Set up:
        - _connected: False
        - _query_count: 0

    connect() -> str:
        Set _connected to True. Return "Connected to database".
        If already connected, return "Already connected".

    disconnect() -> str:
        Set _connected to False. Return "Disconnected".
        If not connected, return "Not connected".

    execute(query: str) -> str:
        If not connected, raise ConnectionError("Not connected to database").
        Increment _query_count.
        Return f"Executed: {query}"

    is_connected() -> bool:
        Return connection status.

    get_query_count() -> int:
        Return total queries executed.

ESTIMATED TIME: 30-45 minutes
"""


# ============================================
# PART 1: Logger Singleton
# ============================================

# YOUR CODE HERE


# ============================================
# PART 2: Configuration Singleton
# ============================================

# YOUR CODE HERE


# ============================================
# PART 3 (HARD): Database Connection Singleton
# ============================================

# YOUR CODE HERE


# ==========================================
# TEST CASES
# ==========================================

if __name__ == "__main__":

    # ==========================================
    # PART 1 TESTS: Logger
    # ==========================================
    print("\n=== Test 1: Logger is Singleton ===")
    try:
        log1 = Logger()
        log2 = Logger()
        assert log1 is log2, "Should be the same instance"

        print(f"  log1 is log2: {log1 is log2}")
        print("Test 1 PASSED!")
    except AssertionError as e:
        print(f"Test 1 FAILED: {e}")
    except Exception as e:
        print(f"Test 1 ERROR: {e}")

    print("\n=== Test 2: Logger Functionality ===")
    try:
        logger = Logger()
        logger.clear()  # Clean slate

        logger.log("App started")
        logger.log("User logged in")
        logger.log("Something broke", "ERROR")

        logs = logger.get_logs()
        assert len(logs) == 3
        assert logs[0] == {"message": "App started", "level": "INFO"}
        assert logs[2] == {"message": "Something broke", "level": "ERROR"}

        errors = logger.get_logs_by_level("ERROR")
        assert len(errors) == 1

        print(f"  Logged {len(logs)} messages, {len(errors)} errors")
        print("Test 2 PASSED!")
    except AssertionError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 ERROR: {e}")

    print("\n=== Test 3: Logger Shared State ===")
    try:
        # Create "another" logger - should be same instance
        another = Logger()
        logs = another.get_logs()
        assert len(logs) == 3, "Should see logs from previous test (same instance!)"

        print("  Shared state confirmed - both references see same logs")
        print("Test 3 PASSED!")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 ERROR: {e}")

    # ==========================================
    # PART 2 TESTS: Config
    # ==========================================
    print("\n=== Test 4: Config is Singleton ===")
    try:
        c1 = Config()
        c2 = Config()
        assert c1 is c2

        print("  Config singleton works")
        print("Test 4 PASSED!")
    except AssertionError as e:
        print(f"Test 4 FAILED: {e}")
    except Exception as e:
        print(f"Test 4 ERROR: {e}")

    print("\n=== Test 5: Config Functionality ===")
    try:
        config = Config()
        config.reset()

        config.set("debug", True)
        config.set("database_url", "sqlite:///test.db")
        config.set("max_connections", 10)

        assert config.get("debug") == True
        assert config.get("database_url") == "sqlite:///test.db"
        assert config.get("missing") is None
        assert config.get("missing", "default") == "default"

        all_settings = config.get_all()
        assert len(all_settings) == 3

        print(f"  Settings: {all_settings}")
        print("Test 5 PASSED!")
    except AssertionError as e:
        print(f"Test 5 FAILED: {e}")
    except Exception as e:
        print(f"Test 5 ERROR: {e}")

    print("\n=== Test 6: Config Shared State ===")
    try:
        another_config = Config()
        assert another_config.get("debug") == True, "Should see settings from same instance"

        print("  Config shared state confirmed")
        print("Test 6 PASSED!")
    except AssertionError as e:
        print(f"Test 6 FAILED: {e}")
    except Exception as e:
        print(f"Test 6 ERROR: {e}")

    # ==========================================
    # PART 3 TESTS (HARD): Uncomment when ready
    # ==========================================

    # print("\n=== Test 7: DB Connection Singleton ===")
    # try:
    #     db1 = DatabaseConnection()
    #     db2 = DatabaseConnection()
    #     assert db1 is db2
    #
    #     print("  DB connection is singleton")
    #     print("Test 7 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 7 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 7 ERROR: {e}")

    # print("\n=== Test 8: DB Connection Usage ===")
    # try:
    #     db = DatabaseConnection()
    #
    #     # Not connected yet
    #     try:
    #         db.execute("SELECT 1")
    #         assert False, "Should raise ConnectionError"
    #     except ConnectionError:
    #         pass
    #
    #     result = db.connect()
    #     assert result == "Connected to database"
    #     assert db.is_connected() == True
    #
    #     # Already connected
    #     assert db.connect() == "Already connected"
    #
    #     # Execute queries
    #     db.execute("SELECT * FROM users")
    #     db.execute("INSERT INTO users VALUES (1, 'Alice')")
    #     assert db.get_query_count() == 2
    #
    #     # Another reference sees same state
    #     db2 = DatabaseConnection()
    #     assert db2.is_connected() == True
    #     assert db2.get_query_count() == 2
    #
    #     db.disconnect()
    #     assert db.is_connected() == False
    #
    #     print("  DB connection works correctly")
    #     print("Test 8 PASSED!")
    # except AssertionError as e:
    #     print(f"Test 8 FAILED: {e}")
    # except Exception as e:
    #     print(f"Test 8 ERROR: {e}")

    print("\n" + "=" * 60)
    print("SINGLETON KEY LESSONS")
    print("=" * 60)
    print("""
1. Singleton ensures only ONE instance of a class exists
2. Override __new__ to control object creation
3. Use a flag (_initialised) to prevent __init__ running multiple times
4. Use cases: loggers, config, DB connections, caches
5. All references to the class share the SAME state
6. Be careful: Singletons can make testing harder (global state)
7. Sometimes dependency injection (DIP) is better than Singleton
""")
    print("=" * 60)
