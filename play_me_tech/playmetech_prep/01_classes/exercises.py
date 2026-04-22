"""
═══════════════════════════════════════════════════════════════════
 TOPIC 1: Python OOP — Classes, Encapsulation & Clean Code
═══════════════════════════════════════════════════════════════════

WHY THIS MATTERS FOR PLAYMETECH:
  The job spec explicitly asks for "clean, maintainable, well-structured
  Python code using OOP principles." Traders will rely on your code running
  correctly in production. Messy procedural scripts don't scale.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 THEORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

A CLASS is a blueprint for creating objects. An OBJECT is an instance
of a class — it has its own data (attributes) and behaviour (methods).

  class Match:
      def __init__(self, home_team, away_team):   # constructor
          self.home_team = home_team               # instance attribute
          self.away_team = away_team

      def label(self):                             # method
          return f"{self.home_team} vs {self.away_team}"

  m = Match("Arsenal", "Chelsea")
  print(m.label())   # "Arsenal vs Chelsea"

THE FOUR PILLARS OF OOP:

  1. ENCAPSULATION — bundle data + behaviour together, hide internals.
     Use _ prefix for "private" attributes by convention.
     Use @property to expose read-only computed values.

  2. INHERITANCE — a child class inherits from a parent class.
     Use super().__init__() to call the parent constructor.

  3. POLYMORPHISM — different classes share the same method name
     but behave differently. Lets you write generic code.

  4. ABSTRACTION — expose only what the user needs; hide complexity.

DUNDER (MAGIC) METHODS:
  __init__     → called on creation
  __repr__     → developer-facing string (used in debugger / REPL)
  __str__      → user-facing string (used by print())
  __eq__       → defines == behaviour
  __lt__       → defines < behaviour (enables sorting)
  __len__      → defines len() behaviour

DATACLASSES (modern shortcut):
  from dataclasses import dataclass, field

  @dataclass
  class Odds:
      home_win: float
      draw: float
      away_win: float

      @property
      def favourite(self) -> str:
          lowest = min(self.home_win, self.draw, self.away_win)
          if lowest == self.home_win: return "home"
          if lowest == self.draw: return "draw"
          return "away"

📚 DOCS TO READ:
  https://docs.python.org/3/tutorial/classes.html
  https://docs.python.org/3/library/dataclasses.html
  https://realpython.com/python3-object-oriented-programming/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 EXERCISES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ─────────────────────────────────────────────────────────────────
# EXERCISE 1 (Beginner) — Basic class
# ─────────────────────────────────────────────────────────────────
# Build a Match class that represents a sports fixture.
# It should store home_team, away_team, and sport (default="football").
# It needs a label() method: "Arsenal vs Chelsea (football)"
# It needs __repr__ that returns the same as label().

class Match:
    # YOUR CODE HERE
    pass

print("hello!")
# ─────────────────────────────────────────────────────────────────
# EXERCISE 2 (Beginner) — Encapsulation & property
# ─────────────────────────────────────────────────────────────────
# Build an Odds class.
# Store home_win, draw, away_win as floats (e.g. 1.9, 3.4, 4.2).
# Add a property `implied_probabilities` that returns a dict:
#   {"home_win": 0.526, "draw": 0.294, "away_win": 0.238}
# Implied probability = 1 / decimal_odds, rounded to 3 decimal places.
# Add a property `favourite` that returns "home_win", "draw", or "away_win"
# — whichever has the lowest decimal odds.

class Odds:
    # YOUR CODE HERE
    pass


# ─────────────────────────────────────────────────────────────────
# EXERCISE 3 (Intermediate) — Inheritance
# ─────────────────────────────────────────────────────────────────
# Create a base class Event with:
#   - attributes: event_id (int), name (str)
#   - method: summary() → returns "Event #<id>: <name>"
#
# Create two child classes:
#   FootballMatch(Event)  — adds home_team, away_team
#     override summary() → "Match #<id>: <home> vs <away>"
#
#   TennisMatch(Event)    — adds player1, player2, surface (default="hard")
#     override summary() → "Tennis #<id>: <p1> v <p2> on <surface>"

class Event:
    # YOUR CODE HERE
    pass

class FootballMatch(Event):
    # YOUR CODE HERE
    pass

class TennisMatch(Event):
    # YOUR CODE HERE
    pass


# ─────────────────────────────────────────────────────────────────
# EXERCISE 4 (Intermediate) — Dunder methods & sorting
# ─────────────────────────────────────────────────────────────────
# Build a BettingMarket class:
#   - attributes: name (str), liquidity (float, i.e. £ available to bet)
#   - __repr__ → "BettingMarket(name='...',  liquidity=...)"
#   - __eq__   → two markets are equal if they have the same name
#   - __lt__   → compare by liquidity (enables sorted())
#
# This lets traders sort markets by depth automatically.

class BettingMarket:
    # YOUR CODE HERE
    pass


# ─────────────────────────────────────────────────────────────────
# EXERCISE 5 (Hard) — Composition & a mini trading ledger
# ─────────────────────────────────────────────────────────────────
# Don't use inheritance here — use COMPOSITION (objects inside objects).
#
# Create a Bet class:
#   - attributes: market (str), stake (float), odds (float)
#   - property `potential_return` → stake * odds, rounded to 2dp
#   - property `profit_if_win`   → potential_return - stake, rounded to 2dp
#
# Create a Ledger class:
#   - holds a list of Bet objects internally
#   - method add_bet(bet: Bet) — appends a bet
#   - method total_staked() → sum of all stakes
#   - method total_potential_return() → sum of all potential_returns
#   - method best_value_bet() → returns the Bet with the highest odds
#   - method summary() → prints a formatted table of all bets:
#
#       Market              Stake     Odds    Potential Return
#       ──────────────────────────────────────────────────────
#       Man Utd to Win      £10.00    2.50    £25.00
#       Over 2.5 Goals      £5.00     1.80    £9.00
#       ──────────────────────────────────────────────────────
#       TOTAL               £15.00            £34.00

class Bet:
    # YOUR CODE HERE
    pass

class Ledger:
    # YOUR CODE HERE
    pass


# ═══════════════════════════════════════════════════════════════════
#  TESTS — run this file to check your answers
# ═══════════════════════════════════════════════════════════════════

def test(description, got, expected):
    status = "✅ PASS" if got == expected else f"❌ FAIL (got {got!r}, expected {expected!r})"
    print(f"  {status}  →  {description}")

print("\n── Exercise 1: Match ──")
try:
    m = Match("Arsenal", "Chelsea")
    test("label()", m.label(), "Arsenal vs Chelsea (football)")
    test("repr",    repr(m),   "Arsenal vs Chelsea (football)")
    m2 = Match("Lakers", "Bulls", sport="basketball")
    test("custom sport", m2.label(), "Lakers vs Bulls (basketball)")
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print("\n── Exercise 2: Odds ──")
try:
    o = Odds(1.9, 3.4, 4.2)
    probs = o.implied_probabilities
    test("home prob",  probs["home_win"], 0.526)
    test("draw prob",  probs["draw"],     0.294)
    test("away prob",  probs["away_win"], 0.238)
    test("favourite",  o.favourite, "home_win")
    o2 = Odds(3.0, 3.0, 2.5)
    test("favourite away", o2.favourite, "away_win")
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print("\n── Exercise 3: Inheritance ──")
try:
    e = Event(1, "Grand Final")
    test("base summary", e.summary(), "Event #1: Grand Final")
    fm = FootballMatch(2, "Premier League Clash", "Arsenal", "Chelsea")
    test("football summary", fm.summary(), "Match #2: Arsenal vs Chelsea")
    tm = TennisMatch(3, "Wimbledon SF", "Djokovic", "Alcaraz")
    test("tennis default surface", tm.summary(), "Tennis #3: Djokovic v Alcaraz on hard")
    tm2 = TennisMatch(4, "Roland Garros", "Nadal", "Federer", surface="clay")
    test("tennis clay", tm2.summary(), "Tennis #4: Nadal v Federer on clay")
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print("\n── Exercise 4: BettingMarket ──")
try:
    m1 = BettingMarket("Match Winner", 50000.0)
    m2 = BettingMarket("Match Winner", 80000.0)
    m3 = BettingMarket("Over 2.5", 20000.0)
    test("eq same name",    m1 == m2, True)
    test("eq diff name",    m1 == m3, False)
    test("lt by liquidity", m3 < m1,  True)
    markets = [m1, m3, m2]
    sorted_names = [m.name + str(m.liquidity) for m in sorted(markets)]
    test("sorted order", sorted_names, ["Over 2.520000.0", "Match Winner50000.0", "Match Winner80000.0"])
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print("\n── Exercise 5: Bet & Ledger ──")
try:
    b1 = Bet("Man Utd to Win", 10.0, 2.5)
    b2 = Bet("Over 2.5 Goals", 5.0, 1.8)
    test("potential return", b1.potential_return, 25.0)
    test("profit if win",    b1.profit_if_win,    15.0)
    ledger = Ledger()
    ledger.add_bet(b1)
    ledger.add_bet(b2)
    test("total staked",           ledger.total_staked(),           15.0)
    test("total potential return", ledger.total_potential_return(),  34.0)
    test("best value bet",         ledger.best_value_bet().market,  "Man Utd to Win")
    print("  ℹ️  (summary() output not auto-tested — call ledger.summary() manually to check formatting)")
except Exception as e:
    print(f"  ❌ ERROR: {e}")

print()
